import streamlit as st
import random

# 메뉴 리스트
menu_list = [
    "치킨 🍗",
    "피자 🍕",
    "햄버거 🍔",
    "떡볶이 🌶️",
    "초밥 🍣",
    "삼겹살 🥓",
    "파스타 🍝",
    "김치찌개 🍲",
    "라면 🍜",
    "마라탕 🌶️"
]

# 제목
st.title("🍽️ 저녁 메뉴 추천 앱")

# 설명
st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해드립니다!")

# 버튼
if st.button("메뉴 추천 받기"):

    # 랜덤 메뉴 선택
    dinner = random.choice(menu_list)

    # 결과 출력
    st.success(f"오늘 저녁은 👉 {dinner}")
