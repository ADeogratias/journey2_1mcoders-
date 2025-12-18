import streamlit as st
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_two_cards, render_info_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="National Rehabilitation Services – Metrics", layout="wide")

mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=1, horizontal=True)
apply_theme(mode)
render_sidebar_nav("nrs")

prog_name = "National Rehabilitation Services"
data = PROGRAM_DATA.get(prog_name, {"enrolled": 0, "completed": 0})

render_header(prog_name, mode, PROGRAM_DESCRIPTIONS.get(prog_name))

render_two_cards(
    data["enrolled"],
    data["completed"],
    col1_label="Total Participants",
    col2_label="Trained Graduates",
)

ongoing = max(data["enrolled"] - data["completed"], 0)

render_info_cards(
    [
        {
            "label": "Ongoing Trainings",
            "value": f"{ongoing:,}",
            "subtext": "Currently in rehabilitation pathways",
            "gradient": "linear-gradient(135deg, rgba(249,115,22,0.95), rgba(251,191,36,0.85))",
        },
    ]
)

# st.markdown(
#     f"""
#     National Rehabilitation Services is supporting <strong>{ongoing:,}</strong> active participants while
#     <strong>{data['completed']:,}</strong> individuals have already completed their training.
#     Combined, this represents a total footprint of <strong>{data['enrolled']:,}</strong> people advancing
#     through or graduating from NRS training pathways.
#     """,
#     unsafe_allow_html=True,
# )

footer_note()
