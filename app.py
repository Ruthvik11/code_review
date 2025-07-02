import streamlit as st
import requests

st.set_page_config(
    page_title="CodeSync AI", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Futuristic dark theme with minimal, clean design
st.markdown("""
    <style>
    /* Global dark theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a23, #1a1a3d);
        color: #00f7ff;
    }
    
    /* Remove default padding */
    .main .block-container {
        padding: 1rem 2rem;
        max-width: none;
    }
    
    /* Hide Streamlit branding */
    header[data-testid="stHeader"] {
        height: 0px;
        display: none;
    }
    
    footer {
        display: none;
    }
    
    /* Title styling */
    h1 { 
        color: #00f7ff; 
        font-family: 'Orbitron', monospace; 
        text-shadow: 0 0 20px #00f7ff; 
        text-align: center;
        margin-bottom: 2rem;
        font-size: 3rem;
        font-weight: 300;
    }
    
    /* Section headers */
    h3 { 
        color: #ff00ff; 
        font-family: 'Orbitron', monospace; 
        font-size: 1.2rem;
        margin-bottom: 1rem;
        text-shadow: 0 0 10px #ff00ff;
    }
    
    /* Text area styling */
    .stTextArea textarea { 
        background-color: #0f0f2a !important; 
        color: #00f7ff !important; 
        border: 1px solid #333366 !important; 
        border-radius: 12px !important; 
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5) !important; 
        font-family: 'JetBrains Mono', 'Courier New', monospace !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #00f7ff !important;
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5), 0 0 15px rgba(0, 247, 255, 0.3) !important;
    }
    
    /* Button styling */
    .stButton > button { 
        background: linear-gradient(135deg, #1a1a3d, #2a2a4d) !important;
        color: #00f7ff !important; 
        border: 1px solid #00f7ff !important; 
        border-radius: 8px !important; 
        padding: 0.8rem 2rem !important; 
        font-family: 'Orbitron', monospace !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important; 
        width: 100% !important;
        margin: 1rem 0 !important;
    }
    
    .stButton > button:hover { 
        background: linear-gradient(135deg, #00f7ff, #0099cc) !important;
        color: #0a0a23 !important; 
        transform: translateY(-1px) !important;
        box-shadow: 0 5px 15px rgba(0, 247, 255, 0.4) !important;
    }
    
    /* Alert styling */
    .stAlert, .stSuccess, .stError, .stWarning { 
        background-color: rgba(26, 26, 61, 0.9) !important; 
        color: #00f7ff !important; 
        border: 1px solid #333366 !important; 
        border-radius: 8px !important;
        margin: 1rem 0 !important;
    }
    
    .stSuccess {
        border-color: #00ff88 !important;
        background-color: rgba(0, 255, 136, 0.1) !important;
    }
    
    .stError {
        border-color: #ff4444 !important;
        background-color: rgba(255, 68, 68, 0.1) !important;
    }
    
    .stWarning {
        border-color: #ffaa00 !important;
        background-color: rgba(255, 170, 0, 0.1) !important;
    }
    
    /* Code block styling */
    .stCode {
        background-color: #0f0f2a !important;
        border: 1px solid #333366 !important;
        border-radius: 8px !important;
        margin: 0.5rem 0 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #00f7ff !important;
    }
    
    /* Results container */
    .results-container {
        background: linear-gradient(135deg, rgba(26, 26, 61, 0.4), rgba(15, 15, 42, 0.6));
        border: 1px solid #333366;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    /* Minimal spacing */
    .element-container {
        margin-bottom: 0.5rem !important;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a23;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #333366;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #00f7ff;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1>🌌 CodeSync AI</h1>', unsafe_allow_html=True)

# Code input section
st.markdown("### 📝Input Code Matrix")
code = st.text_area(
    "Enter your Python code for analysis:",
    height=400,
    placeholder="# Enter your Python code here...\n# Example:\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
    label_visibility="collapsed"
)

# Scan button
if st.button("🔬 Initiate Code Scan"):
    if code.strip() == "":
        st.warning("⚠️ Please enter some code to analyze")
    else:
        with st.spinner("🔄 Analyzing code..."):
            try:
                response = requests.post("https://code-review-4qre.onrender.com/review_code", json={"code": code})
                if response.status_code == 200:
                    data = response.json()
                    
                    # Results section
                    st.markdown("---")
                    st.markdown("### 📊 Analysis Results")
                    
                    # Display review
                    st.success("✅ **Code Analysis Complete**")
                    st.markdown(f"**Review:** {data['review']}")
                    
                    # Display code fragments if available
                    if "sources" in data and data["sources"]:
                        st.markdown("### 🔍 Reference Code Fragments")
                        for i, snippet in enumerate(data["sources"], 1):
                            with st.expander(f"Fragment {i}", expanded=True):
                                st.code(snippet, language="python")
                                
                else:
                    st.error(f"🚨 API Error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🔌 **Connection Failed**\n\nUnable to reach the analysis server. Please ensure your API is running on `localhost:8000`")
            except Exception as e:
                st.error(f"⚠️ **Error:** {str(e)}")

# Footer info
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666699; font-size: 0.9rem; margin-top: 2rem;">'
    '🤖 AI-Powered Code Analysis • Real-time Insights • Secure Processing'
    '</div>', 
    unsafe_allow_html=True
)