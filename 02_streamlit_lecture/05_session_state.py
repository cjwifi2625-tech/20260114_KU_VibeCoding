import streamlit as st

st.title("💾 Session State 예제")
st.markdown("---")

# Session State 초기화
# session_state는 페이지가 새로고침되거나 재실행되어도 값을 유지합니다
if "text_list" not in st.session_state:
    st.session_state.text_list = []

if "flushed_texts" not in st.session_state:
    st.session_state.flushed_texts = []

st.subheader("📝 텍스트 입력")
st.caption("텍스트를 입력하고 '추가' 버튼을 눌러 저장하세요. 여러 개를 저장할 수 있습니다.")

# 텍스트 입력과 추가 버튼을 같은 행에 배치
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input(
        "텍스트를 입력하세요",
        placeholder="여기에 텍스트를 입력하세요...",
        label_visibility="collapsed",
        key="input_text"
    )

with col2:
    add_button = st.button("추가", use_container_width=True)

# '추가' 버튼을 누르면 session_state에 텍스트 저장
if add_button and user_input:
    st.session_state.text_list.append(user_input)
    st.success(f"'{user_input}' 저장되었습니다!")
    
    # 입력 필드 초기화를 위해 rerun
    st.rerun()

# 저장된 텍스트 개수 표시
if st.session_state.text_list:
    st.info(f"현재 {len(st.session_state.text_list)}개의 텍스트가 저장되어 있습니다.")

st.markdown("---")

# Flush 버튼
st.subheader("🔄 Flush 버튼")
st.caption("저장된 모든 텍스트를 출력하고 목록을 비웁니다.")

col1, col2 = st.columns([1, 3])
with col1:
    flush_button = st.button("Flush", type="primary", use_container_width=True)

# Flush된 텍스트 출력 영역 (Flush 버튼 바로 아래에 표시)
if st.session_state.flushed_texts:
    with st.container():
        st.markdown("### 📋 저장된 텍스트 목록:")
        st.markdown("---")
        
        # 저장된 텍스트를 순서대로 출력
        for idx, text in enumerate(st.session_state.flushed_texts, 1):
            st.markdown(f"**{idx}.** {text}")
        
        st.markdown("---")
        st.success(f"총 {len(st.session_state.flushed_texts)}개의 텍스트를 출력했습니다.")
        
        # 출력 영역 초기화 버튼 (선택사항)
        if st.button("출력 초기화", key="clear_output"):
            st.session_state.flushed_texts = []
            st.rerun()

# Flush 버튼을 누르면 저장된 텍스트를 모두 출력
if flush_button:
    if st.session_state.text_list:
        # 출력할 텍스트를 flushed_texts에 저장 (rerun 후에도 보이도록)
        st.session_state.flushed_texts = st.session_state.text_list.copy()
        # 출력 후 목록 초기화
        st.session_state.text_list = []
        st.rerun()
    else:
        st.warning("저장된 텍스트가 없습니다.")

st.markdown("---")