import streamlit as st
import openai
import os
from dotenv import load_dotenv

# 環境変数からAPIキーを読み込む
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# タイトルの設定
st.title("OpenAI APIチャットボット")

# ユーザー入力の取得
user_input = st.text_input("質問を入力してください：")

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# メッセージ履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 送信ボタンが押されたら
if user_input:
    # ユーザーのメッセージを履歴に追加
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # ユーザーのメッセージを表示
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # OpenAI APIを呼び出し
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
        ]
    )
    
    # アシスタントの応答を取得
    assistant_response = response.choices[0].message.content
    
    # アシスタントの応答を履歴に追加
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    # アシスタントの応答を表示
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
