import pickle
import streamlit as st
import plotly.graph_objects as go


def predict(df):
    abc = pickle.load(open('model/Model/abc.sav', 'rb'))
    dtc = pickle.load(open('model/Model/dtc.sav', 'rb'))
    gbc = pickle.load(open('model/Model/gbc.sav', 'rb'))
    knn = pickle.load(open('model/Model/knn.sav', 'rb'))
    rfc = pickle.load(open('model/Model/rfc.sav', 'rb'))

    result_rfc = rfc.predict_proba(df)
    result_knn = knn.predict_proba(df)
    result_gbc = gbc.predict_proba(df)
    result_dtc = dtc.predict_proba(df)
    result_abc = abc.predict_proba(df)

    return result_rfc[0], result_knn[0], result_gbc[0], result_dtc[0], result_abc[0]


def predict_class(df):
    st.write("### **Hasil Prediksi Model**")
    rfc, knn, gbc, dtc, abc = predict(df)
    name = ['Random Forest', 'K-Nearest Neighbour', 'Gradient Boost', 'Decision Tree', 'Ada Boost']
    results = [rfc, knn, gbc, dtc, abc]
    df_model = []
    df_prob_0 = []
    df_prob_1 = []
    df_pred = []

    for i, val in zip(name, results):
        status = 'Negatif'

        if val[0] < val[1]:
            status = 'Positif'

        df_model.append(i)
        df_prob_0.append(round(val[0], 2))
        df_prob_1.append(round(val[1], 2))
        df_pred.append(status)

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Model', 'Probabilitas 0', 'Probabilitas 1', 'Prediksi'],
            line_color='darkslategray',
            fill_color='#ff4a3d',
            font=dict(color='white', size=15),
            height=30
        ),
        cells=dict(
            values=[df_model, df_prob_0, df_prob_1, df_pred],
            line_color='darkslategray',
            fill=dict(color='white'),
            height=30,
            font_size=15
        ))
    ])

    fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=600, height=550)
    st.plotly_chart(fig)
