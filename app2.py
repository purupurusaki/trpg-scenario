import streamlit as st
import time

# --- バグっぽい演出のためのCSS設定 ---
st.markdown("""
<style>
@keyframes glitch {
  0% { transform: translate(0) }
  20% { transform: translate(-2px, 2px) }
  40% { transform: translate(-2px, -2px) }
  60% { transform: translate(2px, 2px) }
  80% { transform: translate(2px, -2px) }
  100% { transform: translate(0) }
}
.buggy-text {
  font-family: 'Courier New', monospace;
  font-size: 30px;
  font-weight: bold;
  color: #33ff33;
  background-color: #000000;
  padding: 15px;
  border: 1px solid #33ff33;
  text-shadow: 2px 2px #ff00ff;
  animation: glitch 0.3s infinite;
  text-align: center;
  margin-bottom: 20px;
}
.error-text {
    color: red;
    font-weight: bold;
    font-family: 'Courier New', monospace;
}
</style>
""", unsafe_allow_html=True)

# --- セッション状態の管理（ページ遷移のため） ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# --- 第1段階：最初の質問 ---
if st.session_state.stage == 1:
    st.title("ゲート起動...")
    st.write("システムチェック完了。")
    st.write("---")
    
    st.subheader("異世界に転生しますか？")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("はい (YES)"):
            st.session_state.stage = 2
            st.rerun() # 画面を更新して次へ
            
    with col2:
        if st.button("いいえ (NO)"):
            # 「いいえ」を押しても無理やり進む演出（あるいはここでループも可）
            with st.spinner("キャンセル中... エラー発生..."):
                time.sleep(1.5)
            st.error("キャンセルできません。プロセスを続行します。")
            time.sleep(1)
            st.session_state.stage = 2
            st.rerun()

# --- 第2段階：最終確認と無限ループの罠 ---
elif st.session_state.stage == 2:
    # バグったタイトル表示
    st.markdown('<div class="buggy-text">本 当 ニ よ ろ し い で す ね ？</div>', unsafe_allow_html=True)
    
    # 選択肢
    choice = st.radio(
        "最終意思確認",
        ["はい、行きます", "いいえ、やめます"],
        index=1 # 最初は「いいえ」に合わせておく（罠）
    )
    
    # 決定ボタンが押された時の処理
    if st.button("決定"):
        if choice == "はい、行きます":
            # 成功ルート
            st.success("認証成功。転送を開始します...")
            with st.spinner("空間接続中..."):
                time.sleep(3)
            st.balloons()
            st.markdown("## ようこそ、新しい世界へ。")
            # ここに転生後の画像などを追加できます
            
        else:
            # 「いいえ」を選んだ時の無限ループ（エラー）演出
            placeholder = st.empty()
            
            # 100回くらいエラーを表示して画面を埋め尽くす演出
            # ※本当の無限ループ(while True)にするとブラウザが固まるため、視覚的なループにします
            error_msg = ""
            for i in range(20):
                error_msg += f"ERROR: CANNOT ABORT process_id_{i*9382}<br>"
                placeholder.markdown(f'<div class="error-text">{error_msg}</div>', unsafe_allow_html=True)
                time.sleep(0.1)
            
            st.error("システムエラー：拒否権ハアリマセン。「はい」ヲ選択シテクダサイ。")