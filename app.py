import streamlit as st
import openai

# OpenAIクライアントを初期化
client = openai.OpenAI()

# APIキーをsecretsから取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

PASSWORD = "mypassword"

password = st.text_input("パスワードを入力してください", type="password")
if password != PASSWORD:
    st.warning("正しいパスワードを入力してください。")
    st.stop()

st.title("My chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "あなたは優秀なアシスタントです。"}]

user_input = st.text_input("あなたのメッセージを入力:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages,
        max_tokens=300
    )
    reply = response.choices[0].message.content.strip()
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages[1:]:
    st.write(f"{msg['role'].capitalize()}: {msg['content']}")
