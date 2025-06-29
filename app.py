import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# ✅ Load from Streamlit Secrets — these are OpenRouter values
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]

# ✅ Agentic LLM model from OpenRouter
chat = ChatOpenAI(
    model_name="openai/gpt-3.5-turbo",  # ✅ Make sure model name matches OpenRouter's docs
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),  # ✅ Use env or Streamlit secrets
    openai_api_base="https://openrouter.ai/api/v1",  # ✅ Key line for OpenRouter
)

# ✅ Streamlit Chatbot UI
st.title("🧠 SoochnaSeva – Rural AI Chatbot 🇮🇳")
st.write("यह एआई चैटबॉट ग्रामीण उपयोगकर्ताओं को हिंदी में सरकारी योजनाओं और खेती से संबंधित सवालों का जवाब देता है।")

query = st.text_input("❓ अपना सवाल लिखें:")

if st.button("📩 पूछें"):
    response = chat([HumanMessage(content=query)])
    st.success(f"📌 जवाब: {response.content}")
