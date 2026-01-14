import streamlit as st

# ページ設定
st.set_page_config(page_title="転生ゲート", layout="centered")

# === 設定エリア ===
# 飛ばしたい「別のサイト」のURLをここに書いてください
TARGET_URL = "https://google.com" 
# =================

# セッション状態の初期化（ループ中かどうかを記憶する変数）
if 'in_loop' not in st.session_state:
    st.session_state.in_loop = False

# タイトル表示
st.title("🔮 運命の選択")
st.write("あなたは選ばれました。")
st.header("異世界に転生しますか？")

# --- メインの選択肢エリア ---

# 1. YESボタン（押すと別サイトへ飛ぶ）
# ※ link_button は押すとブラウザの新しいタブでURLを開きます
st.link_button("はい (YES)", TARGET_URL, type="primary")

# 2. NOボタン（押すとループモードへ突入）
if st.button("いいえ (NO)"):
    st.session_state.in_loop = True
    st.rerun() # 画面を更新して下の表示を出す

# --- ループエリア（NOを押した人だけに見える） ---
if st.session_state.in_loop:
    st.divider() # 区切り線
    st.error("⚠️ エラー：拒否権限がありません")
    st.write("本当によろしいのですね？")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # このYESを押しても、何も起きない（ループする）
        if st.button("はい、転生しません"):
            st.toast("拒否できません！") # ポップアップでメッセージを出す演出
            # ここで何も変数を変えずに終わるので、
            # 画面が再描画されてもまた「本当によろしいのですね？」に戻ります
            
    with col2:
        # NOを押すとループから抜ける（最初の画面に戻る）
        if st.button("いいえ、やっぱり..."):
            st.session_state.in_loop = False
            st.rerun()