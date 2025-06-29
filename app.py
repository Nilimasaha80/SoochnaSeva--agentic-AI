import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# ✅ Read secrets directly (no need to write to os.environ)
chat = ChatOpenAI(
    model_name="openai/gpt-3.5-turbo",  # ✅ must include 'openai/' for OpenRouter
    openai_api_key=st.secrets["OPENAI_API_KEY"],     # ✅ securely stored in Streamlit Secrets
    openai_api_base=st.secrets["OPENAI_API_BASE"]    # ✅ usually 'https://openrouter.ai/api/v1'
)

# ✅ Streamlit UI
st.title("🧠 SoochnaSeva – Rural AI Chatbot 🇮🇳")
st.write("यह एआई चैटबॉट ग्रामीण उपयोगकर्ताओं को हिंदी में सरकारी योजनाओं और खेती से संबंधित सवालों का जवाब देता है।")

query = st.text_input("❓ अपना सवाल लिखें:")

if st.button("📩 पूछें") and query:
    try:
        response = chat([HumanMessage(content=query)])
        st.success(f"📌 जवाब: {response.content}")
    except Exception as e:
        st.error(f"❌ एरर: {str(e)}")

