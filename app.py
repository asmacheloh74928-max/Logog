import streamlit as st

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="ห้องเรียนตรรกศาสตร์คณิตศาสตร์ - Logic Lab",
    page_icon="🧠",
    layout="wide"
)

# 2. ปรับแต่งสไตล์ Retro Pastel
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F5FA;
        font-family: 'Kanit', sans-serif;
    }
    .main-header {
        background: linear-gradient(135deg, #FFD1DC 0%, #E0C3FC 100%);
        border: 3px solid #2B2B2B;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 5px 5px 0px #2B2B2B;
        margin-bottom: 25px;
    }
    .concept-card {
        background-color: #FFFFFF;
        border: 2.5px solid #2B2B2B;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 4px 4px 0px #2B2B2B;
        margin-bottom: 15px;
    }
    .sub-badge {
        background-color: #FFF3B0;
        border: 1.5px solid #2B2B2B;
        border-radius: 8px;
        padding: 4px 10px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 8px;
        color: #2B2B2B;
    }
    .error-popup {
        background-color: #FFD2D2;
        border: 3px solid #D8000C;
        border-radius: 14px;
        padding: 15px;
        color: #D8000C;
        font-weight: bold;
        box-shadow: 4px 4px 0px #D8000C;
        margin-top: 10px;
    }
    .success-popup {
        background-color: #D4EDDA;
        border: 3px solid #28A745;
        border-radius: 14px;
        padding: 15px;
        color: #155724;
        font-weight: bold;
        box-shadow: 4px 4px 0px #28A745;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัวเรื่อง
st.markdown("""
    <div class="main-header">
        <h1 style="color: #2B2B2B; margin: 0;">🧠 ห้องเรียนตรรกศาสตร์คณิตศาสตร์ (Mathematical Logic Lab)</h1>
        <p style="color: #4A4A4A; font-size: 1.1rem; margin-top: 5px;">
            สื่อการเรียนรู้อินเทอร์แอกทีฟ สรุปเนื้อหาสำคัญ และแบบทดสอบประเมินความเข้าใจ
        </p>
    </div>
""", unsafe_allow_html=True)

# เมนูด้านบน
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 1. ประพจน์และตัวเชื่อม", 
    "📊 2. ตารางความจริง & สัจนิรันดร์", 
    "⚖️ 3. การอ้างเหตุผล", 
    "🔍 4. ตัวบ่งปริมาณ", 
    "🧩 5. การเหตุผลแบบอุปนัย"
])

with tab1:
    st.markdown("### 📌 บทที่ 1: ประพจน์และตัวเชื่อมทางตรรกศาสตร์")
    col_content, col_quiz = st.columns([1.2, 1])
    
    with col_content:
        st.markdown("""
        <div class="concept-card">
            <div class="sub-badge">💡 1.1 ประพจน์ (Propositions)</div>
            <ul>
                <li><b>นิยาม:</b> ประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็น <b>"จริง (T)"</b> หรือ <b>"เท็จ (F)"</b> เพียงอย่างใดอย่างหนึ่งเท่านั้น</li>
                <li><b>ประโยคที่ไม่เป็นประพจน์:</b> คำถาม คำสั่ง คำห้าม เช่น "อย่าส่งเสียงดัง", "คุณชื่ออะไร?"</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_quiz:
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.subheader("🎯 แบบทดสอบบทที่ 1")
        ans1 = st.radio(
            "ข้อที่ 1: ข้อใดต่อไปนี้จัดว่าเป็น 'ประพจน์' ?",
            ["ก) กรุณาอย่าเดินลัดสนาม", "ข) 2 + 5 = 10", "ค) ทำไมวันนี้ฝนตก?"],
            index=None
        )
        if ans1 is not None:
            if ans1 == "ข) 2 + 5 = 10":
                st.balloons()
                st.markdown('<div class="success-popup">🎉 ถูกต้องครับ! เป็นประพจน์ที่มีค่าความจริงเป็นเท็จ</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-popup">❌ คุณทำผิดนะ! ลองเลือกใหม่อีกครั้งครับ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
