import streamlit as st
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_two_cards, render_info_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="ALx – Learner Journey", layout="wide")

mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=1, horizontal=True)
apply_theme(mode)
render_sidebar_nav("alx")

prog_name = "ALx"
data = PROGRAM_DATA.get(prog_name, {"enrolled": 0, "completed": 0})

render_header(prog_name, mode, PROGRAM_DESCRIPTIONS.get(prog_name))

render_two_cards(
    data["enrolled"],
    data["completed"],
    col1_label="Enrolled Learners",
    col2_label="Graduates",
)

employment_rate = 0.66
employed_within_6_months = round(data["completed"] * employment_rate)

render_info_cards(
    [
        {
            "label": "Employment in 6 Months",
            "value": f"{employment_rate * 100:.0f}%",
            "subtext": "Share of ALx graduates",
            "gradient": "linear-gradient(135deg, rgba(14,165,233,0.95), rgba(56,189,248,0.88))",
        },
    ]
)

# st.markdown(
#     f"""
#     ALx’s blended model continues to move large cohorts from enrollment to job-ready status.
#     The 66% employment outcome is tracked within six months of graduation, affirming
#     the program’s role in accelerating labor-market absorption for roughly
#     <strong>{employed_within_6_months:,}</strong> recent graduates.
#     """.strip()
# )

footer_note()
