import streamlit as st

st.set_page_config(page_title="Position Size Calculator", layout="centered")

# --- UI Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #0f1116;
        }
        .calculator-box {
            background-color: #1a1d23;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0px 0px 25px rgba(0,0,0,0.35);
        }
        label, .stTextInput label {
            font-size: 18px !important;
            color: #e0e0e0 !important;
        }
        .result {
            font-size: 26px;
            color: #00e676;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Position Size Calculator")

st.markdown("<div class='calculator-box'>", unsafe_allow_html=True)

# --- Inputs ---
risk = st.number_input("Risk Amount ($)", min_value=0.0, format="%.4f")
entry = st.number_input("Entry Price", min_value=0.0, format="%.4f")
sl = st.number_input("Stop Loss Price", min_value=0.0, format="%.4f")

# --- Calculation ---
if st.button("Calculate", type="primary"):
    if entry == sl:
        st.error("Entry and SL cannot be the same.")
    elif risk <= 0:
        st.error("Risk must be greater than 0.")
    else:
        distance = abs(entry - sl)
        position_size = risk / distance

        st.markdown(
            f"<div class='result'>Position Size: {position_size:.4f} units</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)
