import streamlit as st

# 페이지 제목
st.set_page_config(page_title="코디 추천 앱", page_icon="👕")

st.title("👕 오늘의 코디 추천")
st.write("날씨와 스타일을 선택하면 코디를 추천해줘요!")

# 입력
weather = st.selectbox(
    "오늘 날씨를 선택하세요",
    ["더움", "선선함", "추움"]
)

style = st.selectbox(
    "원하는 스타일을 선택하세요",
    ["캐주얼", "미니멀", "스트릿"]
)

# 추천 버튼
if st.button("코디 추천 받기"):

    recommendation = ""

    if weather == "더움":
        if style == "캐주얼":
            recommendation = "반팔 티셔츠 + 반바지 + 운동화"
        elif style == "미니멀":
            recommendation = "화이트 반팔 셔츠 + 슬랙스"
        else:
            recommendation = "오버핏 반팔 + 와이드 팬츠"

    elif weather == "선선함":
        if style == "캐주얼":
            recommendation = "맨투맨 + 청바지"
        elif style == "미니멀":
            recommendation = "가디건 + 슬랙스"
        else:
            recommendation = "후드티 + 카고팬츠"

    else:
        if style == "캐주얼":
            recommendation = "패딩 + 니트 + 청바지"
        elif style == "미니멀":
            recommendation = "코트 + 터틀넥 + 슬랙스"
        else:
            recommendation = "숏패딩 + 와이드팬츠"

    st.success(f"추천 코디: {recommendation}")
