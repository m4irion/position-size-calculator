import streamlit as st

st.set_page_config(page_title="Position Size Calculator", layout="centered")

# --- Custom UI Style ---
st.markdown("""
    <style>
        .answer-box {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            margin-bottom: 25px;
            color: #00e676;
        }
        .calc-box {
            background-color: #1a1d23;
            padding: 25px;
            border-radius: 15px;
        }
        label {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Position Size Calculator")

# Placeholder for the answer (shows at the top)
answer = st.empty()

st.markdown("<div class='calc-box'>", unsafe_allow_html=True)

# --- Inputs (empty defaults, no forced format) ---
risk = st.text_input("Risk Amount ($)", value="")
entry = st.text_input("Entry Price", value="")
sl = st.text_input("Stop Loss Price", value="")

# --- Calculate Button ---
if st.button("Calculate", type="primary"):

    try:
        risk_val = float(risk)
        entry_val = float(entry)
        sl_val = float(sl)

        distance = abs(entry_val - sl_val)

        if distance == 0:
            answer.markdown("<div class='answer-box'>Error</div>", unsafe_allow_html=True)
        else:
            pos_size = risk_val / distance
            answer.markdown(f"<div class='answer-box'>{pos_size:.4f}</div>", unsafe_allow_html=True)

    except:
        answer.markdown("<div class='answer-box'>Error</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
