import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import streamlit as st

# Title for the app
st.title("Scientific Graphical Calculator")

# Define a function for basic arithmetic operations
def basic_operations():
    st.subheader("Basic Operations")
    operation = st.selectbox("Choose an operation:", ['+', '-', '*', '/'])
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    
    if st.button("Calculate"):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error! Division by zero.")
                return
        st.write(f"Result: {result}")

# Define a function for scientific operations using SymPy
def scientific_operations():
    st.subheader("Scientific Operations")
    operation = st.selectbox("Choose an operation:", ['Solve Equations', 'Derivative', 'Integral'])
    x = sp.Symbol('x')
    equation = st.text_input("Enter an expression in terms of 'x' (e.g., x**2 + 3*x + 2):")
    
    if st.button("Calculate"):
        try:
            if operation == 'Solve Equations':
                solution = sp.solve(sp.sympify(equation), x)
                st.write(f"Solutions: {solution}")
            elif operation == 'Derivative':
                derivative = sp.diff(sp.sympify(equation), x)
                st.write(f"Derivative: {derivative}")
            elif operation == 'Integral':
                integral = sp.integrate(sp.sympify(equation), x)
                st.write(f"Integral: {integral}")
        except Exception as e:
            st.error(f"Error in computation: {e}")

# Define a function for graphing using Matplotlib and NumPy
def graph_function():
    st.subheader("Graphing")
    func = st.text_input("Enter a function to graph in terms of 'x' (e.g., np.sin(x), x**2):")
    
    if st.button("Plot Graph"):
        try:
            x = np.linspace(-10, 10, 400)  # Generate values from -10 to 10
            y = eval(func)
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_title(f"Graph of {func}")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.grid(True)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting graph: {e}")

# Main function to control the app
def main():
    st.sidebar.title("Calculator Menu")
    option = st.sidebar.selectbox("Choose an option:", ["Basic Operations", "Scientific Operations", "Graph Function"])
    
    if option == "Basic Operations":
        basic_operations()
    elif option == "Scientific Operations":
        scientific_operations()
    elif option == "Graph Function":
        graph_function()

# Run the app
if __name__ == "__main__":
    main()
