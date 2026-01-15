import streamlit as st
import time

# --- バグっぽい演出のためのCSS設定 ---
# --- バグっぽい演出のためのCSS設定 ---
st.markdown("""
<style>
/* 既存のアニメーション設定 */
@keyframes glitch {
  0% { transform: translate(0) }
  20% { transform: translate(-2px, 2px) }
  40% { transform: translate(-2px, -2px) }
  60% { transform: translate(2px, 2px) }
  80% { transform: translate(2px, -2px) }
  100% { transform: translate(0) }
}
/* バグ文字のスタイル */
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
  margin-top: 10px;
}
/* エラー文字のスタイル */
.error-text {
    color: red;
    font-weight: bold;
    font-family: 'Courier New', monospace;
    font-size: 16px;
    line-height: 1.2;
}

/* ★★★ ここに追記しました（メニュー隠し） ★★★ */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)         


# --- セッション状態の管理 ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'refused' not in st.session_state:
    st.session_state.refused = False

# --- 第1段階：最初の質問 ---
if st.session_state.stage == 1:
    st.title("ゲート起動...")
    st.write("システムチェック完了。")
    st.write("---")

    # ★変更点1：ボタンより先に「場所取り」をしておく
    # ここにエラーログやバグ文字を表示させるための空き地を作ります
    message_area = st.empty()
    
    # ★変更点2：拒否フラグが立っていたら、ここで（ボタンより上で）表示する
    if st.session_state.refused:
        message_area.markdown('<div class="buggy-text">拒 否 ス ル 権 限 ハ <br>ア リ マ セ ン</div>', unsafe_allow_html=True)
    
    st.subheader("異世界に転生しますか？")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("はい (YES)"):
            st.session_state.stage = 2
            st.rerun()
            
    with col2:
        if st.button("いいえ (NO)"):
            st.session_state.refused = True
            
            # トースト通知
            for _ in range(3):
                st.toast('⚠️ 警告：拒否信号ヲ検知', icon='🚫')
                time.sleep(0.1)
            
            # ★変更点3：エラーログを「message_area（画面上部）」に流し込む
            # まずはエラーログを表示
            log_text = ""
            for i in range(10):
                log_text += f"SYSTEM_ALERT: User_Refusal_Denied_0x{i}A{i*3}<br>"
                # placeholderを使って上のエリアを書き換える
                message_area.markdown(f'<div class="error-text">{log_text}</div>', unsafe_allow_html=True)
                time.sleep(0.1)
                
            # 最後にバグ文字で上書き固定する
            message_area.markdown('<div class="buggy-text">拒 否 ス ル 権 限 ハ <br>ア リ マ セ ン</div>', unsafe_allow_html=True)
            
            # ダメ押しのエラー表示（これはボタンの下に出るが、補助的なのでOK）
            st.error("エラー：アナタノ意思ハ関係アリマセン。「はい」ヲ押シテクダサイ。")

# --- 第2段階：最終確認と無限ループの罠 ---
elif st.session_state.stage == 2:
    # 2段階目も画面上部にバグ文字を出す
    st.markdown('<div class="buggy-text">本 当 ニ よ ろ し い で す ね ？</div>', unsafe_allow_html=True)
    
    choice = st.radio(
        "最終意思確認",
        ["はい、行きます", "いいえ、やめます"],
        index=1
    )
    
    if st.button("決定"):
        if choice == "はい、行きます":
            # ★転送先URL★
            target_url = "https://ccfolia.com/rooms/fjmlLlLSn" 
            
            st.success("認証成功。転送シーケンスを開始します。")
            
            my_bar = st.progress(0)
            status_text = st.empty() 
            
            for i in range(100):
                if i < 30:
                    status_text.text(f"空間座標を計算中... {i}%")
                elif i < 80:
                    status_text.text(f"魂データをアップロード中... {i}%")
                else:
                    status_text.text(f"転送実行中... {i}%")
                time.sleep(0.03)
                my_bar.progress(i + 1)
            
            status_text.text("転送完了。Good Luck.")
            time.sleep(0.5)
            
            st.markdown(f'<meta http-equiv="refresh" content="0; url={target_url}">', unsafe_allow_html=True)
            
        else:
            # 無限ループ演出（これも画面上部に出るように placeholder を使う）
            top_placeholder = st.empty() # 上部に場所を作る
            error_msg = ""
            for i in range(20):
                error_msg += f"ERROR: CANNOT ABORT process_id_{i*9382}<br>"
                top_placeholder.markdown(f'<div class="error-text">{error_msg}</div>', unsafe_allow_html=True)
                time.sleep(0.1)
            st.error("システムエラー：拒否権ハアリマセン。「はい」ヲ選択シテクダサイ。")
