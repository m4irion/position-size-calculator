import streamlit as st

st.title("Position Size Calculator")

# Inputs
risk = st.number_input("Risk (USDT)")
entry = st.number_input("Entry")
sl = st.number_input("SL")

# Calculation
if entry != sl and risk != 0:
    distance = abs(entry - sl)
    units = risk / distance
    value = units * entry

    st.write(f"Units: {units:.4f}")
    st.write(f"Value: {value:.4f} USDT")
elif entry == sl:
    st.write("Entry and SL cannot be the same")
