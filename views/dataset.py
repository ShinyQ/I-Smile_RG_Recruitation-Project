import streamlit as st
import pandas as pd


def app():
    st.write("### **Dataset Train**")
    df_train = pd.read_csv('Dataset/train.csv', sep=';')
    st.write(df_train)

    st.write("")

    st.write("### **Dataset Test**")
    df_test = pd.read_csv('Dataset/test.csv', sep=';')
    st.write(df_test)

    st.write("")

    st.write("### **Dataset Train Clean**")
    df_train_clean = pd.read_csv('Dataset/train_clean.csv')
    st.write(df_train_clean)

    st.write("")

    st.write("### **Dataset Test Clean**")
    df_test_clean = pd.read_csv('Dataset/test_clean.csv')
    st.write(df_test_clean)
