
import streamlit as st
from string import Template

LOGO_LIGHT_SVG = """
<svg width="280" height="120" viewBox="0 0 560 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="560" height="240" rx="28" fill="#0C2F8A"/>
  <text x="40" y="128" font-family="Montserrat, 'Segoe UI', sans-serif" font-size="90" font-weight="700" textLength="480" lengthAdjust="spacingAndGlyphs">
    <tspan fill="#FFFFFF">&lt;1 Mi</tspan>
    <tspan fill="#21C4FF">//</tspan>
    <tspan fill="#FFFFFF">ion&gt;</tspan>
  </text>
  <text x="52" y="196" font-family="Montserrat, 'Segoe UI', sans-serif" font-size="52" font-weight="700" textLength="456" lengthAdjust="spacingAndGlyphs" fill="#FFFFFF">RWANDAN CODERS</text>
</svg>
""".strip()

LOGO_DARK_SVG = """
<svg width="280" height="120" viewBox="0 0 560 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="560" height="240" rx="28" fill="none"/>
  <text x="40" y="128" font-family="Montserrat, 'Segoe UI', sans-serif" font-size="90" font-weight="700" textLength="480" lengthAdjust="spacingAndGlyphs">
    <tspan fill="#E5EDFF">&lt;1 Mi</tspan>
    <tspan fill="#38BDF8">//</tspan>
    <tspan fill="#E5EDFF">ion&gt;</tspan>
  </text>
  <text x="52" y="196" font-family="Montserrat, 'Segoe UI', sans-serif" font-size="52" font-weight="700" textLength="456" lengthAdjust="spacingAndGlyphs" fill="#E5EDFF">RWANDAN CODERS</text>
</svg>
""".strip()

SIDEBAR_LINKS = [
    {"key": "main", "path": "app.py", "label": "Overview"},
    {"key": "exec_summary", "path": "pages/00_Executive_Summary.py", "label": "Executive Summary"},
    {"key": "gym_uni", "path": "pages/01_The_Gym_at_University.py", "label": "Gym @ University"},
    {"key": "gym_prep", "path": "pages/02_The_Gym_Preparatory_Training.py", "label": "Gym Prep"},
    {"key": "dot_rwanda", "path": "pages/03_DOT_Rwanda_Program.py", "label": "DOT Rwanda"},
    {"key": "techtonic", "path": "pages/04_TechTonic.py", "label": "TechTonic"},
    {"key": "get_into_tech", "path": "pages/05_Get_Into_Tech.py", "label": "Get Into Tech"},
    {"key": "risa_it", "path": "pages/06_RISA_Training_of_Public_IT_Professionals_Up_skilled_and_Re_skilled.py", "label": "RISA IT Pros"},
    {"key": "auca_outreach", "path": "pages/07_AUCA_Community_Outreach_Program.py", "label": "AUCA Outreach"},
    {"key": "digital_talent", "path": "pages/08_Digital_Talent_Program.py", "label": "Digital Talent"},
    {"key": "dl_students", "path": "pages/09_Digital_Literacy_Program_Students.py", "label": "Digital Literacy – Students"},
    {"key": "dl_teachers", "path": "pages/10_Digital_Literacy_Program_Teachers.py", "label": "Digital Literacy – Teachers"},
    {"key": "udacity", "path": "pages/11_Udacity_One_Million_Rwandan_Coders_Program.py", "label": "Udacity Coders"},
    {"key": "ingazi", "path": "pages/12_Ingazi.py", "label": "Ingazi"},
    {"key": "agcci", "path": "pages/13_African_Girls_Can_Code_Initiative.py", "label": "Girls Can Code"},
    {"key": "reb_2324", "path": "pages/14_REB_RTB_Graduates_2023_2024.py", "label": "REB/RTB 23–24"},
    {"key": "reb_2425", "path": "pages/15_REB_RTB_Graduates_2024_2025.py", "label": "REB/RTB 24–25"},
    {"key": "auca", "path": "pages/16_AUCA.py", "label": "AUCA"},
    {"key": "cops", "path": "pages/17_COP_s.py", "label": "COPs"},
]

