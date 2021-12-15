import streamlit as st

from views import home
from views import dataset

st.set_page_config(
    page_title='I-Smile Marketing Target Classification',
    page_icon='https://telkomuniversity.ac.id/wp-content/uploads/2019/07/cropped-favicon-2-32x32.png',
    layout='wide'
)

PAGES = {
    "🌎 Halaman Utama": home,
    "💡 Dataset": dataset,
}

st.sidebar.subheader('Navigasi')

page = st.sidebar.selectbox("Pindah Halaman", list(PAGES.keys()))
page = PAGES[page]
page.app()
