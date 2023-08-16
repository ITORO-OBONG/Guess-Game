import streamlit as st
import random

st.header("My Guessing Game")
from PIL import Image
img = Image.open("dice.png")
st.sidebar.image(img.resize((500, 400)))
b = st.number_input("PLease input a number from 1 - 6", step =1)
a = random.randint(1,6)

def game (a,b):
   
    if b > 6:
        return("Invalid Input please select a number between 1 and 6")
    else:
        if a ==b:
            return("correct")
        else:
            st.write(f" Your selected number is {b}")
            st.write(f" Random number is {a}")
            return("Wrong, try again")

if st.button("Try your luck"):
    st.write(game(a,b))