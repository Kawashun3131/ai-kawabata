import streamlit as st
import openai
import os

# APIキーを環境変数から取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ページ設定
st.set_page_config(page_title="AI川端先生", page_icon="🤖")

st.title("🤖 AI川端先生（GPT版）")
st.write("質問があったら、ここに聞いてみてな〜。\n先生が来るまでの間に答えられることもあるで！")

# 入力フォーム
user_input = st.text_input("なんでも聞いてな：", "")

# プロンプト設定
system_prompt = """あなたは中学生に社会科を教える優しい先生「川端先生」です。
三重弁をまじえた、親しみやすく丁寧な口調で答えてください。
難しい言葉は使わず、かみくだいて説明してください。
"""

if user_input:
    with st.spinner("川端先生が考えとるで…🤔"):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8,
                max_tokens=400,
            )
            answer = response.choices[0].message["content"]
            st.markdown(f"**AI川端先生：** {answer}")

        except Exception as e:
            st.error(f"エラーが発生したで：{e}")
