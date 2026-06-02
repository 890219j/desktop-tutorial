import streamlit as st

# 1. 網頁基本設定
st.set_page_config(
    page_title="Peter Tsai | 個人簡歷",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 注入高質感自訂 CSS
st.markdown("""
    <style>
    /* 調整背景與主文字顏色 */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    /* 標語與名字樣式 */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(45deg, #ff4b4b, #4b7bec);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #a0a0a0;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    /* 專業卡片樣式 */
    .service-card {
        background-color: #1f242d;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4b7bec;
        margin-bottom: 15px;
        transition: transform 0.3s;
    }
    .service-card:hover {
        transform: translateY(-5px);
        border-left: 5px solid #ff4b4b;
    }
    /* 聯絡資訊樣式 */
    .contact-item {
        font-size: 1.1rem;
        margin-bottom: 10px;
    }
    /* 社群按鈕樣式 */
    .fb-button {
        display: inline-block;
        background-color: #1877f2;
        color: white !important;
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        transition: background 0.3s;
    }
    .fb-button:hover {
        background-color: #145dbf;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# 3. 網頁內容
# =========================================================================

# --- HEADER SECTION (Hero Area) ---
st.markdown('<p class="hero-title">Peter Tsai</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">南台資訊有限公司 | 執行長</p>', unsafe_allow_html=True)

# 宣傳標語 (Slogan)
st.info("💡 **「數據驅動未來，資訊成就價值。我們不只做技術，更為您的企業打造數位轉型的最強引擎。」**")

st.markdown("---")

# --- ABOUT & CONTACT SECTION ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📋 關於我 / 聯絡資訊")
    st.markdown(f"""
    <div class="contact-item">🏢 <b>公司名稱：</b> 南台資訊有限公司</div>
    <div class="contact-item">💼 <b>職稱：</b> 執行長 (CEO)</div>
    <div class="contact-item">📧 <b>電子郵件：</b> <a href="mailto:chtsai@stust.edu.tw" style="color:#4b7bec;">chtsai@stust.edu.tw</a></div>
    <div class="contact-item">📞 <b>連絡電話：</b> 06-253-3131</div>
    """, unsafe_allow_html=True)
    
    # Facebook 連結按鈕
    st.markdown('<a href="https://www.facebook.com/keepbusytsai" target="_blank" class="fb-button">🌐 追蹤我的 Facebook</a>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🎯 執行長核心特質")
    st.success("✔️ **戰略布局：** 引領南台資訊走向現代化架構。")
    st.success("✔️ **技術敏銳：** 專注於雲端、大數據與高效能系統整合。")
    st.success("✔️ **客製化服務：** 深諳企業痛點，量身打造最合適的數位解方。")

st.markdown("---")

# --- SERVICES SECTION ---
st.markdown("### 🚀 南台資訊 - 核心服務項目")
st.write("我們提供全方位的網路資訊技術支援，協助企業在數位浪潮中保持領先：")

services = [
    {"title": "🌐 企業級網頁與系統開發", "desc": "高效能 Web 應用程式、RWD 響應式網站、EPR/CRM 客製化系統開發。"},
    {"title": "☁️ 雲端架構部署與維護", "desc": "AWS / GCP / Azure 雲端環境建置、雲端遷移、微服務架構與自動化運維 (DevOps)。"},
    {"title": "🔒 網路資訊安全防護", "desc": "資安漏洞檢測、系統防禦升級、SSL 憑證部署，確保企業商務數據萬無一失。"},
    {"title": "⚡ 數位轉型與技術顧問", "desc": "針對傳統流程進行科技賦能，提供最頂層的資訊架構規劃與技術顧問服務。"}
]

for svc in services:
    st.markdown(f"""
    <div class="service-card">
        <h4 style="margin-top:0; color:#ffffff;">{svc['title']}</h4>
        <p style="margin-bottom:0; color:#b0b0b0;">{svc['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 南台資訊有限公司. Designed with ❤️ using Streamlit & Vibe Coding.")