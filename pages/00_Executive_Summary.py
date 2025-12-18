import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from data import PROGRAM_DATA, PROGRAM_DESCRIPTIONS
from utils import apply_theme, render_header, render_sidebar_nav, footer_note

st.set_page_config(page_title="Executive Summary – Strategic Progress", layout="wide")

st.info("Executive Summary is temporarily hidden while updates are in progress.")
st.stop()

# Sidebar theme toggle + theming
mode = st.sidebar.radio("Appearance", ["Light", "Dark"], index=1, horizontal=True)
apply_theme(mode)
render_sidebar_nav("exec_summary")

render_header(
    "Executive Summary – Strategic Progress",
    mode,
    "Snapshot of NST2 progress to date with cumulative performance, early projections, and program momentum.",
)

is_dark = mode.lower() == "dark"

# --- CONFIGURABLE PLACEHOLDERS (replace with live data later) ---
target_by_year_df = pd.DataFrame(
    [
        {"Year": "2024/25", "Target": 152_000},
        {"Year": "2025/26", "Target": 212_000},
        {"Year": "2026/27", "Target": 302_000},
        {"Year": "2027/28", "Target": 362_000},
        {"Year": "2028/29", "Target": 472_000},
    ]
)

target_first_two_years = int(target_by_year_df.loc[:1, "Target"].sum())
total_target = int(target_by_year_df["Target"].sum())
total_completed = sum(program["completed"] for program in PROGRAM_DATA.values())
total_enrolled = sum(program["enrolled"] for program in PROGRAM_DATA.values())
cumulative_progress_pct = (total_completed / target_first_two_years) * 100 if target_first_two_years else 0

# --- LAYOUT ---
top_col_left, top_col_right = st.columns([2.3, 1.2], gap="large")

with top_col_left:
    st.markdown("#### Target by Year")
    palette = ["#1E3A8A", "#0EA5E9", "#10B981", "#F97316", "#F43F5E"]
    base_chart = alt.Chart(target_by_year_df).encode(
        y=alt.Y("Year:N", sort=list(target_by_year_df["Year"])[::-1], title=None),
        x=alt.X("Target:Q", title="Learners", axis=alt.Axis(format=",.0f")),
        color=alt.Color("Year:N", scale=alt.Scale(range=palette), legend=None),
        tooltip=[alt.Tooltip("Year:N"), alt.Tooltip("Target:Q", format=",d")],
    )
    bars = base_chart.mark_bar(radius=14)
    labels = base_chart.mark_text(
        align="left",
        baseline="middle",
        dx=8,
        color="#ffffff",
        fontWeight="bold",
        fontSize=13,
    ).encode(text=alt.Text("Target:Q", format=",d"))

    st.altair_chart((bars + labels).properties(height=280, padding={"left": 10, "right": 10, "top": 10, "bottom": 10}), use_container_width=True)


# with top_col_right:
st.markdown("#### Cumulative Snapshot Y1 & Y2")
# st.markdown("#### Cumulative Snapshot")

in_progress = max(total_enrolled - total_completed, 0)
projected_total = total_completed + in_progress
gap_raw = target_first_two_years - projected_total
overall_total = 1000000 #adding this for now 
gap_positive = max(gap_raw, 0)
# completed_pct = (total_completed / target_first_two_years * 100) if target_first_two_years else 0
# projected_pct = (projected_total / target_first_two_years * 100) if target_first_two_years else 0
completed_pct = (total_completed / overall_total * 100) if target_first_two_years else 0
projected_pct = (projected_total / overall_total * 100) if target_first_two_years else 0


gauge_bg = "rgba(148,163,184,0.12)" if not is_dark else "rgba(30,41,59,0.45)"
primary_color = "#6366F1" if not is_dark else "#A5B4FC"
pipeline_color = "#14B8A6" if not is_dark else "#2DD4BF"
gap_color = "#EF4444" if gap_positive > 0 else "#22C55E"

