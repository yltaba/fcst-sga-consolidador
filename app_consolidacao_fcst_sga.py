import streamlit as st
import pandas as pd
from io import BytesIO

def load_excel(file):
    """Load an Excel file into a pandas DataFrame."""
    return pd.read_excel(file)

def concatenate_dataframes(dfs):
    """Concatenate a list of DataFrames into a single DataFrame."""
    return pd.concat(dfs, ignore_index=True, index=0)


# Streamlit app starts here
st.title('Consolidador - Forecast SGA')

uploaded_files = st.file_uploader("Suba os arquivos", accept_multiple_files=True, type=['xlsx'])

if uploaded_files:
    dataframes = [load_excel(file) for file in uploaded_files]
    concatenated_df = concatenate_dataframes(dataframes)

    # Display the concatenated DataFrame
    st.write("Tabela final:")
    st.dataframe(concatenated_df)

    # EXPORT EXCEL
    towrite = BytesIO()
    concatenated_df.to_excel(towrite, index=False)
    towrite.seek(0)
    
    st.dataframe(concatenated_df)
    st.success("Arquivos consolidados com sucesso!")
    st.download_button(label="📥 Download Excel Consolidado",
            data=towrite,
            file_name='forecast_sga_consolidado.xlsx',
            mime="application/vnd.ms-excel")