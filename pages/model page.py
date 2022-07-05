# Contents of ~/my_app/pages/page_2.py
import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# 예시 용도로 호출
import numpy as np
import time

# st.set_page_config(page_icon='📈' ,layout="wide")

st.title("Model page") # 페이지 제목 뭐로 하죠??
st.sidebar.markdown("# Model page ")
st.write("이 페이지는 ~~ 설명글")
# st.sidebar.header('Menu')

st.sidebar.subheader('Ticker')
name = st.sidebar.selectbox('please select a ticker', ['BTC', 'ETH', 'USDT'])
st.sidebar.subheader('Start Date')
start_date = st.sidebar.date_input('please select a start date', datetime(2022, 5, 4))
# end_date = st.sidebar.date_input('End date', datetime(2022, 7, 4))
end_date = datetime.now()

# https://coinmarketcap.com
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y')) # '%d-%m-%Y'
df = scraper.get_dataframe()


### Pattern Recognition
# 결정할 것
# - 페이지 제목 뭐로 할까요?
# - gradcam plot을 candlestick chart랑 따로 넣어주는지 / 어디에 넣을지
# - 알림 받을 패턴 선택지 넣을지 말지 / sidebar에 넣을지 페이지에 넣을지
# - 패턴 설명 페이지 넣을지 / 어디에 넣을지
# - 레이아웃이 괜찮은지 같이 보기 (probability 위치 옆?아래?..)
# - In progress 문구 위치 어디로
# - fig.show() # 이미지 팝업으로 보여지는 예시
st.header("Pattern Recognition")
st.write("현재 시점을 기준으로 패턴을 감지해 알림을 제공합니다. 어쩌구~")


# 패턴 선택하게 할건지?
# st.sidebar.markdown("#### Select patterns")
st.sidebar.subheader("Select patterns")
st.sidebar.write("알림 받을 패턴을 선택해주세요. (다중 선택 가능)")
rising_wedge = st.sidebar.checkbox('Rising Wedge')
falling_Wedge = st.sidebar.checkbox('Falling Wedge')
ascending_triangle = st.sidebar.checkbox('Ascending Triangle')
descending_triangle = st.sidebar.checkbox('Descending Triangle')
symmetric_triangle = st.sidebar.checkbox('Symmetric Triangle')

num_patterns = rising_wedge + falling_Wedge + ascending_triangle + descending_triangle + symmetric_triangle
if not num_patterns:
    st.sidebar.error("패턴을 한 개 이상 선택해주세요.")

with st.expander("pattern explanation"):
    st.markdown('#### Rising Wedge')
    st.image("/Users/kim_yoonhye/Desktop/TS-컨퍼/rising_wedge.png")
    st.write("설명~~")
    st.markdown('#### Falling Wedge')
    st.write("~~")
# if rising_wedge == True:

# Candle Strick Chart 그리기
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

col1, col2 = st.columns([3,1])
prob_sample = np.random.rand(5,1)

col1.subheader("Candlestick Chart")
col1.plotly_chart(fig, use_container_width=True)

col2.subheader("Probabilities")
with st.spinner("In progress.."): # 문구 위치 어디로
    time.sleep(5)
    col2.write(f'Rising Wedge\n : {prob_sample[0][0]:.2f}')
    col2.write(f'Falling Wedge : {prob_sample[1][0]:.2f}')
    col2.write(f'Ascending Triangle : {prob_sample[2][0]:.2f}')
    col2.write(f'Descending Triangle : {prob_sample[3][0]:.2f}')
    col2.write(f'Symmetric Triangle : {prob_sample[4][0]:.2f}')

# warning box 예시
    rising_wedge = 0.8 
    thresh = 0.7
    if rising_wedge >= thresh:
        st.warning(f"Rising Wedge가 {rising_wedge*100:.0f}% 감지되었습니다.")

# Forecasting Stock Prices
st.write('---')
# fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Price')
st.header("Forecasting Stock Prices")
st.write("미래 ~까지의 종가를 예측....~~")
fig_close = px.line(df, x='Date', y=['Close'])

st.plotly_chart(fig_close)