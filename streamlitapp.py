import streamlit as st

# Set the title of the Streamlit app
st.title("Math Operations Calculator")  # Main heading for the app

# Input fields for two numbers
# The user can enter any two numbers (floats or integers)
num1 = st.number_input("Enter the first number:", value=0.0, format="%f")
num2 = st.number_input("Enter the second number:", value=0.0, format="%f")

# Button to trigger calculation
# When the user clicks 'Calculate', all math operations are performed and displayed
if st.button("Calculate"):
    # Addition
    st.write(f"Addition: {num1} + {num2} = {num1 + num2}")
    # Subtraction
    st.write(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    # Multiplication
    st.write(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    # Division (handle division by zero)
    if num2 != 0:
        st.write(f"Division: {num1} / {num2} = {num1 / num2}")
    else:
        st.write("Division: Cannot divide by zero.")

# Notes:
# - Use the number input fields to enter two numbers.
# - Click the 'Calculate' button to see the results of all operations.
# - Division by zero is handled gracefully and displays an appropriate message.
# - You can modify or extend this app to include more operations or features as needed.