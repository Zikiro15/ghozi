# library
import streamlit as st

# write
st.title('sofware perhitungan')
st.subheader('perkalian')

#input bilangan pertama
number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama ialah {number1}')

#input bilangan pengali
number2 = st.number_input('masukan bilangan pengali')
st.write(f'bilangan pengali ialah {number1}')

# hasil kali
hasil= number1*number2

if st.button('cek'):
    st.write('anda kena prank')
    st.button('nah kukasih tau')

      
