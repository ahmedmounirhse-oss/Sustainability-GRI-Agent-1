import streamlit as st

# --------------------------------------
# PAGE CONFIG
# --------------------------------------
st.set_page_config(
    page_title="Sustainability GRI Agent",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------
# HEADER
# --------------------------------------
st.markdown("""
<h1 style='text-align:center; color:#2E7D32;'>
    🌍 Sustainability GRI Reporting Agent
</h1>

<p style='text-align:center; font-size:18px;'>
    AI-powered platform for automated sustainability analytics, KPI generation, 
    GRI-aligned narratives, dashboards, and full PDF reporting.
</p>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------------------
# FEATURE CARDS
# --------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="padding:20px; border-radius:12px; background-color:#E8F5E9; 
    box-shadow:0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="color:#1b5e20;">📊 KPI Dashboard</h3>
        <p>Interactive dashboards for Energy, Water, Emissions, and Waste.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding:20px; border-radius:12px; background-color:#E3F2FD; 
    box-shadow:0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="color:#0d47a1;">💬 AI Chat Agent</h3>
        <p>Ask any sustainability question and get GRI-aligned insights powered by Groq LLM.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="padding:20px; border-radius:12px; background-color:#FFF3E0; 
    box-shadow:0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="color:#e65100;">📄 PDF Generator</h3>
        <p>Generate full GRI sustainability reports in polished PDF format.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------------------
# QUICK NAVIGATION
# --------------------------------------
st.subheader("🚀 Quick Navigation")

colA, colB, colC, colD = st.columns(4)

with colA:
    st.page_link("pages/01_Chat_Agent.py", label="💬 Chat Agent")

with colB:
    st.page_link("pages/02_KPI_Dashboard.py", label="📊 KPI Dashboard")

with colC:
    st.page_link("pages/03_Data_Explorer.py", label="📂 Data Explorer")

with colD:
    st.page_link("pages/04_GRI_Report_PDF.py", label="📄 PDF Report Generator")

st.write("")
st.write("")

# --------------------------------------
# FOOTER
# --------------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Developed by Ahmed Mounir | Powered by Streamlit + Groq LLM
</p>
""", unsafe_allow_html=True)