completion_pulse_fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=max(min(completed_pct, 100), 0),
        number={"suffix": "%", "font": {"size": 52, "family": "Inter, sans-serif"}},
        # title={"text": "Completion Pulse Y1 & Y2", "font": {"size": 20}},
        title={"text": "Overall Completion Pulse", "font": {"size": 20}},
        gauge={
            "axis": {"range": [0, 100], "tickmode": "array", "tickvals": [0, 25, 50, 75, 100]},
            "bar": {"color": primary_color, "thickness": 0.34},
            "bgcolor": gauge_bg,
            "steps": [
                {"range": [0, 50], "color": "rgba(99,102,241,0.22)"},
                {"range": [50, 80], "color": "rgba(59,130,246,0.2)"},
                {"range": [80, 100], "color": "rgba(16,185,129,0.25)"},
            ],
            "threshold": {
                "line": {"color": pipeline_color, "width": 6},
                "value": max(min(projected_pct, 100), 0),
            },
        },
    )
)
completion_pulse_fig.update_layout(
    height=300,
    margin=dict(l=20, r=20, t=60, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
)

card_palette = [
    ("Target (Y1+Y2)", target_first_two_years, "#0EA5E9"),
    ("Completed", total_completed, "#16A34A"),
    ("In Progress", in_progress, "#F59E0B"),
    ("Projected (Complete)", projected_total, "#6366F1"),
]

st.markdown("<div style='margin-top:18px;'></div>", unsafe_allow_html=True)

card_columns = st.columns(4, gap="large")
for col, (label, value, accent) in zip(card_columns, card_palette):
    col.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, {accent}1A, rgba(15,23,42,0.02));
            border-left: 5px solid {accent};
            border-radius: 16px;
            padding: 16px 18px;
            margin-bottom: 1.1rem;
            box-shadow: 0 12px 28px rgba(15,23,42,0.12);
            color: {'#0F172A' if not is_dark else '#E2E8F0'};
        ">
            <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.18em; opacity:0.75;">{label}</div>
            <div style="font-size:1.9rem; font-weight:800;">{value:,}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.caption(f"Full NST2 target (2024–2029): {total_target:,} learners")

st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)
st.plotly_chart(completion_pulse_fig, use_container_width=True, config={"displayModeBar": False})

if target_first_two_years:
    status_message = (
        f"Needs <strong style='color:{gap_color};'>{gap_positive:,}</strong> additional learners to reach the two-year goal."
        if gap_positive > 0
        else f"On track to exceed the two-year goal by <strong style='color:#22C55E;'>{abs(gap_raw):,}</strong> learners if the pipeline completes."
    )
else:
    status_message = "Set a two-year target to activate projections."

st.markdown(
    f"""
    <div style="
        background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(59,130,246,0.08));
        border-radius: 18px;
        padding: 18px 20px;
        border: 1px solid rgba(99,102,241,0.35);
        margin-top: 0.9rem;
        margin-bottom: 1.2rem;
        color: {'#0F172A' if not is_dark else '#E2E8F0'};
        font-size: 0.95rem;
    ">
        <strong>{completed_pct:,.1f}%</strong> of the Y1–Y2 target is complete and the pipeline lifts coverage to
        <strong>{min(projected_pct, 150):,.1f}%</strong> if everyone graduates.<br />
        {status_message}
    </div>
    """,
    unsafe_allow_html=True,
)

# --- PROGRAM MOMENTUM ---
st.markdown("### Program Momentum (Share of Cumulative Completion)")

program_df = (
    pd.DataFrame(PROGRAM_DATA)
    .T.reset_index()
    .rename(columns={"index": "Program", "completed": "Completed", "enrolled": "Enrolled"})
)
program_df["Contribution %"] = (
    (program_df["Completed"] / total_completed) * 100 if total_completed else 0.0
)
program_df = program_df.sort_values("Completed", ascending=False).reset_index(drop=True)
program_df.index = program_df.index + 1

