import streamlit as st

# 앱 제목
st.title("💖 연애 코칭 앱")

# 설명
st.write("현재 상황을 입력하면 연애 조언을 해드립니다.")

# 사용자 입력
situation = st.text_area("현재 연애 고민을 적어주세요")

# 버튼 클릭
if st.button("조언 받기"):

    # 입력 없을 때
    if situation == "":
        st.warning("고민을 입력해주세요!")
    
    # 간단한 조언 시스템
    else:

        # 키워드 기반 답변
        if "고백" in situation:
            advice = "상대방의 반응을 너무 두려워하지 말고 솔직하게 표현해보세요 💌"

        elif "싸움" in situation:
            advice = "감정보다 대화를 우선하면 관계 회복에 도움이 됩니다 🤝"

        elif "연락" in situation:
            advice = "너무 조급해하지 말고 자연스러운 흐름을 유지해보세요 📱"

        elif "이별" in situation:
            advice = "힘든 시기지만 자신을 돌보는 시간이 가장 중요합니다 🌱"

        else:
            advice = "상대방의 감정을 존중하면서 자신의 마음도 솔직하게 표현해보세요 😊"

        # 결과 출력
        st.success(advice)
