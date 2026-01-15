import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="퀴즈 앱",
    page_icon="🎯",
    layout="centered"
)

# ============================================
# 퀴즈 데이터
# ============================================
QUIZ_DATA = [
    {
        "question": "Python에서 리스트를 정의하는 올바른 방법은?",
        "options": ["list = (1, 2, 3)", "list = [1, 2, 3]", "list = {1, 2, 3}", "list = <1, 2, 3>"],
        "answer": 1,  # 인덱스
        "explanation": "Python에서 리스트는 대괄호 []를 사용하여 정의합니다."
    },
    {
        "question": "다음 중 Streamlit의 기본 출력 함수는?",
        "options": ["st.print()", "st.write()", "st.display()", "st.show()"],
        "answer": 1,
        "explanation": "st.write()는 Streamlit에서 가장 많이 사용되는 범용 출력 함수입니다."
    },
    {
        "question": "Session State를 사용하는 이유는?",
        "options": [
            "앱을 더 빠르게 만들기 위해",
            "재실행 시 데이터를 유지하기 위해",
            "코드를 짧게 만들기 위해",
            "에러를 방지하기 위해"
        ],
        "answer": 1,
        "explanation": "Session State는 페이지 재실행 후에도 데이터를 유지하기 위해 사용합니다."
    },
    {
        "question": "다음 중 사용자 입력을 받는 위젯이 아닌 것은?",
        "options": ["st.text_input()", "st.button()", "st.success()", "st.slider()"],
        "answer": 2,
        "explanation": "st.success()는 성공 텍스트를 표시하는 함수로, 입력을 받지 않습니다."
    },
    {
        "question": "Streamlit 앱을 실행하는 명령어는?",
        "options": [
            "python app.py",
            "streamlit app.py",
            "streamlit run app.py",
            "run streamlit app.py"
        ],
        "answer": 2,
        "explanation": "'streamlit run app.py' 명령어로 Streamlit 앱을 실행합니다."
    },
    {
        "question": "다음 중 레이아웃을 만드는 함수가 아닌 것은?",
        "options": ["st.columns()", "st.sidebar", "st.tabs()", "st.image()"],
        "answer": 3,
        "explanation": "st.image()은 이미지를 표시하는 함수이며, 레이아웃 함수가 아닙니다."
    },
    {
        "question": "다음 중 상태 메시지 함수가 아닌 것은?",
        "options": ["st.success()", "st.info()", "st.alert()", "st.warning()"],
        "answer": 2,
        "explanation": "st.alert()는 존재하지 않습니다. st.error()를 사용할 수 있습니다."
    },
    {
        "question": "Streamlit 앱의 페이지 설정을 하는 함수는?",
        "options": [
            "st.page_config()",
            "st.set_page_config()",
            "st.config()",
            "st.setup()"
        ],
        "answer": 1,
        "explanation": "st.set_page_config()을 사용하여 페이지 제목, 아이콘, 레이아웃 등을 설정합니다."
    }
]

# ============================================
# Session State 초기화
# ============================================
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'answers' not in st.session_state:
    st.session_state.answers = []

if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None

if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False

# ============================================
# 함수 정의
# ============================================
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.quiz_finished = False
    st.session_state.selected_answer = None
    st.session_state.answer_submitted = False

def submit_answer():
    st.session_state.answer_submitted = True
    
    current_q = QUIZ_DATA[st.session_state.current_question]
    is_correct = st.session_state.selected_answer == current_q['answer']
    
    st.session_state.answers.append({
        'question_num': st.session_state.current_question + 1,
        'selected': st.session_state.selected_answer,
        'correct': current_q['answer'],
        'is_correct': is_correct
    })
    
    if is_correct:
        st.session_state.score += 1

def next_question():
    st.session_state.current_question += 1
    st.session_state.selected_answer = None
    st.session_state.answer_submitted = False
    
    if st.session_state.current_question >= len(QUIZ_DATA):
        st.session_state.quiz_finished = True

# ============================================
# 메인 UI
# ============================================
st.title("🎯 Python & Streamlit 퀴즈")

