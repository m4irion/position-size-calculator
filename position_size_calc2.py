import streamlit as st

st.set_page_config(page_title="Calculator Input Position Size", layout="centered")

# --- GLOBAL STATE ---
if "active_input" not in st.session_state:
    st.session_state.active_input = None

if "risk" not in st.session_state:
    st.session_state.risk = ""

if "entry" not in st.session_state:
    st.session_state.entry = ""

if "sl" not in st.session_state:
    st.session_state.sl = ""

if "display" not in st.session_state:
    st.session_state.display = ""


# --- FUNCTIONS ---
def press_button(val):
    st.session_state.display += val

def clear():
    st.session_state.display = ""

def save_value():
    if st.session_state.active_input == "risk":
        st.session_state.risk = st.session_state.display
    elif st.session_state.active_input == "entry":
        st.session_state.entry = st.session_state.display
    elif st.session_state.active_input == "sl":
        st.session_state.sl = st.session_state.display
    st.session_state.display = ""
    st.session_state.active_input = None


# --- UI STYLING ---
st.markdown("""
    <style>
        .screen {
            font-size: 46px;
            text-align: right;
            padding: 15px;
            background: #000;
            color: #00e676;
            border-radius: 12px;
            margin-bottom: 25px;
            font-weight: 700;
        }
        .btn {
            background: #1a1a1a;
            padding: 28px 0;
            border-radius: 50%;
            font-size: 24px;
            color: #fff;
            text-align: center;
            cursor: pointer;
        }
        .btn:hover { background: #333; }
        .top-btn {
            background: #333;
            border-radius: 12px;
            padding: 14px;
            text-align: center;
            font-size: 20px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📱 Calculator Input Position Size")


# --- Display ---
st.markdown(f"<div class='screen'>{st.session_state.display}</div>", unsafe_allow_html=True)


# --- INPUT SELECT BUTTONS ---
c1, c2, c3 = st.columns(3)
if c1.button("Risk"):
    st.session_state.active_input = "risk"
    st.session_state.display = st.session_state.risk
if c2.button("Entry"):
    st.session_state.active_input = "entry"
    st.session_state.display = st.session_state.entry
if c3.button("SL"):
    st.session_state.active_input = "sl"
    st.session_state.display = st.session_state.sl


# ONLY show keypad if an input is active
if st.session_state.active_input:

    # keypad layout
    rows = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["0", ".", "⌫"]
    ]

    for row in rows:
        c = st.columns(3)
        for i, key in enumerate(row):
            if c[i].button(key):
                if key == "⌫":
                    st.session_state.display = st.session_state.display[:-1]
                else:
                    press_button(key)

    # save button
    if st.button("OK"):
        save_value()

# CALCULATE BUTTON
if st.button("="):
    try:
        r = float(st.session_state.risk)
        e = float(st.session_state.entry)
        s = float(st.session_state.sl)

        diff = abs(e - s)

        if diff == 0:
            st.session_state.display = "Error"
        else:
            pos = (r / diff) * e
            st.session_state.display = f"{pos:.4f}"
    except:
        st.session_state.display = "Error"
