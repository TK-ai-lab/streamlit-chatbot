import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.organization = st.secrets["OPENAI_PROJECT_ID"]

client = OpenAI(api_key=api_key, project=project_id)

st.title("パスワード付きチャットボット")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "あなたは優秀なアシスタントです。"}
    ]

user_input = st.text_input("あなたのメッセージを入力:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages,
    )
    reply = response.choices[0].message.content.strip()
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    st.write(f"{msg['role'].capitalize()}: {msg['content']}")
