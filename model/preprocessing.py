import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import pickle
from sklearn.preprocessing import LabelEncoder


def convert_categorical(df):
    column = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

    for i, col in enumerate(column):
        encoder = LabelEncoder()
        encoder.classes_ = np.load(f'model/LabelEncoder/encoder-{i}.npy')
        df[col] = encoder.transform(df[col])

    return df


def convert_numeric(df):
    numerical = ['age', 'balance', 'day', 'duration', 'pdays', 'poutcome', 'campaign']
    scaler = pickle.load(open('model/Scaler/scaler.sav', 'rb'))
    df[numerical] = scaler.transform(df[numerical].values)

    return df


def map_data(data, value):
    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.write("#### **Data Yang Diinputkan :**")

        df_show = [[value[k] for k in range(0, 16)]]
        df_show.insert(0, [
            'Umur', 'Pekerjaan', 'Status', 'Edukasi', 'Kredit Default', 'Saldo Tahunan', 'Kredit Rumah',
            'Kredit Pribadi', 'Kontak', 'Hari', 'Bulan', 'Durasi', 'Kampanye', 'Terakhir Dikontak',
            'Kontak Sebelumnya', 'Hasil Kampanye'])

        fig = go.Figure(data=[go.Table(
            columnwidth=200,
            header=dict(
                values=[['<b>Kolom</b>'],
                        ['<b>Hasil Inputan</b>']],
                line_color='darkslategray',
                fill_color='#ff4a3d',
                font=dict(color='white', size=15),
                height=30
            ),
            cells=dict(
                values=df_show,
                line_color='darkslategray',
                fill=dict(color='white'),
                height=30,
                font_size=15)
        )
        ])

        fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=400, height=550)
        st.plotly_chart(fig)

    l_pekerjaan = [
        '', 'admin.', 'blue-collar', 'entrepreneur', 'housemaid',
        'management', 'retired', 'self-employed', 'services',
        'student', 'technician', 'unemployed', 'unknown'
    ]

    l_marrital = ['', 'divorced', 'married', 'single']
    l_education = ['', 'primary', 'secondary', 'tertiary', 'unknown']
    l_contact = ['', 'telephone', 'cellular', 'unknown']
    l_poutcome = ['', 'failure', 'other', 'success', 'unknown']
    l_month = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    data[1] = l_pekerjaan[data[1]]
    data[2] = l_marrital[data[2]]
    data[3] = l_education[data[3]]
    data[8] = l_contact[data[8]]
    data[15] = l_poutcome[data[15]]
    data[10] = l_month[data[10]]

    df_train_raw = [data[k] for k in range(0, 16)]

    for i, val in enumerate(df_train_raw):
        if val == 'Ya':
            df_train_raw[i] = 'yes'
        elif val == 'Tidak':
            df_train_raw[i] = 'no'

    df_train = pd.DataFrame([df_train_raw], columns=[
        'age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan',
        'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome'
    ])

    df_train = convert_categorical(df_train)
    df_train = convert_numeric(df_train)

    with col2:
        st.write("#### **Hasil Preprocessing :**")
        df_show_pre = df_train.iloc[[0]].values.tolist()
        df_show_pre.insert(0, [
            'Umur', 'Pekerjaan', 'Status', 'Edukasi', 'Kredit Default', 'Saldo Tahunan', 'Kredit Rumah',
            'Kredit Pribadi', 'Kontak', 'Hari', 'Bulan', 'Durasi', 'Kampanye', 'Terakhir Dikontak',
            'Kontak Sebelumnya', 'Hasil Kampanye'])

        fig = go.Figure(data=[go.Table(
            columnwidth=200,
            header=dict(
                values=[['<b>Kolom</b>'],
                        ['<b>Hasil Inputan</b>']],
                line_color='darkslategray',
                fill_color='#ff4a3d',
                font=dict(color='white', size=15),
                height=30
            ),
            cells=dict(
                values=df_show_pre,
                line_color='darkslategray',
                fill=dict(color='white'),
                height=30,
                font_size=15,
            ),
        )
        ])

        fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=400, height=550)
        st.plotly_chart(fig)

    return df_train
