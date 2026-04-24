import streamlit as st
import requests

api_key = ""
url = "https://api.coinmarketcap.com/v1/{api_key}/latest/USD"

def convert(currency, currency_value):
    response = requests.get(url.format(api_key=api_key))
    return response

st.title('Currency Converter: USD ⇌ EUR')

convertion = st.radio('Select Currency Converter', ('USD to EUR', 'EUR to USD'))

input_value = st.number_input("Enter the input amount: ")
button = st.button('Convert')
if convertion == 'USD to EUR':
    if button:
        euros = convert(convertion[:3], input_value)
        st.success(f'The converted amount is {euros}.')
else:
    if button:
        dollars = convert(convertion[:3], input_value)
        st.success(f'The converted amount is {dollars}.')