# ---- THEME & STYLES ----
def apply_theme(mode: str = "Light"):
    """
    Injects CSS variables for Light or Dark modes and base styling.
    """
    is_dark = (mode.lower() == "dark")
    bg = "#0B1020" if is_dark else "#EEF2FF"
    surface = "#151A28" if is_dark else "#FFFFFF"
    surface_alt = "#1D2334" if is_dark else "#F8FAFF"
    text = "#F8FAFC" if is_dark else "#111827"
    subtext = "#9CA3AF" if is_dark else "#4B5563"
    border = "#27324A" if is_dark else "#E2E8F0"
    accent = "#60A5FA" if is_dark else "#4F46E5"
    accent_soft = "rgba(96,165,250,0.35)" if is_dark else "rgba(79,70,229,0.25)"
    card_text = "#FFFFFF"
    grad_enrolled = (
        "linear-gradient(135deg, rgba(79,70,229,0.95) 0%, rgba(14,165,233,0.92) 55%, rgba(56,189,248,0.85) 100%)"
        if is_dark else
        "linear-gradient(135deg, rgba(79,70,229,1) 0%, rgba(14,165,233,0.95) 52%, rgba(45,212,191,0.92) 100%)"
    )
    grad_completed = (
        "linear-gradient(135deg, rgba(34,197,94,0.95) 0%, rgba(22,163,74,0.95) 55%, rgba(132,204,22,0.85) 100%)"
        if is_dark else
        "linear-gradient(135deg, rgba(22,163,74,1) 0%, rgba(34,197,94,0.95) 55%, rgba(74,222,128,0.9) 100%)"
    )
    sidebar_bg = (
        "linear-gradient(180deg, rgba(15,23,42,0.9), rgba(15,23,42,0.6))"
        if is_dark else
        "linear-gradient(180deg, rgba(255,255,255,0.96), rgba(239,246,255,0.92))"
    )
    css = Template("""
    <style>
    :root {
        --bg: $bg;
        --surface: $surface;
        --surface-alt: $surface_alt;
        --text: $text;
        --subtext: $subtext;
        --border: $border;
        --accent: $accent;
        --accent-soft: $accent_soft;
        --card-text: $card_text;
        --grad-enrolled: $grad_enrolled;
        --grad-completed: $grad_completed;
        --sidebar-bg: $sidebar_bg;
    }
    /* App background + text */
    .stApp {
        background: radial-gradient(circle at top, rgba(96,165,250,0.18), transparent 55%),
                     radial-gradient(circle at 15% 65%, rgba(79,70,229,0.12), transparent 55%),
                     var(--bg) !important;
        color: var(--text) !important;
    }
    section.main {
        background: transparent !important;
    }
    .stApp header {
        backdrop-filter: blur(18px);
    }
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1080px;
    }
    /* Headings, captions & structural text */
    h1, h2, h3, h4, h5, h6, p, li, span, div, label {
        color: var(--text) !important;
    }
    .stCaption, .stMarkdown small {
        color: var(--subtext) !important;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border);
        backdrop-filter: blur(18px);
    }
    section[data-testid="stSidebar"] *, section[data-testid="stSidebar"] p {
        color: var(--text) !important;
    }
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
    /* Sidebar radio pills */
    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: transparent !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: var(--accent) !important;
        border-color: var(--accent) !important;
        color: #FFFFFF !important;
    }
    /* Inputs */
    input, textarea, select, .stTextInput > div > div > input, .stNumberInput input, .stTextArea textarea {
        background-color: var(--surface) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
    }
    /* Expander */
    details, .stExpander {
        background: var(--surface-alt) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 12px 16px;
        box-shadow: 0 14px 35px rgba(15,23,42,0.15);
    }
    .stExpander div[role="button"] p {
        color: var(--text) !important;
    }
    .sidebar-section-title {
        font-size: 0.85rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--subtext);
        margin: 1.25rem 0 0.75rem;
    }
    .sidebar-nav {
        display: grid;
        gap: 0.45rem;
    }
    .sidebar-nav div[data-testid^="stPageLink"] > a {
        display: block;
        padding: 0.6rem 0.85rem;
        border-radius: 12px;
        border: 1px solid var(--border);
        background: var(--surface);
        color: var(--text);
        font-weight: 600;
        text-decoration: none;
        font-size: 0.95rem;
        transition: transform 150ms ease, box-shadow 180ms ease, border-color 180ms ease, background 180ms ease;
        box-shadow: 0 8px 18px rgba(15,23,42,0.12);
    }
    .sidebar-nav div[data-testid^="stPageLink"] > a:hover {
        transform: translateY(-2px);
        border-color: var(--accent);
        box-shadow: 0 16px 28px rgba(15,23,42,0.22);
    }
    .sidebar-nav div[data-testid^="stPageLink"][aria-current="page"] > a,
    .sidebar-nav div[data-testid^="stPageLink"][aria-disabled="true"] > a {
        background: var(--accent);
        color: #FFFFFF;
        border-color: transparent;
        box-shadow: 0 18px 32px rgba(99,102,241,0.35);
        transform: translateY(-2px);
        cursor: default;
    }
    /* Header layout helpers */
    .dashboard-logo svg {
        width: 220px;
        max-width: 100%;
        height: auto;
        display: block;
    }
    .dashboard-title {
        margin-bottom: 0.25rem;
        font-size: clamp(2.1rem, 2.8vw, 2.8rem);
        font-weight: 800;
    }
    /* Fancy metric cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(320px, 1fr));
        gap: 1.75rem;
        margin: 0;
        justify-content: center;
        justify-items: center;
    }
    .metrics-wrapper {
        display: flex;
        justify-content: center;
        margin: clamp(5rem, 14vh, 11rem) auto;
        max-width: 820px;
        padding: 0 1rem;
    }
    .metric-card {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        gap: 0.85rem;
        width: min(100%, 360px);
        border-radius: 18px;
        padding: 36px 32px 32px 32px;
        min-height: 200px;
        border: 1px solid var(--accent-soft);
        box-shadow: 0 20px 40px rgba(15,23,42,0.18), 0 4px 12px rgba(15,23,42,0.12);
        overflow: hidden;
        transition: transform 240ms ease, box-shadow 240ms ease, filter 220ms ease;
        cursor: pointer;
        isolation: isolate;
        backdrop-filter: saturate(120%);
    }
    .metric-card:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 30px 55px rgba(15,23,42,0.35);
        filter: saturate(1.05);
    }
    .metric-label {
        font-size: 1.05rem;
        font-weight: 600;
        letter-spacing: 1.6px;
        text-transform: uppercase;
        color: var(--card-text);
        opacity: 0.82;
    }
    .metric-value {
        font-size: clamp(3rem, 5vw, 3.4rem);
        font-weight: 900;
        line-height: 1.05;
        color: var(--card-text);
    }
    .metric-card .metric-subtext {
        font-size: 0.95rem;
        color: rgba(255,255,255,0.82);
    }
    .gloss {
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at top right, rgba(255,255,255,0.35), transparent 55%);
        opacity: 0.75;
        pointer-events: none;
        z-index: -1;
    }
    /* Card gradient presets */
    .grad-enrolled {
        background: var(--grad-enrolled);
    }
    .grad-completed {
        background: var(--grad-completed);
    }
    @media (max-width: 1080px) {
        .metric-grid {
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        }
    }
    @media (max-width: 768px) {
        .dashboard-logo svg {
            width: 180px;
        }
        .block-container {
            padding-top: 1.75rem;
        }
        .metrics-wrapper {
            margin: 4rem auto 4.5rem auto;
        }
        .metric-card {
            min-height: 180px;
            padding: 28px 24px;
        }
    }
    </style>
    """).substitute(
        bg=bg,
        surface=surface,
        surface_alt=surface_alt,
        text=text,
        subtext=subtext,
        border=border,
        accent=accent,
        accent_soft=accent_soft,
        card_text=card_text,
        grad_enrolled=grad_enrolled,
        grad_completed=grad_completed,
        sidebar_bg=sidebar_bg,
    )
    st.markdown(css, unsafe_allow_html=True)

