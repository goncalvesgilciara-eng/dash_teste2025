import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('/content/vacinacao.csv')

fig1 = px.line(df, x='date', y='people_fully_vaccinated', color='location', title='Total de Vacinações')
fig1.update_layout(xaxis_title='Data', yaxis_title='Vacinados')
fig1.show()
st.plotly_chart(fig1, use_container_width=True)

df_brasil_usa_india = df.query('location in ["Brazil", "India", "United States"]')
fig2 = px.line(df_brasil_usa_india, x='date', y='people_fully_vaccinated', color='location', title='Total de Vacinações')
fig2.update_layout(xaxis_title='Data', yaxis_title='Brasil x USA x India')
fig2.show()
st.plotly_chart(fig2, use_container_width=True)

df_brasil_usa_india = df.query('location in ["Brazil", "India", "United States"]')
fig3 = px.pie(df_brasil_usa_india, values='people_fully_vaccinated', names='location', title='Total de Vacinações')
fig3.show()
st.plotly_chart(fig3, use_container_width=True)
