
import streamlit as st
import pandas as pd
import altair as alt

from data import PROGRAM_DATA
from utils import apply_theme, render_header, render_two_cards, footer_note, render_sidebar_nav

st.set_page_config(page_title="Program Metrics Preview", layout="wide")

# Sidebar theme toggle
mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=1, horizontal=True)
apply_theme(mode)
render_sidebar_nav("main")

render_header("One Million Coders Status Overview", mode, "Cross-program performance pulse and totals.")
st.subheader("Aggregated totals across all programs")

total_enrolled = sum(p["enrolled"] for p in PROGRAM_DATA.values())
total_completed = sum(p["completed"] for p in PROGRAM_DATA.values())

render_two_cards(total_enrolled, total_completed)

program_contrib_df = (
    pd.DataFrame(PROGRAM_DATA)
    .T.reset_index()
    .rename(columns={"index": "Program", "enrolled": "Enrolled", "completed": "Completed"})
)
program_contrib_df["Contribution %"] = (
    (program_contrib_df["Completed"] / total_completed) * 100 if total_completed else 0.0
)
program_contrib_df = program_contrib_df.sort_values("Completed", ascending=False).reset_index(drop=True)

st.markdown("### Programs Fueling Completions")
top_contrib = program_contrib_df.head(12)
top_contrib_chart = (
    alt.Chart(top_contrib)
    .mark_bar(cornerRadius=12)
    .encode(
        y=alt.Y("Program:N", sort=top_contrib["Program"].tolist(), title=None),
        x=alt.X("Contribution %:Q", axis=alt.Axis(labels=False, ticks=False, title=None), stack=None),
        color=alt.Color(
            "Contribution %:Q",
            scale=alt.Scale(range=["#C7D2FE", "#6366F1"]),
            legend=None,
        ),
        tooltip=[
            alt.Tooltip("Program:N"),
            alt.Tooltip("Contribution %:Q", format=",.2f"),
            alt.Tooltip("Completed:Q", format=",d"),
        ],
    )
    .properties(height=320)
)
st.altair_chart(top_contrib_chart, use_container_width=True)
st.caption("Hover each bar to view its completion share and counts.")

footer_note()
