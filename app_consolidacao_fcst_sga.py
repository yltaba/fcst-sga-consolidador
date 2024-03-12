from io import BytesIO
import streamlit as st
import pandas as pd

st.title('Consolidador - Forecast SGA')

uploaded_files = st.file_uploader("Selecione os arquivos para consolidação", 
                                  accept_multiple_files=True)

dfs = []
if uploaded_files is not None:
    for uploaded_file in uploaded_files:

        dataframe = pd.read_excel(uploaded_file, 
                                  sheet_name='CargaDW_ForecastBR')

        dfs.append(dataframe)

    sga_forecast = pd.concat(dfs, ignore_index=True)

    # towrite = BytesIO()
    # sga_forecast.to_excel(towrite, index=False)
    # towrite.seek(0)
    
    st.write("Tabela final:")
    st.dataframe(sga_forecast)
    # st.success("Arquivo consolidado com sucesso!")
    # st.download_button(label="📥 Download Excel Consolidado",
    #         data=towrite,
    #         file_name='forecast_sga_consolidado.xlsx',
    #         mime="application/vnd.ms-excel")