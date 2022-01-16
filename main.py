import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title ('Streamlit 超入門')

st.write('プログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'










# if st.checkbox('Show Image'):
#     img = Image.open('mu-min simple2.png')
#     st.image(img, caption='Mumin', use_column_width=True)

# text = st.text_input('あなたの好きな趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0,100, 50,10)

# 'あなたの好きな趣味: ', text
# 'condition',condition

left_column, right_column=st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 =st.expander('質問項目1')
expander1.write('質問1に答える')
expander2 =st.expander('質問項目2')
expander2.write('質問２に答える')
expander3 =st.expander('質問項目3')
expander3.write('質問３に答える')