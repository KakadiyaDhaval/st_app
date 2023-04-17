import streamlit as st

st.write("""#   Find Largest Number """)

st.header('Enter any Three Numbers of your choice')

f = st.number_input("First Number")
s = st.number_input("Second Number")
t = st.number_input("Third Number")

largest = max(f,s,t)


# st.subheader('Largest number')
# st.write(largest)


st.subheader(f'Largest number amongst the inputs is {largest}    :thumbsup:')

