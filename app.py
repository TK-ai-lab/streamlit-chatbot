import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.organization = st.secrets["OPENAI_ORGANIZATION_ID"]

PASSWORD = "mypassword"

# パスワード認証
password = st.text_input("パスワードを入力してください", type="password")
if password != PASSWORD:
    st.warning("正しいパスワードを入力してください。")
    st.stop()

# タイトル
st.title("パスワード付きチャットボット")

# メッセージ履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "あなたは優秀なアシスタントです。"}]

# ユーザー入力
user_input = st.text_input("あなたのメッセージを入力:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenAI API にリクエスト
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # ← 必要に応じて gpt-4, gpt-4-turbo に変更
        messages=st.session_state.messages,
        max_tokens=500
    )

    # 応答を保存
    reply = response.choices[0].message.content.strip()
    st.session_state.messages.append({"role": "assistant", "content": reply})

# チャット履歴を表示
for msg in st.session_state.messages[1:]:
    st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
