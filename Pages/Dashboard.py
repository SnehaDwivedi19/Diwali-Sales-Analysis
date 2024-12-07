import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df = pd.read_csv(r'C:\Users\Gallery\Downloads\Diwali_sales_data.csv',encoding='unicode_escape')
df

fig = px.pie(df, 'Gender')
st.plotly_chart(fig)


