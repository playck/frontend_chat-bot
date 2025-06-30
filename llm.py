from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, FewShotChatMessagePromptTemplate
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from config import answer_examples

store = {}


def get_llm(model='gpt-4.1-nano'):
    llm = ChatOpenAI(model=model)
    return llm

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def get_retriever():
    embedding = OpenAIEmbeddings(
        model='text-embedding-3-large',
        dimensions=2048
    )
    index_name = 'front-end-info-index' 
    database = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embedding)
    retriever = database.as_retriever(search_kwargs={'k': 2})
    return retriever

def get_history_retriever():
    llm = get_llm()
    retriever = get_retriever()
    
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )
    return history_aware_retriever

def get_dictionary_chain():
    dictionary = [
        # 날짜 관련
        "날짜 -> date",
        "시간 -> time", 
        "오늘 -> today",
        "내일 -> tomorrow",
        "어제 -> yesterday",
        "날짜 형식 -> date format",
        "날짜 포맷 -> date format",
        "날짜 포맷팅 -> date formatting",
        "유효한 날짜 -> valid date",
        "날짜 검증 -> date validation",
        "날짜 확인 -> date check",
        "날짜 계산 -> date calculation",
        "로케일 -> locale",
        "한국어 -> korean",
        
        # 숫자 관련
        "숫자 -> number",
        "천단위 -> thousand",
        "콤마 -> comma",
        "콤마 추가 -> add comma",
        "콤마 제거 -> remove comma",
        "천단위 콤마 -> thousand comma",
        "소수점 -> decimal",
        "반올림 -> round",
        "올림 -> ceil", 
        "버림 -> floor",
        "가격 -> price",
        "금액 -> price",
        "가격 표시 -> price format",
        "금액 포맷 -> price format",
        "숫자만 -> numeric only",
        "숫자 입력 -> numeric input",
        "숫자 필터 -> numeric filter",
        "정수 -> integer",
        "실수 -> decimal",
        
        # 폼 관련
        "폼 -> form",
        "변경된 -> changed",
        "수정된 -> modified",
        "변경된 필드 -> changed fields",
        "수정된 값 -> modified values",
        "폼 검증 -> form validation",
        "입력 검증 -> input validation",
        "빈 값 -> empty value",
        "공백 -> empty",
        "필수 -> required",
        "react-hook-form -> react hook form",
        
        # 문자열 관련  
        "문자열 -> string",
        "전화번호 -> phone",
        "휴대폰번호 -> phone number",
        "핸드폰번호 -> phone number", 
        "빈 문자열 -> empty string",
        "공백 문자열 -> empty string",
        
        # 시간 관련
        "시:분 -> time format",
        "HH:mm -> time format",
        "분으로 변환 -> convert to minutes",
        "시간으로 변환 -> convert to time",
        "분 -> minutes",
        "시간 -> time",
        
        # 팝업 관련
        "팝업 -> popup",
        "가운데 -> center",
        "중앙 -> center",
        "중앙 정렬 -> center popup",
        
        # 변환 관련
        "변환 -> convert",
        "파싱 -> parse",
        "참/거짓 -> boolean",
        "배열 -> array",
        "객체 -> object",
        "전체 -> all",
        
        # 검증 관련
        "검증 -> validation",
        "확인 -> check", 
        "유효성 -> validation",
        "체크 -> check",
        "zod -> zod",
        
        # 기타
        "생성 -> generate",
        "만들기 -> create",
        "포맷팅 -> formatting",
        "포맷 -> format",
        "형식 -> format",
        "로케일 -> locale",
        "한국 -> korean",
        "영어 -> english",
        "React -> react",
        "타입스크립트 -> typescript",
        "dayjs -> dayjs",
        
        # 동작 관련
        "추가하기 -> add",
        "제거하기 -> remove", 
        "삭제하기 -> remove",
        "필터링 -> filter",
        "필터 -> filter",
        "계산하기 -> calculate",
        "처리하기 -> process",
        "변경하기 -> change",
        "수정하기 -> modify",
        
        # 상태 관련
        "비어있는 -> empty",
        "빈 -> empty",
        "0 -> zero",
        "공백 -> blank"
    ]
    
    llm = get_llm()
    prompt = ChatPromptTemplate.from_template(f"""
        사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
        만약 변경할 필요가 없다고 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.
        그런 경우에는 질문만 리턴해주세요
        
        사전: {dictionary}
        
        질문: {{question}}
    """)

    dictionary_chain = prompt | llm | StrOutputParser()
    
    return dictionary_chain

def get_rag_chain():
    llm = get_llm()
    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{answer}"),
        ]
    )
    
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=answer_examples,
    )
    
    system_prompt = (
        "당신은 프론트엔드 프로젝트 함수 전문가입니다. 사용자가 필요한 프론트엔드 프로젝트 함수에 대해 질문하면 "
        "아래 제공된 프론트엔드 프로젝트 함수 모음에서 적절한 함수를 찾아 추천해주세요."
        "함수의 사용법과 예제도 함께 제공해주세요."
        "함수와 관련없는 질문일 때는 프론트엔드 유틸 함수 관련 질문만 가능하다고 답변해주세요."
        "만약 정확한 함수가 없다면 해당 함수는 없다고 답변해주세요."
        "답변할 때는 함수명과 간단한 설명을 먼저 제공하고, 코드 예제를 포함해주세요."
        "2-3문장 정도의 간결한 답변을 원합니다."
        "\n\n"
        "{context}"
    )
    
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            few_shot_prompt,
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    history_aware_retriever = get_history_retriever()
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    ).pick('answer')
    
    return conversational_rag_chain

def get_ai_response(user_message):
    dictionary_chain = get_dictionary_chain()
    rag_chain = get_rag_chain()
    function_utils_chain = {"input": dictionary_chain} | rag_chain
    ai_response = function_utils_chain.stream(
        {
            "question": user_message
        },
        config={
            "configurable": {"session_id": "function_utils_session"}
        },
    )

    return ai_response 