def render_header(title: str, mode: str = "Light", subtitle: str | None = None):
    is_dark = (mode.lower() == "dark")
    logo_svg = LOGO_DARK_SVG if is_dark else LOGO_LIGHT_SVG
    logo_col, text_col = st.columns([2, 5])
    with logo_col:
        st.markdown(f'<div class="dashboard-logo">{logo_svg}</div>', unsafe_allow_html=True)
    with text_col:
        st.markdown(f'<h1 class="dashboard-title">{title}</h1>', unsafe_allow_html=True)
        if subtitle:
            st.caption(subtitle)

def render_two_cards(enrolled: int, completed: int, col1_label: str="Enrolled", col2_label: str="Completed / Expected"):
    st.markdown(
        f"""
        <div class="metrics-wrapper">
            <div class="metric-grid">
                <div class="metric-card grad-enrolled">
                    <div class="metric-label">{col1_label}</div>
                    <div class="metric-value">{enrolled:,}</div>
                    <div class="gloss"></div>
                </div>
                <div class="metric-card grad-completed">
                    <div class="metric-label">{col2_label}</div>
                    <div class="metric-value">{completed:,}</div>
                    <div class="gloss"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_note():
    st.write("---")

def render_sidebar_nav(active_key: str):
    st.sidebar.markdown('<div class="sidebar-section-title">Navigate</div>', unsafe_allow_html=True)
    nav_container = st.sidebar.container()
    with nav_container:
        st.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
        for item in SIDEBAR_LINKS:
            disabled = (item["key"] == active_key)
            st.page_link(item["path"], label=item["label"], disabled=disabled)
        st.markdown('</div>', unsafe_allow_html=True)
