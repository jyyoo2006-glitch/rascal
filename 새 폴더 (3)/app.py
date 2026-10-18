import streamlit as st

# 웹 앱 제목 설정
st.title("텍스트 길이와 단어수를 분석")

# 텍스트 박스에 문장 입력받기
text_input = st.text_area("문장을 입력하세요:")

# 버튼을 누르면 분석을 실행하는 로직
if st.button("분석 실행"):
  if text_input:
    # 1. 전체 문장의 텍스트 길이(글자 수) 계산
    text_length = len(text_input)

    # 2. 단어 수 계산 (공백 기준으로 분리)[cite: 5]
    word_count = len(text_input.split())

    # 결과 출력 레이블/영역[cite: 5]
    st.write(f"텍스트 길이: {text_length}자")
    st.write(f"단어 수: {word_count}개")

    # 단어 수 조건에 따른 코멘트 출력[cite: 5]
    if word_count < 5:
      st.write("조금 짧은 문장이네요. 내용을 더 보완해 볼까요?")[cite: 5]
    elif word_count < 20:
      st.write("적당한 길이의 문장입니다.")[cite: 5]
    else:
      st.write("꽤 긴 문장이네요. 핵심만 줄여 보는 것도 좋겠습니다.")[cite: 5]
  else:
    st.write("문장을 입력해 주세요.")