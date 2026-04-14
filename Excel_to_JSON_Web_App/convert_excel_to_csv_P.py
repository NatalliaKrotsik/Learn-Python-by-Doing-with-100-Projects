import streamlit as st
import pandas as pd
from io import StringIO


def convert_excel_to_csv(uploaded_file):
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file)

    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)

    return StringIO(csv_data)  # Use StringIO to create a file-like object


st.title('Excel to CSV Converter')
st.write("Upload an Excel file to convert it to CSV format")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    csv_data = convert_excel_to_csv(uploaded_file)

    st.download_button(label="Download CSV",
                       data=csv_data,
                       file_name='converted.csv',
                       mime='text/csv')
