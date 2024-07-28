import pandas as pd
import altair as alt
import streamlit as st
from streamlit_option_menu import option_menu


# Set the page title and icon
st.set_page_config(page_title="Cucian Mobil Thanzels", page_icon="🚗")

st.title("Cucia Mobil Thanzel's")
st.markdown("\n")

opt = option_menu(
    menu_title = None,
    options = ["Introduction", "Analytics"],
    orientation = "horizontal"
)
st.markdown("\n")

if opt == "Introduction":
    st.write('''Website ini bertujuan untuk melihat tingkat kepuasan para pelanggan terhadap cucian Thanzel's. Data yang digunakan didapat dari hasil survey selama 30 hari,
             yang terbagi menjadi beberapa jenis tingkat kepuasan ''')
    st.write('''Dengan X1 adalah "Fasilitas yang disediakan", X2 adalah "Pelayanan yang di sediakan", X3 adalah "Harga" , X4 adalah "Kecepatan pengerjaan". ''')
    
    st.markdown("""
    <style>
    .sidebar-text {
        display: flex;
        align-items: center;
    }
    .sidebar-text img {
        width: 24px;
        height: 24px;
        margin-left: 20px;
    }
    """, unsafe_allow_html=True)

    st.markdown("Website ini dibuat oleh :  ")
    
    st.markdown('''<div class="sidebar-text"> 1. Naufal Tansel 
                <a href="mailto:tanselnaufal39.com" target="_blank">
                <img src="https://cdn.worldvectorlogo.com/logos/gmail-icon.svg" alt="Gmail Logo"></a>
                </a></div>''', unsafe_allow_html=True)
else:
    df1 = pd.read_csv('asd.csv', sep=";")
    # Define the options for the multiselect widget
    kolom_options = ['X1', 'X2', 'X3', 'X4']

    # Create a multiselect widget to select the "Jenis Kepuasan"
    selected_jenis_kepuasan = st.multiselect(
        "Pilih Jenis Kepuasan",
        kolom_options,
        default=['X1']  # Default value when the app is first loaded
    )

    # Filter the DataFrame based on the selected "Jenis Kepuasan"
    filtered_df = df1[df1['Jenis Kepuasan'].isin(selected_jenis_kepuasan)]

    # Create an Altair line chart using the filtered DataFrame
    chart1 = alt.Chart(filtered_df).mark_line().encode(
        alt.X('Hari:O', title='Hari', axis=alt.Axis(format='d',labelAngle=0)),
        alt.Y('Tingkat Kepuasan', title='Tingkat Kepuasan', axis=alt.Axis(format='d'),scale=alt.Scale(domain=[1, filtered_df['Tingkat Kepuasan'].max()])),
        color='Jenis Kepuasan',
        tooltip=['Hari:O', 'Jenis Kepuasan', 'Tingkat Kepuasan']
    ).properties(
        width=800,
        height=400
    )

    st.altair_chart(chart1, use_container_width=True)

    st.markdown(
            """
            <div style="text-align: justify;margin-top:-25px">
                Tingkat kepuasan untuk setiap jenis (X1, X2, X3, X4) bervariasi secara signifikan selama periode 30 hari, 
                yang menunjukkan fluktuasi dalam pengalaman pelanggan.
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write('Untuk titik tertinggi menunjukkan pada rentan pertengahan bulan (hari ke 13- 16) dan pada akhir bulan (hari ke 22-24). Dan untuk titik terendahnya terjadi diawal bulan (hari ke 1-3), pertengahan (hari ke 10-12), dan menjelang akhir bulan (hari ke 22-24).')