import streamlit as st

# --- シンプルなFAQデータ ---
faq = {
    "条約": "それはな、国と国とが『こっからはこんなふうにしましょか』って決める大事な約束のことやに。",
    "調べ学習": "まずは何について調べたいんか、はっきりさせてみよな。キーワード集めるんが大事やに。",
    "第一次世界大戦": "もともとは一発のピストルの音から始まったんやけど、それまでにいろんな国が力比べしとったんやわ。",
    "資料の読み取り": "表やグラフをよう見て、数字や言葉から言えることを考えるんがコツやに〜。",
}

# --- ページ設定 ---
st.set_page_config(page_title="AI川端先生", page_icon="🤖")

st.title("🤖 AI川端先生")
st.write("質問があったら、ここに聞いてみてな〜。先生が来るまでの間に答えられることもあるで！")

# --- ユーザー入力 ---
user_input = st.text_input("なんでも聞いてな：", "")

if user_input:
    # キーワードにヒットするかチェック
    reply = None
    for keyword in faq:
        if keyword in user_input:
            reply = faq[keyword]
            break

    if reply:
        st.markdown(f"**AI川端先生：** {reply}")
    else:
        st.markdown("**AI川端先生：** うーん、それはちょっとむずかしいなぁ。ほんまの先生にも聞いてみてな！")
