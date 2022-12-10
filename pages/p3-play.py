import streamlit as st
import pandas as pd
st.markdown('# play page')

# index_file = '/home/william/web/QuantFund/02-history_value/index_data/000001_上证指数.csv'
# DFindex = pd.read_csv(index_file)

slider = st.slider('slider')
if st.checkbox('show slider results:'):
    st.write(slider)

sel = st.selectbox('select a number: ', range(5))
if st.sidebar.checkbox('show select results:'):
    st.write(sel)

st.radio('Sorting hat', ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))

# input
st.text_input("text input", key="Tx")
st.write(st.session_state.Tx)

# layout
col1, col2, col3 = st.sidebar.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df)
st.table(df)


