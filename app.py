import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💕",
    layout="centered"
)

st.title("💕 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# API 키 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("API 키를 찾을 수 없습니다. Secrets 설정을 확인하세요.")
    st.stop()

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요 😊\n\n"
                "연애 고민, 썸, 이별, 재회, 고백 등 무엇이든 상담해 드릴게요."
            )
        }
    ]

# 기존 메시지 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
user_input = st.chat_input("연애 고민을 입력하세요...")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        try:
            with st.spinner("생각 중..."):

                # 시스템 프롬프트
                system_prompt = """
                당신은 공감 능력이 뛰어난 연애 상담 전문가입니다.

                규칙:
                - 친절하고 따뜻하게 답변한다.
                - 사용자의 감정을 먼저 공감한다.
                - 현실적이고 구체적인 조언을 제공한다.
                - 단정적으로 판단하지 않는다.
                - 답변은 한국어로 한다.
                """

                # 최근 대화 기록 구성
                conversation = ""

                for msg in st.session_state.messages[-10:]:
                    role = "사용자" if msg["role"] == "user" else "상담사"
                    conversation += f"{role}: {msg['content']}\n"

                prompt = f"""
                {system_prompt}

                아래는 지금까지의 대화입니다.

                {conversation}

                상담사:
                """

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )

                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

        except Exception as e:
            error_msg = f"오류가 발생했습니다.\n\n{str(e)}"

            st.error(error_msg)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "죄송해요. 일시적인 오류가 발생했어요."
                }
            )

# 사이드바
with st.sidebar:
    st.header("설정")

    if st.button("대화 초기화"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "안녕하세요 😊 연애 고민을 말씀해주세요."
            }
        ]
        st.rerun()
