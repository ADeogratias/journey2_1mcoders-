
import streamlit as st
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_two_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="The Gym at University – Metrics", layout="wide")

# Sidebar theme toggle
mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=0, horizontal=True)
apply_theme(mode)
render_sidebar_nav("gym_uni")

prog_name = "The Gym at University"
data = PROGRAM_DATA.get(prog_name, {"enrolled": 0, "completed": 0})

render_header(prog_name, mode, PROGRAM_DESCRIPTIONS.get(prog_name))
render_two_cards(data["enrolled"], data["completed"])


footer_note()