st.dataframe(
    program_df.head(15),
    use_container_width=True,
    hide_index=False,
    column_config={
        "Program": st.column_config.TextColumn("Program"),
        "Enrolled": st.column_config.NumberColumn("Enrolled"),
        "Completed": st.column_config.NumberColumn("Completed"),
        "Contribution %": st.column_config.NumberColumn("Contribution %", format="%.2f%%"),
    },
)

# # --- CAPABILITY MIX (VENN-STYLE OVERVIEW) ---
# st.markdown("### Capability Mix Snapshot")
# venn_col_left, venn_col_right = st.columns([1.1, 2], gap="large")

# with venn_col_left:
#     st.markdown(
#         "Visualizing how programs cluster across basic, intermediate, and advanced digital capability goals."
#     )
#     capability_counts = {"Basic": 6, "Intermediate": 10, "Advanced": 4, "Overlap": {"Basic-Intermediate": 4, "Intermediate-Advanced": 3, "Basic-Advanced": 0, "All": 2}}

#     fig = go.Figure()
#     fig.add_shape(type="circle", xref="x", yref="y", x0=0, y0=0, x1=2, y1=2, fillcolor="rgba(250,204,21,0.35)", line_color="rgba(250,204,21,0.8)")
#     fig.add_shape(type="circle", xref="x", yref="y", x0=1, y0=0, x1=3, y1=2, fillcolor="rgba(56,189,248,0.35)", line_color="rgba(56,189,248,0.8)")
#     fig.add_shape(type="circle", xref="x", yref="y", x0=0.5, y0=0.8, x1=2.5, y1=2.8, fillcolor="rgba(129,140,248,0.33)", line_color="rgba(99,102,241,0.8)")

#     annotations = [
#         dict(x=0.5, y=1.7, text=f"Basic<br><b>{capability_counts['Basic']}</b>", showarrow=False, font=dict(size=14, color="#713F12")),
#         dict(x=2.2, y=1.7, text=f"Intermediate<br><b>{capability_counts['Intermediate']}</b>", showarrow=False, font=dict(size=14, color="#1E40AF")),
#         dict(x=1.5, y=0.4, text=f"Advanced<br><b>{capability_counts['Advanced']}</b>", showarrow=False, font=dict(size=14, color="#312E81")),
#         dict(x=1.0, y=1.0, text=f"<b>{capability_counts['Overlap']['All']}</b>", showarrow=False, font=dict(size=16, color="#0F172A")),
#         dict(x=0.9, y=1.6, text=f"<b>{capability_counts['Overlap']['Basic-Intermediate']}</b>", showarrow=False, font=dict(size=14, color="#0F172A")),
#         dict(x=1.9, y=1.3, text=f"<b>{capability_counts['Overlap']['Intermediate-Advanced']}</b>", showarrow=False, font=dict(size=14, color="#0F172A")),
#         dict(x=1.1, y=0.8, text=f"<b>{capability_counts['Overlap']['Basic-Advanced']}</b>", showarrow=False, font=dict(size=14, color="#0F172A")),
#     ]

#     fig.update_layout(
#         showlegend=False,
#         margin=dict(l=0, r=0, t=10, b=0),
#         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.2, 3.2]),
#         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.2, 3.0]),
#         annotations=annotations,
#         height=360,
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)",
#     )

#     st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# with venn_col_right:
#     st.markdown("#### Quick Insights")
#     st.markdown(
#         """
#         - **Momentum**: Programs are collectively **{:.1f}%** toward the first two-year goal.
#         - **Pipeline**: We have **{}** learners enrolled, providing a healthy pipeline toward completions.
#         - **Capability Mix**: Majority of initiatives skew toward intermediate skills; advanced courses remain a growth area.
#         - **Targets**: Keep pace with onboarding to stay ahead of the 2025/26 uplift of **{}** learners.
#         """.format(
#             cumulative_progress_pct,
#             f"{total_enrolled:,}",
#             f"{int(target_by_year_df.loc[target_by_year_df['Year'] == '2025/26', 'Target'].iloc[0]):,}",
#         )
#     )

footer_note()
