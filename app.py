import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# ✅ Load from Streamlit Secrets — these are OpenRouter values
os.environ["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"] = st.secrets["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"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]

# ✅ Agentic LLM model from OpenRouter
chat = ChatOpenAI(
    model_name="openai/gpt-3.5-turbo",  # Or try "mistralai/mistral-7b-instruct"
    temperature=0.7
)

# ✅ Streamlit Chatbot UI
st.title("🧠 SoochnaSeva – Rural AI Chatbot 🇮🇳")
st.write("यह एआई चैटबॉट ग्रामीण उपयोगकर्ताओं को हिंदी में सरकारी योजनाओं और खेती से संबंधित सवालों का जवाब देता है।")

query = st.text_input("❓ अपना सवाल लिखें:")

if st.button("📩 पूछें"):
    response = chat([HumanMessage(content=query)])
    st.success(f"📌 जवाब: {response.content}")
