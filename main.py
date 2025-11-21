import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, x='Date_reported', y='Cumulative_cases', color='Country', title='Casos Acumulados de Covid-19-Ano 2020')
fig1.update_layout(xaxis_title='Data', yaxis_title='Casos Acumulados')
fig1.show()
st.plotly_chart(fig1, use_container_width=True)

df_brasil_usa_india = df.query('Country in ["Brazil", "India", "United States of America"]')
fig2 = px.line(df_brasil_usa_india, x='Date_reported', y='Cumulative_cases', color='Country', title='Casos Acumulados de Covid-19-Ano 2020')
fig2.update_layout(xaxis_title='Data', yaxis_title='Brasil x USA x India')
fig2.show()
st.plotly_chart(fig2, use_container_width=True)

df_brasil_usa_india = df.query('Country in ["Brazil", "India", "United States of America"]')
fig3 = px.pie(df_brasil_usa_india, values='Cumulative_cases', names='Country', title='Casos Acumulados de Covid-19-Ano 2020')
fig3.show()
st.plotly_chart(fig3, use_container_width=True)
