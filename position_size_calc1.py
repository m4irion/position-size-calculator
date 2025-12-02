import streamlit as st

st.set_page_config(page_title="Position Size Calculator", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
        .display {
            font-size: 46px;
            text-align: right;
            padding: 15px;
            background-color: #0d0d0d;
            border-radius: 12px;
            color: #00e676;
            margin-bottom: 25px;
            font-weight: 600;
        }
        .key {
            background-color: #222;
            padding: 18px;
            text-align: center;
            border-radius: 50%;
            font-size: 22px;
            color: white;
            cursor: pointer;
            margin: 5px;
        }
        .key:hover {
            background-color: #333;
        }
        .calc-box {
            background-color: #111;
            border-radius: 20px;
            padding: 25px;
        }
        label { color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Position Size Calculator (Simple)")

result_area = st.empty()

st.markdown("<div class='calc-box'>", unsafe_allow_html=True)

risk = st.text_input("Risk Amount ($)", value="")
entry = st.text_input("Entry Price", value="")
sl = st.text_input("Stop Loss Price", value="")

if st.button("Calculate"):
    try:
        r = float(risk)
        e = float(entry)
        s = float(sl)

        distance = abs(e - s)
        if distance == 0:
            result_area.markdown("<div class='display'>Error</div>", unsafe_allow_html=True)
        else:
            size = (r / distance) * e
            result_area.markdown(f"<div class='display'>{size:.4f}</div>", unsafe_allow_html=True)
    except:
        result_area.markdown("<div class='display'>Error</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
