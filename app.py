import streamlit as st
import openai

# secrets.toml から APIキーとプロジェクトIDを読み込む
openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.organization = st.secrets["OPENAI_PROJECT_ID"]

# アプリ用パスワード
PASSWORD = "mypassword"

# パスワード入力
password = st.text_input("パスワードを入力してください", type="password")
if password != PASSWORD:
    st.warning("正しいパスワードを入力してください。")
    st.stop()

# タイトル
st.title("🔑 パスワード付きチャットボット")

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "あなたは優秀なアシスタントです。"}
    ]

# ユーザー入力
user_input = st.text_input("あなたのメッセージを入力:")

if user_input:
    # ユーザーのメッセージを履歴に追加
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # OpenAI API 呼び出し
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # gpt-3.5-turbo も可
            messages=st.session_state.messages,
            max_tokens=500,
        )

        reply = response.choices[0].message.content.strip()

        # アシスタントの応答を履歴に追加
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")

# チャット履歴の表示
for msg in st.session_state.messages[1:]:
    st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
