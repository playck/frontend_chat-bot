import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response  

st.set_page_config(page_title="🔧 프론트엔드 ERP-v2 bot", page_icon="💻")

st.title("💻 프론트엔드 ERP-V2 bot")
st.caption("당신에게 필요한 프론트엔드 함수를 찾아드립니다! 💡")

# 사이드바에 사용 가이드 추가
with st.sidebar:
    st.header("📋 사용 가이드")
    st.markdown("""
    **질문 예시:**
    - 날짜를 포맷팅하는 함수 있어?
    - 폼에서 변경값만 추출하는 방법
    - 이메일 유효성 검사 함수
    - 팝업 관련 함수 있어?
    - 시간을 분으로 변환하고 싶어
    """)

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 초기 환영 메시지
if len(st.session_state.message_list) == 0:
    welcome_message = """
    👋 프론트엔드 ERP-v2 bot입니다.
    
    어떤 프론트엔드 함수가 필요하신가요? 
    예를 들어:
    - "날짜를 YYYY-MM-DD 형식으로 바꾸는 함수 있어?"
    - "React-hook-form에서 변경된 값들만 추출하고 싶어"
    - "이메일 주소 유효성을 확인하는 방법"
    """
    st.session_state.message_list.append({"role": "assistant", "content": welcome_message})

# 채팅 메시지 표시
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
if user_question := st.chat_input(placeholder="프론트엔드 팀 함수에 대해 궁금한 것을 물어보세요! 예: 날짜 포맷팅 함수 있어?"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("적합한 함수를 찾는 중입니다... 🔍"):
        try:
            ai_response = get_ai_response(user_question)
            with st.chat_message("assistant"):
                ai_message = st.write_stream(ai_response)
                st.session_state.message_list.append({"role": "assistant", "content": ai_message})
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
            st.info("API 키가 올바르게 설정되었는지 확인해주세요.")