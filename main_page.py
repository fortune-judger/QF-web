import streamlit as st
import pandas as pd
import pyecharts.charts as pye
import pyecharts.globals as pyeg
from pyecharts import options as opts
import streamlit_echarts
from pyecharts.faker import Faker
st.set_page_config(layout="wide")
st.markdown('# Board historical value')


DFindex = pd.read_csv('data/index_history.csv')
DFboard = pd.read_csv('data/board_history.csv')

Lboard = DFboard.iloc[:, 1:].columns.to_list()
Lindex_all = DFindex.iloc[:, 1:].columns.to_list()

# keep most board data
DF = pd.merge(DFboard, DFindex, left_on='日期', right_on='日期', how='left')



##################################
### select
##################################
board = st.sidebar.selectbox('Select a board', options=Lboard)
Lindex = st.sidebar.multiselect('Select index', options=Lindex_all, default=['上证指数'])

##################################
### Plot
##################################
# remove NA board data
DFsel = DF.loc[:, ['日期', board] + Lindex].dropna(axis='index', how='all', subset=[board])

line = pye.Line()
line = line.add_xaxis(DFsel['日期'].to_list())
line = line.add_yaxis(board, DFsel[board].to_list())

for col in Lindex:
    line = line.add_yaxis(col, DFsel[col].to_list())
    
line.set_global_opts(title_opts={"text": board},
                    datazoom_opts=opts.DataZoomOpts(range_start=50, range_end=80, filter_mode='none'),
                    tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='shadow'))

streamlit_echarts.st_pyecharts(line, height='600px')