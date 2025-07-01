import streamlit as st

# Set the title of the Streamlit app
st.title("Simple Input Display App")  # This will appear as the main heading

# Step 1: Take user input using a text input box
user_input = st.text_input("Enter something:")  # Prompts the user to enter text

# Step 2: Display the input if the user has entered something
if user_input:
    # Display the user's input below the input box
    st.write("You entered:", user_input)
    # st.write automatically updates as the user types

# Note:
# - To run this app, use the command: streamlit run streamlitapp.py
# - Streamlit automatically reloads the app when you save changes to this file.
# - You can add more widgets (e.g., number_input, slider, etc.) for more complex apps.