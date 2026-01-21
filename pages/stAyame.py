import streamlit as st
import pickle
from pathlib import Path
#import warnings
#warnings.filterwarnings('ignore')
st.markdown("""
<style>
     div[data-baseweb="slider"] 
     {
     width: 50% !important;
     border: 2px solid #4CAF50;
     padding: 10px; 
     border-radius: 10px;
     } 
</style>
""", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;background-color:pink; color:black; font-size: 24px;font-weight: bold;">あやめ判定AI</p>', unsafe_allow_html=True)

# このファイルの場所を取得
current_dir = Path.cwd()
data_path = current_dir / "ayame.pkl"
with open(data_path, 'rb') as f:
    model = pickle.load(f)
# 小数のスライダー
# 2列レイアウトを作成 
col1, col2 = st.columns([1, 1]) # 左:スライダー, 右:画像 
with col1:
    SepalLengthCm = st.slider(
        "がくの長さを選択してください",
        min_value=4.3,
        max_value=7.9,
        value=5.0,
        step=0.1  # 0.1刻みで調整可能
    )
    st.write(f"選択された値: {SepalLengthCm}") 
    st.markdown('<hr style="border: 2px solid #ccc;">', unsafe_allow_html=True)
    
    #st.markdown('<p  style="background-color: cyan;"> "---"</p>', unsafe_allow_html=True)
    ###############################################
    SepalWidthCm = st.slider(
        "がくの幅を選択してください",
        min_value=2.0,
        max_value=4.4,
        value=3.0,
        step=0.1  # 0.1刻みで調整可能
    )
    st.markdown('<hr style="border: 2px solid #ccc;">', unsafe_allow_html=True)
    
    #############################################
with col2:
    PetalLengthCm = st.slider(
        "花びらの長さを選択してください",
        min_value=1.0,
        max_value=6.9,
        value=5.0,
        step=0.1  # 0.1刻みで調整可能
    )
    st.write(f"選択された値: {PetalLengthCm}") 
    st.markdown('<hr style="border: 2px solid #ccc;">', unsafe_allow_html=True)
    
    #############################################
    PetalWidthCm = st.slider(
        "花びらの幅を選択してください",
        min_value=0.1,
        max_value=2.5,
        value=1.0,
        step=0.1  # 0.1刻みで調整可能
    )
    st.markdown('<hr style="border: 2px solid #ccc;">', unsafe_allow_html=True)
# with col2:
    # 画像ファイルを表示
if st.checkbox("判定結果を見る"):
    my_list =[[SepalLengthCm ,SepalWidthCm ,PetalLengthCm ,PetalWidthCm]]
    #my_list = [[8.9,3.9,1.60,3.2]]
    pred = model.predict(my_list)
    st.write(f"あなたが採取してきたあやめは{pred[0]}です。")
    st.image(f"{current_dir}/{pred[0]}.jpg",width=300)


howtouse="""
スライダーをクリックして
マウスで操作してください
また、クリックして
左右の矢印キーで操作してください
"""

with st.popover('操作方法'):
    st.markdown(f"<div style = 'font-size:24px; font-weight:bold; width:100'>{howtouse}</div>", unsafe_allow_html=True)