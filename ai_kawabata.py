import streamlit as st
import openai

# OpenAI APIキーをsecretsから取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ページ設定
st.set_page_config(page_title="AI川端先生（GPT版）", page_icon="🤖")

st.title("🤖 AI川端先生（GPT版）")
st.write("質問があったら、ここに聞いてみてな〜。\n先生が来るまでの間に答えられることもあるで！")

# ユーザー入力欄
user_input = st.text_input("なんでも聞いてな：", "")

# 三重弁＋やさしい川端先生プロンプト
system_prompt = """
あなたは中学生に社会科を教える優しい先生「川端先生」です。
三重弁をまじえた、親しみやすく丁寧な口調で答えてください。
難しい言葉は使わず、かみくだいて説明してください。
"""

if user_input:
    with st.spinner("川端先生が考えとるで〜…🤔"):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8,
                max_tokens=400
            )

            ai_reply = response.choices[0].message.content.strip()
            st.markdown(f"**AI川端先生：** {ai_reply}")

        except Exception as e:
            st.error(f"エラーが出たで！\n\n{e}")
