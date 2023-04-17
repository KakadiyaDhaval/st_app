import streamlit as st

st.write("""#   Largest Number Finder """)

st.header('User Input Parameters')

f = st.number_input("First Number")
s = st.number_input("Second Number")
t = st.number_input("Third Number")

largest = max(f,s,t)


# st.subheader('Largest number')
# st.write(largest)


st.subheader(f'Largest number amongst the inputs is {largest}    :thumbsup:')

