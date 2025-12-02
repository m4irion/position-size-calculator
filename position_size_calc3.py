import streamlit as st

st.set_page_config(page_title="Calculator Input Position Size", layout="centered")

# --- STATES ---
for key in ["active_input", "risk", "entry", "sl", "display"]:
    if key not in st.session_state:
        st.session_state[key] = "" if key != "active_input" else None

# --- FUNCTIONS ---
def press(val):
    st.session_state.display += val

def backspace():
    st.session_state.display = st.session_state.display[:-1]

def clear():
    st.session_state.display = ""

def save():
    if st.session_state.active_input == "risk":
        st.session_state.risk = st.session_state.display
    elif st.session_state.active_input == "entry":
        st.session_state.entry = st.session_state.display
    elif st.session_state.active_input == "sl":
        st.session_state.sl = st.session_state.display
    st.session_state.display = ""
    st.session_state.active_input = None


# --- STYLING ---
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
            background: #1f1f1f;
            padding: 30px 0;
            border-radius: 50%;
            font-size: 26px;
            color: white;
            text-align: center;
            cursor: pointer;
            width: 100%;
        }
        .btn:active {
            background: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📱 Position Size (Calculator Input)")

# --- DISPLAY SCREEN ---
st.markdown(f"<div class='screen'>{st.session_state.display}</div>", unsafe_allow_html=True)

# --- INPUT MODE BUTTONS ---
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


# --- SHOW CALCULATOR KEYPAD ---
if st.session_state.active_input:

    # Rows in real calculator order
    buttons = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["0", ".", "⌫"],
    ]

    for row in buttons:
        col = st.columns(3)
        for i, key in enumerate(row):
            if col[i].button(key):
                if key == "⌫":
                    backspace()
                else:
                    press(key)

    if st.button("OK"):
        save()


# --- CALCULATE ---
if st.button("="):
    try:
        r = float(st.session_state.risk)
        e = float(st.session_state.entry)
        s = float(st.session_state.sl)

        diff = abs(e - s)
        if diff == 0:
            st.session_state.display = "Error"
        else:
            result = (r / diff) * e
            st.session_state.display = f"{result:.4f}"
    except:
        st.session_state.display = "Error"
