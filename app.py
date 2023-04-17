import streamlit as st

st.write("""#   Biggest Number Finder :wave:""")

st.header('User Input Parameters')

f = st.number_input("First Number")
s = st.number_input("Second Number")
t = st.number_input("Third Number")

largest = max(f,s,t)


# st.subheader('Largest number')
# st.write(largest)


st.subheader(f'Biggest number amongst input is {largest}    :thumbsup:')

