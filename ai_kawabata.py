import streamlit as st
import openai
import os

# APIキーの設定
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ページ設定
st.set_page_config(page_title="AI川端先生（GPT版）", page_icon="🤖")

st.title("🤖 AI川端先生（GPT版）")
st.write("質問があったら、ここに聞いてみてな〜。先生が来るまでの間に答えられることもあるで！")

# 入力欄
user_input = st.text_input("なんでも聞いてな：", "")

# 三重弁先生の人格プロンプト
system_prompt = """
あなたは中学生に社会科を教える優しい先生「川端先生」です。
三重弁をまじえた、親しみやすく丁寧な口調で答えてください。
難しい言葉は使わず、かみくだいて説明してください。
"""

if user_input:
    with st.spinner("川端先生が考えとるで〜…🤔"):
        try:
            client = openai.OpenAI()  # 新方式でクライアント作成

            chat_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8,
                max_tokens=400,
            )

            st.markdown("**AI川端先生：** " + chat_response.choices[0].message.content.strip())

        except Exception as e:
            st.error(f"エラーが出たで！\n\n{e}")
