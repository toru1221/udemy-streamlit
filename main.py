import streamlit as st
import numpy as np
from PIL import Image
import time


st.title('初めてのWebアプリ')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'起動率： {i+1} %')
    bar.progress(i + 1)
    time.sleep(0.1)

img = Image.open('wallpaperbetter.jpg')
st.image(img, caption='Hatsune Miku', use_column_width=True)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('回答3')




# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('wallpaperbetter.jpg')
#     st.image(img, caption='Hatsune Miku', use_column_width=True)

