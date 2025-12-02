import streamlit as st

st.title("Position Size Calculator")

# Blank inputs
risk = st.text_input("Risk (USDT)", "")
entry = st.text_input("Entry", "")
sl = st.text_input("SL", "")

# Calculation
try:
    risk = float(risk)
    entry = float(entry)
    sl = float(sl)
    
    if entry == sl:
        st.write("Entry and SL cannot be the same")
    elif risk <= 0:
        st.write("Risk must be greater than 0")
    else:
        distance = abs(entry - sl)
        units = risk / distance
        value = units * entry

        st.write(f"Units: {units:.4f}")
        st.write(f"Value: {value:.4f} USDT")
except:
    if risk or entry or sl:
        st.write("Please enter valid numbers")
