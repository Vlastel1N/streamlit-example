import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# Создать большую надпись
st.title("Прогнозирование потребления электроэнергии в Свердловской области")
# Загрузка файла
st.header('Загрузите данные по потреблению за 2 прошедших года и данные модели')
data_actual = st.file_uploader("Загрузите файл (data_actual)", type=["csv"])
data_actual_test = st.file_uploader("Загрузите файл (data_actual_test)", type=["csv"])
cumulative_forecast = st.file_uploader("Загрузите файл (cumulative_forecast)", type=["csv"])
cumulative_forecast_2 = st.file_uploader("Загрузите файл (cumulative_forecast_2)", type=["csv"])



# Если файл загружен
if data_actual is not None and data_actual_test is not None and cumulative_forecast is not None and cumulative_forecast_2 is not None:
    # Прочитать данные в датафрейм
    df = pd.read_csv(data_actual)
    df_test = pd.read_csv(data_actual_test)
    df_forecast = pd.read_csv(cumulative_forecast)
    df_forecast_2 = pd.read_csv(cumulative_forecast_2)
    # Создаем график с несколькими линиями разного цвета
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['sequence_date'], y=df['consumption'], mode='lines', name='Линия 1', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df_test['sequence_date'], y=df_test['consumption'], mode='lines', name='Линия 2', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df_forecast['sequence_date'], y=df_forecast['consumption'], mode='lines', name='Линия 3', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df_forecast_2['sequence_date'], y=df_forecast_2['consumption'], mode='lines', name='Линия 4', line=dict(color='yellow')))

    # Настройте макет графика
    fig.update_layout(
        title='График потребления электроэнергии в Свердловской области и прогноз на 24 часа',
        xaxis_title='Дата',
        yaxis_title='Потребление электроэнергии, МВт',
    )

# Отображаем график в Streamlit
    st.plotly_chart(fig)

# Создаем данные для графика (пример)