# 시작 화면
if not st.session_state.quiz_started:
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📚 퀴즈 정보
        
        - **문제 수**: 8문제
        - **문제 유형**: 객관식 (4지선다)
        - **주제**: Python 기초 & Streamlit
        - **제한 시간**: 없음
        
        ### 📝 규칙
        
        1. 각 문제마다 4개의 선택지가 있습니다
        2. 정답을 선택하고 '제출' 버튼을 클릭하세요
        3. 제출 후 정답 여부를 확인할 수 있습니다
        4. 모든 문제를 풀면 점수를 확인할 수 있습니다
        """)
    
    with col2:
        st.image("image/bear.jpg", use_container_width=True)
        
        st.button("🚀 퀴즈 시작하기", on_click=start_quiz, type="primary", use_container_width=True)
    
    # 사이드바에 통계
    with st.sidebar:
        st.header("📊 퀴즈 통계")
        st.metric("총 문제 수", f"{len(QUIZ_DATA)}문제")
        st.info("퀴즈를 시작하려면 '퀴즈 시작하기' 버튼을 클릭하세요!")

# 퀴즈 진행 중
elif st.session_state.quiz_started and not st.session_state.quiz_finished:
    
    # 사이드바: 진행 상황
    with st.sidebar:
        st.header("📊 진행 상황")
        
        progress = (st.session_state.current_question + 1) / len(QUIZ_DATA)
        st.progress(progress)
        
        st.metric("현재 문제", f"{st.session_state.current_question + 1} / {len(QUIZ_DATA)}")
        st.metric("현재 점수", f"{st.session_state.score}점")
        
        st.divider()
        
        # 답변 내역
        st.subheader("답변 내역")
        if st.session_state.answers:
            for ans in st.session_state.answers:
                if ans['is_correct']:
                    st.success(f"문제 {ans['question_num']}: ✅")
                else:
                    st.error(f"문제 {ans['question_num']}: ❌")
    
    # 현재 문제
    current_q = QUIZ_DATA[st.session_state.current_question]
    
    st.markdown("---")
    st.subheader(f"문제 {st.session_state.current_question + 1}")
    st.markdown(f"### {current_q['question']}")
    
    # 답변 선택
    if not st.session_state.answer_submitted:
        st.session_state.selected_answer = st.radio(
            "답을 선택하세요:",
            range(len(current_q['options'])),
            format_func=lambda x: current_q['options'][x],
            key=f"q_{st.session_state.current_question}"
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            st.button("✅ 제출", on_click=submit_answer, type="primary", use_container_width=True)
    
    # 답변 제출 후
    else:
        last_answer = st.session_state.answers[-1]
        
        # 결과 표시
        if last_answer['is_correct']:
            st.success("🎉 정답입니다!")
            st.balloons()
        else:
            st.error("❌ 오답입니다!")
            st.write(f"**정답**: {current_q['options'][current_q['answer']]}")
        
        # 설명
        with st.expander("💡 해설 보기", expanded=True):
            st.info(current_q['explanation'])
        
        # 다음 문제 버튼
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.session_state.current_question < len(QUIZ_DATA) - 1:
                st.button("➡️ 다음 문제", on_click=next_question, type="primary", use_container_width=True)
            else:
                st.button("🏁 결과 보기", on_click=next_question, type="primary", use_container_width=True)

# 퀴즈 완료
elif st.session_state.quiz_finished:
    st.markdown("---")
    st.header("🏆 퀴즈 완료!")
    
    # 점수 계산
    total_questions = len(QUIZ_DATA)
    score = st.session_state.score
    percentage = (score / total_questions) * 100
    
    # 등급 판정
    if percentage >= 90:
        grade = "S"
        emoji = "🏆"
        message = "완벽합니다!"
        color = "gold"
    elif percentage >= 80:
        grade = "A"
        emoji = "🥇"
        message = "훌륭해요!"
        color = "silver"
    elif percentage >= 70:
        grade = "B"
        emoji = "🥈"
        message = "잘했어요!"
        color = "bronze"
    elif percentage >= 60:
        grade = "C"
        emoji = "🥉"
        message = "괜찮아요!"
        color = "lightblue"
    else:
        grade = "D"
        emoji = "📚"
        message = "조금 더 공부해봐요!"
        color = "lightgray"
    
    # 결과 표시
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"<h1 style='text-align: center; color: {color};'>{emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>등급: {grade}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{message}</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 점수 상세
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("총 문제", f"{total_questions}문제")
    col2.metric("정답", f"{score}문제", f"{percentage:.1f}%")
    col3.metric("오답", f"{total_questions - score}문제")
    col4.metric("등급", grade)
    
    st.markdown("---")
    
    # 상세 결과
    st.subheader("📋 상세 결과")
    
    for i, ans in enumerate(st.session_state.answers):
        question_data = QUIZ_DATA[i]
        
        with st.expander(
            f"문제 {ans['question_num']}: {'✅ 정답' if ans['is_correct'] else '❌ 오답'}",
            expanded=False
        ):
            st.write(f"**질문**: {question_data['question']}")
            st.write(f"**당신의 답**: {question_data['options'][ans['selected']]}")
            st.write(f"**정답**: {question_data['options'][ans['correct']]}")
            st.info(f"💡 {question_data['explanation']}")
    
    st.markdown("---")
    
    # 다시 풀기
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔄 다시 풀기", type="primary", use_container_width=True):
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.session_state.quiz_finished = False
            st.session_state.selected_answer = None
            st.session_state.answer_submitted = False
            st.rerun()
    
    # 공유하기
    st.markdown("---")
    st.subheader("📢 결과 공유하기")
    
    share_text = f"""
🎯 Python & Streamlit 퀴즈 결과

점수: {score}/{total_questions} ({percentage:.1f}%)
등급: {grade}
{message}
    """.strip()
    
    st.text_area("공유 텍스트:", share_text, height=150)
    st.caption("위 텍스트를 복사하여 공유하세요!")

# Footer
st.markdown("---")
st.caption("💡 Streamlit 퀴즈 앱 v1.0 | Session State를 활용한 인터랙티브 퀴즈")
