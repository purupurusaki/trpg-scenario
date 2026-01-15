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

# --- セッション状態の管理 ---
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
            st.rerun()
            
    with col2:
        if st.button("いいえ (NO)"):
            with st.spinner("キャンセル中... エラー発生..."):
                time.sleep(1.5)
            st.error("キャンセルできません。プロセスを続行します。")
            time.sleep(1)
            st.session_state.stage = 2
            st.rerun()

# --- 第2段階：最終確認と無限ループの罠 ---
elif st.session_state.stage == 2:
    st.markdown('<div class="buggy-text">本 当 ニ よ ろ し い で す ね ？</div>', unsafe_allow_html=True)
    
    choice = st.radio(
        "最終意思確認",
        ["はい、行きます", "いいえ、やめます"],
        index=1
    )
    
    if st.button("決定"):
        if choice == "はい、行きます":
            # ★ここに飛ばしたいサイトのURLを入れてください★
            target_url = "https://www.google.com" 
            
            st.success("認証成功。転送シーケンスを開始します。")
            
            # --- ここから3秒間のロード演出 ---
            
            # プログレスバー（読み込みゲージ）と文字を表示する箱を用意
            my_bar = st.progress(0)
            status_text = st.empty() 
            
            # 0%から100%までループ（合計約3秒）
            for i in range(100):
                # 進行度に合わせてメッセージを変える演出
                if i < 30:
                    status_text.text(f"空間座標を計算中... {i}%")
                elif i < 80:
                    status_text.text(f"魂データをアップロード中... {i}%")
                else:
                    status_text.text(f"転送実行中... {i}%")
                
                # 少し待つ（0.03秒 × 100回 = 3秒）
                time.sleep(0.03)
                my_bar.progress(i + 1)
            
            status_text.text("転送完了。Good Luck.")
            time.sleep(0.5) # 最後の余韻
                
            # サイトへ飛ばす
            st.markdown(f'<meta http-equiv="refresh" content="0; url={target_url}">', unsafe_allow_html=True)
            
        else:
            # 無限ループ演出
            placeholder = st.empty()
            error_msg = ""
            for i in range(20):
                error_msg += f"ERROR: CANNOT ABORT process_id_{i*9382}<br>"
                placeholder.markdown(f'<div class="error-text">{error_msg}</div>', unsafe_allow_html=True)
                time.sleep(0.1)
            st.error("システムエラー：拒否権ハアリマセン。「はい」ヲ選択シテクダサイ。")