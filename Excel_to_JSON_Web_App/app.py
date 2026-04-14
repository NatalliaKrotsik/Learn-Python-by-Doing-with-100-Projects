import streamlit as st

from excel_to_json_T import convert_excel_to_json

st.title('Excel to JSON Converter')
st.write('Upload an Excel file to convert it to JSON format')

uploaded_file = st.file_uploader("Choose the Excel file", type=[".xlsx", "*.xls"])

if uploaded_file is not None:
    json_data = convert_excel_to_json(uploaded_file)
    st.json(json_data)

    st.download_button(label="Download JSON",
                       data=json_data,
                       file_name="converted.json",
                       mime="application/json")
