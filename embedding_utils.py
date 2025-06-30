import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter

# .env 파일 로드
load_dotenv()


PINECONE_VECTOR_STORE_INDEX_NAME = 'front-end-info-index'

def load_and_split_markdown(file_path):
    """마크다운 파일을 로드하고 헤더별로 분할"""
    
    # 마크다운 헤더별 분할기 설정
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )
    
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    # 문서 분할
    docs = markdown_splitter.split_text(markdown_content)
    
    # 각 문서에 메타데이터 추가
    for i, doc in enumerate(docs):
        doc.metadata.update({
            'source': file_path,
            'chunk_id': i,
            'type': 'frontend_utils'
        })
        
        # 함수명 추출 (헤더에서)
        if 'Header 2' in doc.metadata:
            header = doc.metadata['Header 2']
            if '(' in header and ')' in header:
                function_name = header.split('(')[1].split(')')[0]
                doc.metadata['function_name'] = function_name
    
    return docs

def create_vectorstore(documents, index_name=PINECONE_VECTOR_STORE_INDEX_NAME):
    """문서들을 벡터 스토어에 저장"""
    
    # 환경 변수에서 API 키 가져오기
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    
    if not pinecone_api_key or not openai_api_key:
        raise ValueError("PINECONE_API_KEY와 OPENAI_API_KEY 환경 변수를 설정해주세요!")
    
    # Pinecone 초기화
    pc = Pinecone(api_key=pinecone_api_key)
    
    # OpenAI 임베딩 초기화  
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-large',
        dimensions=2048,
        openai_api_key=openai_api_key
    )
    
    try:
        # 기존 인덱스에서 벡터 스토어 생성
        vectorstore = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embeddings
        )
        
        # 문서 추가
        texts = [doc.page_content for doc in documents]
        metadatas = [doc.metadata for doc in documents]
        
        vectorstore.add_texts(texts=texts, metadatas=metadatas)
        print(f"기존 인덱스 '{index_name}'에 {len(texts)}개 문서를 추가했습니다.")
        
    except Exception as e:
        print(f"기존 인덱스를 찾을 수 없습니다. 새로운 인덱스를 생성합니다: {e}")
        
        # 새로운 인덱스 생성
        vectorstore = PineconeVectorStore.from_documents(
            documents=documents,
            embedding=embeddings,
            index_name=index_name
        )
        print(f"새로운 '{index_name}'를 생성했습니다.")
    
    return vectorstore

def update_embeddings(markdown_file_path='frontend_utils.md'):
    """마크다운 파일을 읽어서 임베딩 업데이트"""
    
    print(f"'{markdown_file_path}' 파일에서 함수들을 로드 중...")
    
    # 마크다운 파일 로드 및 분할
    documents = load_and_split_markdown(markdown_file_path)
    
    print(f"{len(documents)}개의 함수 문서를 찾았습니다.")
    
    # 벡터 스토어 생성/업데이트
    print("벡터 스토어에 임베딩 중...")
    vectorstore = create_vectorstore(documents)
    
    print("임베딩 완료!")
    return vectorstore

def search_functions(query, index_name=PINECONE_VECTOR_STORE_INDEX_NAME, k=3):
    """함수 검색"""
    
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-large',
        dimensions=2048,
        openai_api_key=openai_api_key
    )
    
    vectorstore = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    
    # 유사도 검색
    results = vectorstore.similarity_search(query, k=k)
    
    return results

if __name__ == "__main__":
    # 환경 변수 확인
    if not os.getenv('OPENAI_API_KEY'):
        print("OPENAI_API_KEY 환경 변수를 설정해주세요.")
        exit(1)
    
    if not os.getenv('PINECONE_API_KEY'):
        print("PINECONE_API_KEY 환경 변수를 설정해주세요.")
        exit(1)
    
    # 임베딩 업데이트 실행
    update_embeddings()
    
    # 테스트 검색
    print("\n=== 테스트 검색 ===")
    test_queries = [
        "날짜를 포맷팅하는 함수",
        "배열에서 중복 제거",
        "이메일 유효성 검사"
    ]
    
    for query in test_queries:
        print(f"\n검색어: '{query}'")
        results = search_functions(query, k=1)
        if results:
            print(f"결과: {results[0].metadata.get('function_name', 'Unknown')}")
        else:
            print("결과 없음") 