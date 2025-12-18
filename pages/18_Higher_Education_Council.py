import streamlit as st
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_two_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="Higher Education Council – Metrics", layout="wide")

# Sidebar appearance toggle + navigation
mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=1, horizontal=True)
apply_theme(mode)
render_sidebar_nav("hec")

prog_name = "Higher Education Council"
data = PROGRAM_DATA.get(prog_name, {"enrolled": 0, "completed": 0})

render_header(prog_name, mode, PROGRAM_DESCRIPTIONS.get(prog_name))

render_two_cards(
    data["completed"],
    data["completed"],
    col1_label="Graduates (HEC)",
    col2_label="Reflected in Overview",
)

overview_total = sum(program["completed"] for program in PROGRAM_DATA.values())
hec_share = (data["completed"] / overview_total * 100) if overview_total else 0

st.markdown(
    f"""
    <div style="background: rgba(15,23,42,0.06); border-radius: 16px; padding: 1.25rem 1.5rem; border: 1px solid rgba(99,102,241,0.18);">
        <p style="margin-bottom: 0.8rem; font-size: 1.05rem;">
            The Higher Education Council has confirmed <strong>{data["completed"]:,}</strong> total graduates.
            This exact figure is synchronized with the national overview, so the consolidated completed tally
            now reads <strong>{overview_total:,}</strong>.
        </p>
        <p style="margin: 0; color: rgba(15,23,42,0.75);">
            HEC graduates make up <strong>{hec_share:,.2f}%</strong> of all completions tracked in this dashboard.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

footer_note()
