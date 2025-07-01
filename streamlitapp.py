import streamlit as st

# Title for the app
st.title("Simple Input Display App")

# Step 1: Take user input
user_input = st.text_input("Enter something:")

# Step 2: Display the input
if user_input:
    st.write("You entered:", user_input)