import streamlit as st

from model.preprocessing import map_data
from model.predict import predict_class


def app():
    st.write("## **Marketing Target Classification**")
    st.write("")

    st.write("#### **Data Pelanggan**")
    col1, col2, col3 = st.columns(3)

    with col1:
        umur = st.number_input(label="Umur Pelanggan :", min_value=18, max_value=80)

    with col2:
        saldo = st.number_input(label="Saldo Tahunan :", min_value=0, max_value=999999)

    with col3:
        opt_contact = ['', 'Telefon', 'Handphone', 'Tidak Diketahui']
        contact = st.selectbox('Jenis Kontak :', range(len(opt_contact)), format_func=lambda x: opt_contact[x])

    col4, col5, col6 = st.columns(3)

    with col4:
        opt_pekerjaan = [
            '', 'Admin', 'Pekerja Kasar', 'Pengusaha', 'Pembantu Rumah Tangga',
            'Managemen', 'Pensiun', 'Wiraswasta', 'Pelayanan',
            'Pelajar', 'Teknisi', 'Tidak Bekerja', 'Tidak Diketahui'
        ]

        pekerjaan = st.selectbox('Pekerjaan :', range(len(opt_pekerjaan)), format_func=lambda x: opt_pekerjaan[x])

    with col5:
        opt_marrital = ['', 'Cerai', 'Menikah', 'Lajang']
        marrital = st.selectbox('Status Hubungan :', range(len(opt_marrital)), format_func=lambda x: opt_marrital[x])

    with col6:
        opt_edcation = ['', 'Sekolah Dasar', 'Sekolah Menengah', 'Perguruan Tinggi', 'Tidak Diketahui']
        edukasi = st.selectbox('Pendidikan Terakhir :', range(len(opt_edcation)), format_func=lambda x: opt_edcation[x])

    col7, col8, col9 = st.columns(3)

    with col7:
        default = st.radio('Kredit Default :', ['Ya', 'Tidak'])

    with col8:
        housing = st.radio('Memiliki Pinjaman Perumahan :', ['Ya', 'Tidak'])

    with col9:
        loan = st.radio('Memiliki Pinjaman Pribadi :', ['Ya', 'Tidak'])

    st.write("")
    st.write("#### **Data Kampanye Pasar Sebelumnya**")

    col13, col14, col15 = st.columns(3)

    with col13:
        duration = st.number_input(label="Durasi Terakhir Dikontak (Dalam Detik) :", min_value=0)

    with col14:
        campaign = st.number_input(label="Jumlah Kontak Dilakukan Kampanye Pasar :", min_value=1)

    with col15:
        pdays = st.number_input(label="Jarak Hari Terakhir Kali Dikontak :", min_value=-1)

    col16, col17, col18 = st.columns(3)

    with col16:
        previous = st.number_input(label="Jumlah Dikontak Sebelum Kampanye Pasar :", min_value=0)

    with col17:
        day = st.number_input(label="Tanggal Terakhir Dikontak :", min_value=1, max_value=31)

    col10, col11, col12 = st.columns(3)

    with col12:
        pass

    with col10:
        opt_poutcome = ['', 'Sukses', 'Gagal', 'Tidak Diketahui']
        poutcome = st.selectbox("Hasil Kampanye Pasar Sebelumnya :", range(len(opt_poutcome)),
                                format_func=lambda x: opt_poutcome[x])

    with col11:
        opt_month = [
            '', 'Januari', 'Februari', 'Maret', 'April',
            'Mei', 'Juni', 'Juli', 'Agustus', 'September',
            'Oktober', 'November', 'Desember'
        ]

        month = st.selectbox('Bulan Terakhir Dikontak :', range(len(opt_month)), format_func=lambda x: opt_month[x])

    col19, col20, col21, col22, col23 = st.columns(5)

    with col21:
        st.write("")
        st.write("")
        prediksi = st.button('Prediksi Deposit')

    if prediksi:
        if pekerjaan != 0 and marrital != 0 and edukasi != 0 and contact != 0 and poutcome != 0 and month != 0:
            raw = [
                umur, pekerjaan, marrital, edukasi, default, saldo, housing, loan,
                contact, day, month, duration, campaign, pdays, previous, poutcome
            ]

            value = [
                umur, opt_pekerjaan[pekerjaan], opt_marrital[marrital], opt_edcation[edukasi], default, saldo, housing,
                loan, opt_contact[contact], day, opt_month[month], duration, campaign, pdays, previous, opt_poutcome[poutcome]
            ]

            predict_class(map_data(raw, value))
        else:
            with col19:
                st.markdown('<p style="color:red;font-weight:600">Semua Data Harus Diisi! </p>', unsafe_allow_html=True)
