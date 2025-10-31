
import streamlit as st
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_two_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="AUCA – Metrics", layout="wide")

# Sidebar theme toggle
mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=0, horizontal=True)
apply_theme(mode)
render_sidebar_nav("auca")

prog_name = "AUCA"
data = PROGRAM_DATA.get(prog_name, {"enrolled": 0, "completed": 0})

render_header(prog_name, mode, PROGRAM_DESCRIPTIONS.get(prog_name))
render_two_cards(data["enrolled"], data["completed"])


footer_note()
