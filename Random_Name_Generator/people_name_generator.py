import streamlit as st
from faker import Faker

fake = Faker()

def generate_names(number_of_names):
    names = [fake.name() for _ in range(number_of_names)]
    return names

st.title("Random Name Generator")

num_names = st.number_input("Enter the Number of names to generate:", min_value=1, max_value=100, value=10, step=1)

button = st.button("Generate Names")
if button:
    names = generate_names(num_names)
    st.subheader("Generated Names")
    for name in names:
        st.write(name)
        

