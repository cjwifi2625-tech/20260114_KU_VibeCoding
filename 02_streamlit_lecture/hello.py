import streamlit as st
import statistics

st.set_page_config(
    page_title="프리미엄 헤드폰 쇼핑몰",
    page_icon="🎧",
    layout="wide"
)

# -------------------------
# CSS로 빨간색 primary 버튼 스타일 정의
# -------------------------
st.markdown(
    """
    <style>
    .primary-btn {
        background-color: #ff4b4b; /* 빨간색 */
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 0.4rem;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
    }
    .primary-btn:hover {
        background-color: #ff2b2b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# 헤더 / 메인 섹션
# -------------------------
st.title("🎧 프리미엄 헤드폰 스토어")
st.subheader("음악을 새롭게 경험하세요.")

st.write(
    """
    고음질, 편안한 착용감, 세련된 디자인까지 갖춘  
    프리미엄 헤드폰을 만나보세요.
    """
)

st.divider()

# -------------------------
# 단일 상품 데이터
# -------------------------
product = {
    "name": "Studio Pro Wireless",
    "price": 29.9,
    "wireless": True,
    "desc": "스튜디오급 사운드와 30시간 배터리.",
    "tag": "베스트셀러",
    "img": "https://images.pexels.com/photos/374870/pexels-photo-374870.jpeg",
    "spec": """
- 드라이버: 40mm 네오디뮴
- 주파수 응답: 20Hz ~ 20kHz
- 블루투스: 5.3
- 배터리: 최대 30시간 재생
- 충전 포트: USB-C
""",
    "shipping": """
- 배송비: 3,000원 (5만원 이상 구매 시 무료)
- 배송기간: 영업일 기준 1~2일
- 교환/반품: 수령일로부터 7일 이내 가능
""",
    "reviews": [
        {"user": "민수", "rating": 5, "text": "저음도 탄탄하고 오래 써도 귀가 편해요."},
        {"user": "지현", "rating": 4, "text": "노이즈 캔슬링이 생각보다 좋습니다."},
        {"user": "현우", "rating": 5, "text": "출퇴근용으로 최고예요."},
    ],
}

# -------------------------
# 별점 표시용 유틸 함수
# -------------------------
def render_stars(rating: float, max_stars: int = 5) -> str:
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    stars = "★" * full_stars
    if half_star and full_stars < max_stars:
        stars += "☆"
        full_stars += 1
    stars += "☆" * (max_stars - full_stars)
    return stars

# -------------------------
# 본문 레이아웃 (좌: 이미지, 우: 정보)
# -------------------------
left, right = st.columns([1, 1])

with left:
    st.image(
        product["img"],
        use_column_width=True,
        caption=product["name"],
    )

with right:
    st.markdown(f"### {product['name']}")
    st.markdown(f"**가격:** {product['price']}만원")
    wireless_text = "무선" if product["wireless"] else "유선"
    st.markdown(f"**타입:** {wireless_text}")
    st.caption(product["tag"])
    st.write(product["desc"])

    # 평균 별점 요약
    ratings = [r["rating"] for r in product["reviews"]]
    avg_rating = statistics.mean(ratings)
    st.markdown(
        f"**평균 별점:** {avg_rating:.1f} / 5.0  "
        f"{render_stars(avg_rating)}  "
        f"({len(ratings)}개 리뷰)"
    )

    # -------------------------
    # 탭: 상세설명 / 리뷰 / 배송정보
    # -------------------------
    detail_tab, review_tab, shipping_tab = st.tabs(
        ["📋 상세설명", "⭐ 리뷰", "🚚 배송정보"]
    )

    with detail_tab:
        st.subheader("상세설명")
        st.markdown(product["spec"])

    with review_tab:
        st.subheader("리뷰")
        for r in product["reviews"]:
            st.markdown(
                f"- **{r['user']}** | {render_stars(r['rating'])} "
                f"({r['rating']}/5)\n\n"
                f"  → {r['text']}"
            )

    with shipping_tab:
        st.subheader("배송 / 교환 / 반품 안내")
        st.markdown(product["shipping"])

    # -------------------------
    # 수량 + 버튼 영역
    # -------------------------
    st.write("")
    quantity = st.number_input(
        "수량",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
        key="qty_single_product",
    )

    btn_col1, btn_col2 = st.columns(2)

    # 장바구니 버튼 (일반 st.button)
    with btn_col1:
        add_cart = st.button("🧺 장바구니에 담기", key="cart_single_product")

    # 구매 버튼 (빨간 primary 스타일)
    # JS로 hidden input 값을 바꿔서 클릭 여부를 감지
    with btn_col2:
        buy_clicked_key = "buy_single_product_clicked"
        if buy_clicked_key not in st.session_state:
            st.session_state[buy_clicked_key] = False

        buy_html = """
        <form action="#" method="post">
            <input type="hidden" name="buy_click" value="0">
            <button class="primary-btn" type="submit">💳 구매하기</button>
        </form>
        """
        buy_event = st.form(key="buy_form", clear_on_submit=True)
        with buy_event:
            # 사실상 표시용으로 HTML 렌더링
            st.markdown(buy_html, unsafe_allow_html=True)
            submitted = st.form_submit_button("hidden_submit", type="secondary", help="")

        if submitted:
            st.session_state[buy_clicked_key] = True

    # -------------------------
    # 버튼 클릭 처리
    # -------------------------
    if add_cart:
        st.success(
            f"'{product['name']}' {quantity}개가 장바구니에 추가되었습니다."
        )

    if st.session_state.get(buy_clicked_key):
        st.warning(
            f"'{product['name']}' {quantity}개를 구매 진행합니다. "
            "(결제 로직은 아직 구현되지 않았습니다.)"
        )
        # 한 번만 표시되도록 초기화
        st.session_state[buy_clicked_key] = False

st.write("")
st.write("---")
st.write("© 2026 Headphone Store. All rights reserved.")
