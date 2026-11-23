import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

LOGO_PATH = Path(__file__).parent / 'assets' / 'datamind_logo.png'

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="DataMind | Analytics Workspace",
    page_icon=str(LOGO_PATH),
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# THEME & STYLING
# =========================================================
if "datamind_theme" not in st.session_state:
    st.session_state["datamind_theme"] = "Dark"

# This control is deliberately placed before the CSS so every component
# receives the selected palette on the same Streamlit rerun.
st.sidebar.markdown("### Appearance")
st.sidebar.radio(
    "Choose theme",
    ["Dark", "Light"],
    key="datamind_theme",
    horizontal=True,
    label_visibility="collapsed",
)

if st.session_state["datamind_theme"] == "Light":
    BG, PANEL, PANEL_ALT = "#F4F6FB", "#FFFFFF", "#EEF1F8"
    BORDER, TEXT, MUTED = "#DCE2EE", "#182238", "#65728A"
    ACCENT, ACCENT_DARK, SUCCESS = "#7157D9", "#5D45C5", "#16865B"
    SIDEBAR_BG = "#EBEFF7"
    HEADER_BG = "rgba(244, 246, 251, 0.94)"
    HERO_BG = "linear-gradient(115deg, #E8EAFE 0%, #F0EAFE 58%, #F6EEFF 100%)"
    HERO_TITLE = "#202642"
    HERO_COPY = "#5F6880"
else:
    BG, PANEL, PANEL_ALT = "#0B1020", "#11182B", "#151E34"
    BORDER, TEXT, MUTED = "#26324B", "#F4F6FC", "#9AA8C0"
    ACCENT, ACCENT_DARK, SUCCESS = "#9B8AFB", "#7666DB", "#65D6A5"
    SIDEBAR_BG = "#0E1527"
    HEADER_BG = "rgba(11, 16, 32, 0.92)"
    HERO_BG = "linear-gradient(115deg, #1A2340 0%, #211E42 58%, #29234C 100%)"
    HERO_TITLE = "#FFFFFF"
    HERO_COPY = "#C0C5DA"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

    :root {{
        --bg: {BG};
        --panel: {PANEL};
        --panel-alt: {PANEL_ALT};
        --border: {BORDER};
        --text: {TEXT};
        --muted: {MUTED};
        --accent: {ACCENT};
    }}

    html, body, [class*="css"] {{
        font-family: 'DM Sans', sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(ellipse at 80% 0%, rgba(112, 93, 205, 0.12), transparent 34%),
            var(--bg);
        color: var(--text);
    }}

    [data-testid="stHeader"] {{
        background: {HEADER_BG};
    }}

    [data-testid="stSidebar"] {{
        background: {SIDEBAR_BG};
        border-right: 1px solid var(--border);
    }}

    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 1.2rem;
    }}

    /* Keep the brand mark legible in both dark and light themes. */
    [data-testid="stImage"] img {{
        border-radius: 12px;
    }}

    .block-container {{
        max-width: 1440px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3, h4 {{
        color: var(--text) !important;
        letter-spacing: -0.035em;
    }}

    p, label, .stCaption {{
        color: var(--muted);
    }}

    [data-testid="stMarkdownContainer"] p {{
        line-height: 1.6;
    }}

    .brand {{
        color: var(--text);
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: -0.07em;
        margin-bottom: 0.15rem;
    }}

    .brand span {{
        color: var(--accent);
    }}

    .brand-row {{
        display: flex;
        align-items: center;
        gap: 0.65rem;
        margin-bottom: 0.2rem;
    }}

    .brand-mark {{
        width: 38px;
        height: 38px;
        border-radius: 12px;
        display: grid;
        place-items: center;
        background: linear-gradient(145deg, {ACCENT_DARK}, {ACCENT});
        box-shadow: 0 5px 18px rgba(118, 102, 219, 0.25);
        flex: 0 0 auto;
    }}

    .brand-caption {{
        color: var(--muted);
        font-size: 0.78rem;
        letter-spacing: 0.02em;
    }}

    .topline {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.35rem;
    }}

    .eyebrow {{
        color: var(--accent);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }}

    .page-title {{
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        color: var(--text);
        margin: 0;
    }}

    .page-subtitle {{
        color: var(--muted);
        font-size: 0.94rem;
        margin-top: 0.45rem;
    }}

    .hero {{
        background: {HERO_BG};
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1.65rem 1.8rem;
        margin: 1.5rem 0 1.5rem 0;
        box-shadow: 0 14px 38px rgba(0, 0, 0, 0.14);
    }}

    .hero-kicker {{
        color: {ACCENT};
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.13em;
        font-weight: 700;
        margin-bottom: 0.6rem;
    }}

    .hero-title {{
        color: {HERO_TITLE};
        font-size: 1.55rem;
        font-weight: 750;
        letter-spacing: -0.045em;
        margin-bottom: 0.4rem;
    }}

    .hero-copy {{
        color: {HERO_COPY};
        font-size: 0.9rem;
        max-width: 720px;
        margin: 0;
    }}

    .section-head {{
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        margin: 1.7rem 0 0.8rem 0;
    }}

    .section-title {{
        color: var(--text);
        font-size: 1.08rem;
        font-weight: 700;
        letter-spacing: -0.025em;
    }}

    .section-note {{
        color: var(--muted);
        font-size: 0.78rem;
    }}

    .metric-card {{
        background: linear-gradient(145deg, var(--panel), #121B30);
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 1.05rem 1.15rem;
        min-height: 116px;
    }}

    .metric-top {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 600;
    }}

    .metric-icon {{
        color: var(--accent);
        font-size: 1rem;
    }}

    .metric-number {{
        color: var(--text);
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        margin-top: 0.55rem;
    }}

    .metric-foot {{
        color: #7888A5;
        font-size: 0.72rem;
        margin-top: 0.1rem;
    }}

    .surface {{
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 1.1rem 1.2rem;
    }}

    .feature-card {{
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 1.25rem;
        min-height: 150px;
    }}

    .feature-icon {{
        color: var(--accent);
        font-size: 1.35rem;
        margin-bottom: 0.75rem;
    }}

    .feature-title {{
        color: var(--text);
        font-size: 0.95rem;
        font-weight: 700;
    }}

    .feature-copy {{
        color: var(--muted);
        font-size: 0.81rem;
        line-height: 1.55;
        margin-top: 0.4rem;
    }}

    .status-pill {{
        display: inline-block;
        background: rgba(101, 214, 165, 0.10);
        border: 1px solid rgba(101, 214, 165, 0.25);
        color: {SUCCESS};
        border-radius: 999px;
        padding: 0.28rem 0.65rem;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }}

    .coming-pill {{
        display: inline-block;
        background: rgba(155, 138, 251, 0.12);
        border: 1px solid rgba(155, 138, 251, 0.3);
        color: #C5BAFF;
        border-radius: 999px;
        padding: 0.28rem 0.65rem;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }}

    .empty-state {{
        background: linear-gradient(145deg, var(--panel), #131B30);
        border: 1px dashed #394765;
        border-radius: 17px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
    }}

    .empty-icon {{
        font-size: 2rem;
        margin-bottom: 0.6rem;
    }}

    .empty-title {{
        color: var(--text);
        font-size: 1.05rem;
        font-weight: 700;
    }}

    .empty-copy {{
        color: var(--muted);
        font-size: 0.84rem;
        margin-top: 0.4rem;
    }}

    .stButton button {{
        background: linear-gradient(135deg, {ACCENT_DARK}, {ACCENT});
        color: white;
        border: 0;
        border-radius: 10px;
        font-weight: 700;
        min-height: 2.65rem;
    }}

    .stButton button:hover {{
        border: 0;
        color: white;
        filter: brightness(1.08);
    }}

    [data-testid="stFileUploader"] {{
        background: rgba(21, 30, 52, 0.55);
        border: 1px dashed #394765;
        border-radius: 12px;
        padding: 0.45rem;
    }}

    [data-testid="stDataFrame"] {{
        border: 1px solid var(--border);
        border-radius: 12px;
        overflow: hidden;
    }}

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {{
        background: #151E34;
        border-color: #34415D;
        border-radius: 10px;
    }}

    .stTextInput input {{
        color: var(--text);
    }}

    hr {{
        border-color: var(--border);
    }}

    /* Theme-aware surfaces and controls */
    .metric-card, .feature-card, .surface {{
        background: var(--panel);
        border-color: var(--border);
    }}
    .stApp, [data-testid="stSidebar"] {{ color: var(--text); }}
    [data-testid="stFileUploader"], div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {{
        background: var(--panel-alt);
        border-color: var(--border);
    }}
    [data-testid="stDataFrame"] {{ border-color: var(--border); }}
    footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HELPERS
# =========================================================
def section_heading(title: str, note: str = ""):
    icon_map = {
        "Get started": "✦", "Dataset at a glance": "▦", "Data preview": "▤",
        "Column profile": "☷", "Dataset summary": "▦", "Numerical analysis": "∑",
        "Category analysis": "◫", "Full dataset": "▤", "Data quality overview": "✓",
        "Missing value treatment": "✧", "Cleaned dataset preview": "✓",
        "Descriptive statistics": "∑", "Correlation analysis": "⌁",
        "Outlier detection": "⚑", "Export your work": "⇩", "Key statistics": "∑",
        "Planned capabilities": "✦",
    }
    icon = icon_map.get(title, "•")
    note_html = f'<div class="section-note">{note}</div>' if note else ""
    st.markdown(
        f'<div class="section-head"><div class="section-title"><span style="color:var(--accent);margin-right:.55rem;">{icon}</span>{title}</div>{note_html}</div>',
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, icon: str, foot: str = ""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-top"><span>{label}</span><span class="metric-icon">{icon}</span></div>
            <div class="metric-number">{value}</div>
            <div class="metric-foot">{foot}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_safe_dataframe(frame: pd.DataFrame, **kwargs):
    """Keep numeric columns numeric; normalize mixed/object columns for Arrow display."""
    safe = frame.copy()
    for col in safe.columns:
        if pd.api.types.is_object_dtype(safe[col]) or isinstance(safe[col].dtype, pd.StringDtype):
            safe[col] = safe[col].map(
                lambda value: "—" if pd.isna(value) else str(value)
            ).astype(str)
    st.dataframe(safe, **kwargs)


def empty_state(title: str, copy: str, icon: str = "📂"):
    st.markdown(
        f"""
        <div class="empty-state">
            <div class="empty-icon">{icon}</div>
            <div class="empty-title">{title}</div>
            <div class="empty-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def chart_layout(fig):
    fig.update_layout(
        paper_bgcolor=PANEL,
        plot_bgcolor=PANEL,
        font=dict(family="DM Sans, sans-serif", color=TEXT, size=12),
        title=dict(font=dict(size=15, color=TEXT), x=0.02, xanchor="left"),
        margin=dict(l=18, r=18, t=55, b=18),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor=BORDER,
            tickfont=dict(color=MUTED),
            title_font=dict(color=MUTED),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=BORDER,
            zeroline=False,
            linecolor=BORDER,
            tickfont=dict(color=MUTED),
            title_font=dict(color=MUTED),
        ),
    )
    return fig


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.image(str(LOGO_PATH), use_container_width=True)
    st.caption("INTERACTIVE DATA ANALYTICS")
    st.divider()

    st.markdown("##### WORKSPACE")
    navigation = {
        "⌂  Overview": "Overview",
        "▥  Data Explorer": "Data Explorer",
        "✧  Data Cleaning": "Data Cleaning",
        "⌁  Advanced Analytics": "Advanced Analytics",
        "⇩  Export Results": "Export Results",
        "✦  AI Analyst": "AI Analyst",
    }
    selected_navigation = st.radio(
        "Navigation",
        list(navigation.keys()),
        label_visibility="collapsed",
    )
    page = navigation[selected_navigation]

    st.divider()
    st.markdown("##### YOUR DATA")
    uploaded_file = st.file_uploader(
        "＋  Import a dataset",
        type=["csv"],
        help="Upload a CSV file to explore it in DataMind.",
    )

    if uploaded_file is not None:
        try:
            uploaded_file.seek(0)
            loaded_df = pd.read_csv(uploaded_file)
            if st.session_state.get("filename") != uploaded_file.name:
                st.session_state.pop("cleaned_dataset", None)
            st.session_state["dataset"] = loaded_df
            st.session_state["filename"] = uploaded_file.name
        except Exception as error:
            st.error(f"Could not read this CSV: {error}")

    df = st.session_state.get("dataset")

    if df is not None:
        st.markdown(
            f'<div class="status-pill">● DATASET CONNECTED</div>',
            unsafe_allow_html=True,
        )
        st.caption(st.session_state.get("filename", "Uploaded dataset"))
        if st.button("✕  Remove dataset", use_container_width=True):
            st.session_state.pop("dataset", None)
            st.session_state.pop("filename", None)
            st.session_state.pop("cleaned_dataset", None)
            st.rerun()
    else:
        st.caption("CSV files supported")

    st.divider()
    st.markdown("**DataMind**")
    st.caption("Explore data. Find patterns. Build clarity.")

# =========================================================
# MAIN HEADER
# =========================================================
header_titles = {
    "Overview": ("OVERVIEW", "Your analytics workspace", "A clear view of your data, all in one place."),
    "Data Explorer": ("DATA TOOLS", "Explore your data", "Understand distributions, categories, and underlying patterns."),
    "Data Cleaning": ("DATA QUALITY", "Clean your data", "Handle missing values and duplicate records."),
    "Advanced Analytics": ("DEEPER INSIGHTS", "Advanced analytics", "Explore correlations, outliers, and descriptive statistics."),
    "Export Results": ("YOUR OUTPUTS", "Export results", "Download your cleaned dataset and analysis summaries."),
    "Data Cleaning": ("DATA QUALITY", "Clean your data", "Handle missing values and duplicate records."),
    "Advanced Analytics": ("DEEPER INSIGHTS", "Advanced analytics", "Explore correlations, outliers, and descriptive statistics."),
    "Export Results": ("YOUR OUTPUTS", "Export results", "Download your cleaned dataset and analysis summaries."),
    "AI Analyst": ("INTELLIGENCE", "AI Analyst", "A conversational data assistant is on the roadmap."),
}
eyebrow, title, subtitle = header_titles[page]
logo_col, heading_col = st.columns([1.15, 3.85], vertical_alignment="center")
with logo_col:
    st.image(str(LOGO_PATH), use_container_width=True)
with heading_col:
    st.markdown(
        f"""
        <div class="eyebrow">{eyebrow}</div>
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# OVERVIEW
# =========================================================
if page == "Overview":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">YOUR DATA, IN FOCUS</div>
            <div class="hero-title">Make better sense of your data.</div>
            <p class="hero-copy">
                Bring your dataset into one workspace, inspect its quality, and
                explore the patterns that matter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if df is None:
        section_heading("Get started", "Three simple steps")
        cols = st.columns(3)
        cards = [
            ("↥", "Import a dataset", "Upload a CSV file using the panel on the left."),
            ("▦", "Explore the details", "Review records, columns, missing values, and duplicates."),
            ("⌁", "Find patterns", "Use Data Explorer to visualize numeric and categorical data."),
        ]
        for col, (icon, heading, copy) in zip(cols, cards):
            with col:
                st.markdown(
                    f"""
                    <div class="feature-card">
                        <div class="feature-icon">{icon}</div>
                        <div class="feature-title">{heading}</div>
                        <div class="feature-copy">{copy}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        empty_state("Your workspace is ready", "Upload a CSV dataset from the sidebar to begin.", "📊")

    else:
        rows, columns = df.shape
        missing = int(df.isna().sum().sum())
        duplicates = int(df.duplicated().sum())
        filename = st.session_state.get("filename", "Uploaded dataset")

        section_heading("Dataset at a glance", filename)
        metric_cols = st.columns(4)
        metrics = [
            ("Total records", f"{rows:,}", "▤", "Rows in your dataset"),
            ("Total columns", f"{columns:,}", "▦", "Available variables"),
            ("Missing values", f"{missing:,}", "◌", "Empty cells detected"),
            ("Duplicate rows", f"{duplicates:,}", "⧉", "Repeated records"),
        ]
        for col, metric in zip(metric_cols, metrics):
            with col:
                metric_card(*metric)

        section_heading("Data preview", "First 10 records")
        display_safe_dataframe(df.head(10), use_container_width=True, hide_index=True)

        section_heading("Column profile", "Structure and completeness")
        quality = pd.DataFrame({
            "Column": df.columns.astype(str),
            "Data type": [str(dtype) for dtype in df.dtypes],
            "Missing": df.isna().sum().values,
            "Unique values": df.nunique(dropna=True).values,
            "Completeness": [
                f"{(1 - df[col].isna().mean()) * 100:.1f}%"
                for col in df.columns
            ],
        })
        display_safe_dataframe(quality, use_container_width=True, hide_index=True)

# =========================================================
# DATA EXPLORER
# =========================================================
elif page == "Data Explorer":
    if df is None:
        empty_state("No dataset loaded", "Upload a CSV file from the sidebar to start exploring.", "📈")
    else:
        numeric = df.select_dtypes(include="number").columns.tolist()
        categorical = [
            col for col in df.columns
            if col not in numeric and df[col].nunique(dropna=True) > 0
        ]

        section_heading("Dataset summary", st.session_state.get("filename", "Uploaded dataset"))
        c1, c2, c3 = st.columns(3)
        with c1:
            metric_card("Numeric columns", f"{len(numeric)}", "∑", "Suitable for distributions")
        with c2:
            metric_card("Categorical columns", f"{len(categorical)}", "◫", "Suitable for category counts")
        with c3:
            metric_card("Total records", f"{len(df):,}", "▤", "Rows available to explore")

        if numeric:
            section_heading("Numerical analysis", "Inspect the distribution of a numeric variable")
            selected = st.selectbox("Select a numerical column", numeric, key="numeric_column")
            left, right = st.columns([1.65, 1])
            with left:
                fig = px.histogram(
                    df,
                    x=selected,
                    nbins=30,
                    title=f"Distribution of {selected}",
                    template="plotly_white" if st.session_state["datamind_theme"] == "Light" else "plotly_dark",
                    color_discrete_sequence=[ACCENT],
                )
                fig.update_traces(marker_line_width=0)
                st.plotly_chart(chart_layout(fig), use_container_width=True)
            with right:
                series = df[selected].dropna()
                stats = pd.DataFrame({
                    "Statistic": ["Count", "Mean", "Median", "Std. deviation", "Minimum", "Maximum"],
                    "Value": [
                        f"{series.count():,}",
                        f"{series.mean():,.3f}" if len(series) else "—",
                        f"{series.median():,.3f}" if len(series) else "—",
                        f"{series.std():,.3f}" if len(series) > 1 else "—",
                        f"{series.min():,.3f}" if len(series) else "—",
                        f"{series.max():,.3f}" if len(series) else "—",
                    ],
                })
                section_heading("Key statistics")
                display_safe_dataframe(stats, use_container_width=True, hide_index=True)

        if categorical:
            section_heading("Category analysis", "Compare the most frequent values")
            selected_category = st.selectbox(
                "Select a categorical column",
                categorical,
                key="categorical_column",
            )
            counts = (
                df[selected_category]
                .fillna("Missing")
                .astype(str)
                .value_counts()
                .head(10)
                .rename_axis(selected_category)
                .reset_index(name="Records")
            )
            fig = px.bar(
                counts.sort_values("Records"),
                x="Records",
                y=selected_category,
                orientation="h",
                title=f"Top values in {selected_category}",
                template="plotly_white" if st.session_state["datamind_theme"] == "Light" else "plotly_dark",
                color_discrete_sequence=[ACCENT],
            )
            st.plotly_chart(chart_layout(fig), use_container_width=True)

        if not numeric and not categorical:
            st.info("No columns are currently available for visualization.")

        section_heading("Full dataset", f"{len(df):,} rows")
        display_safe_dataframe(df, use_container_width=True, hide_index=True)

# =========================================================
# AI ANALYST — COMING SOON
# =========================================================
elif page == "Data Cleaning":
    if df is None:
        empty_state("No dataset loaded", "Upload a CSV file from the sidebar to clean your data.", "🧹")
    else:
        section_heading("Data quality overview", "Review issues before applying changes")
        missing_by_column = df.isna().sum()
        missing_total = int(missing_by_column.sum())
        duplicate_total = int(df.duplicated().sum())
        a, b, c = st.columns(3)
        with a:
            metric_card("Missing cells", f"{missing_total:,}", "◌", "Across all columns")
        with b:
            metric_card("Duplicate rows", f"{duplicate_total:,}", "⧉", "Exact repeated records")
        with c:
            metric_card("Complete rows", f"{int((~df.isna().any(axis=1)).sum()):,}", "✓", "Rows with no missing cells")

        section_heading("Missing value treatment")
        strategy = st.selectbox(
            "Choose how to handle missing values",
            ["Leave unchanged", "Drop rows with missing values", "Fill numeric with mean and text with mode"],
        )
        remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
        st.caption("Changes are applied to the in-memory dataset only. Your original CSV file is not overwritten.")

        if st.button("✧  Apply cleaning", use_container_width=True):
            cleaned = df.copy()
            if strategy == "Drop rows with missing values":
                cleaned = cleaned.dropna()
            elif strategy == "Fill numeric with mean and text with mode":
                for col in cleaned.columns:
                    if cleaned[col].isna().any():
                        if pd.api.types.is_numeric_dtype(cleaned[col]):
                            mean_value = cleaned[col].mean()
                            if pd.notna(mean_value):
                                cleaned[col] = cleaned[col].fillna(mean_value)
                        else:
                            modes = cleaned[col].mode(dropna=True)
                            if not modes.empty:
                                cleaned[col] = cleaned[col].fillna(modes.iloc[0])
            if remove_duplicates:
                cleaned = cleaned.drop_duplicates()
            st.session_state["cleaned_dataset"] = cleaned
            st.success(f"Cleaning complete. {len(df) - len(cleaned):,} rows removed; {int(cleaned.isna().sum().sum()):,} missing cells remain.")
            st.rerun()

        cleaned_df = st.session_state.get("cleaned_dataset")
        if cleaned_df is not None:
            section_heading("Cleaned dataset preview", f"{len(cleaned_df):,} rows × {cleaned_df.shape[1]:,} columns")
            display_safe_dataframe(cleaned_df.head(10), use_container_width=True, hide_index=True)

# =========================================================
# ADVANCED ANALYTICS
# =========================================================
elif page == "Advanced Analytics":
    if df is None:
        empty_state("No dataset loaded", "Upload a CSV file from the sidebar to analyze it.", "📉")
    else:
        analysis_df = st.session_state.get("cleaned_dataset", df)
        section_heading("Descriptive statistics", "Numeric columns")
        numeric_cols = analysis_df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            display_safe_dataframe(analysis_df[numeric_cols].describe().T.reset_index().rename(columns={"index": "Column"}), use_container_width=True, hide_index=True)
            section_heading("Correlation analysis", "Relationships between numeric variables")
            if len(numeric_cols) >= 2:
                corr = analysis_df[numeric_cols].corr(numeric_only=True)
                fig = px.imshow(
                    corr,
                    text_auto=".2f",
                    aspect="auto",
                    color_continuous_scale="Purples",
                    title="Numeric feature correlation",
                )
                st.plotly_chart(chart_layout(fig), use_container_width=True)
            else:
                st.info("At least two numeric columns are needed to calculate correlations.")

            section_heading("Outlier detection", "IQR method · values outside 1.5× the interquartile range")
            outlier_rows = []
            for col in numeric_cols:
                series = analysis_df[col].dropna()
                if series.empty:
                    count = 0
                else:
                    q1, q3 = series.quantile([0.25, 0.75])
                    iqr = q3 - q1
                    count = int(((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum())
                outlier_rows.append({"Column": col, "Outlier values": count})
            display_safe_dataframe(pd.DataFrame(outlier_rows), use_container_width=True, hide_index=True)
        else:
            st.info("This dataset has no numeric columns for statistical analysis.")

# =========================================================
# EXPORT RESULTS
# =========================================================
elif page == "Export Results":
    if df is None:
        empty_state("No dataset loaded", "Upload a CSV file before exporting results.", "⇩")
    else:
        export_df = st.session_state.get("cleaned_dataset", df)
        section_heading("Export your work", "Download files generated from the current dataset")
        st.markdown(
            f'<div class="status-pill">● READY TO EXPORT</div> &nbsp; '
            f'<span style="color:{MUTED};font-size:0.82rem;">{len(export_df):,} rows · {export_df.shape[1]:,} columns</span>',
            unsafe_allow_html=True,
        )
        st.markdown("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Cleaned dataset**")
            st.caption("CSV file containing the current cleaned dataset. If you have not cleaned it, this exports the uploaded data.")
            st.download_button(
                "⇩  Download dataset (CSV)",
                data=export_df.to_csv(index=False).encode("utf-8"),
                file_name="datamind_cleaned_dataset.csv",
                mime="text/csv",
                use_container_width=True,
            )
        with col2:
            st.markdown("**Analysis summary**")
            st.caption("Descriptive statistics for all numeric columns.")
            numeric_export = export_df.select_dtypes(include="number")
            summary = numeric_export.describe().T.reset_index().rename(columns={"index": "Column"})
            st.download_button(
                "⇩  Download summary (CSV)",
                data=summary.to_csv(index=False).encode("utf-8"),
                file_name="datamind_analysis_summary.csv",
                mime="text/csv",
                use_container_width=True,
                disabled=numeric_export.empty,
            )
        if numeric_export.empty:
            st.info("No numeric columns are available for a statistical summary export.")

elif page == "AI Analyst":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">COMING SOON</div>
            <div class="hero-title">Ask questions. Discover what matters.</div>
            <p class="hero-copy">
                The AI Analyst is planned to help you explore datasets using
                natural language and turn questions into useful analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if df is not None:
        st.markdown(
            f'<div class="status-pill">● DATASET CONNECTED</div> &nbsp; '
            f'<span style="color:{MUTED};font-size:0.82rem;">{st.session_state.get("filename", "Dataset")}</span>',
            unsafe_allow_html=True,
        )

    section_heading("Planned capabilities")
    feature_cols = st.columns(3)
    planned = [
        ("✦", "Ask in plain English", "Ask questions about your data without writing code."),
        ("⌘", "Automated analysis", "Generate relevant summaries, calculations, and comparisons."),
        ("▥", "Insight generation", "Surface trends and visual explanations from your dataset."),
    ]
    for col, (icon, heading, copy) in zip(feature_cols, planned):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{heading}</div>
                    <div class="feature-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("")
    st.info("The AI engine is not connected yet. This section is a preview of planned functionality.")

# =========================================================
# FOOTER
# =========================================================
st.divider()
left, right = st.columns([3, 1])
with left:
    st.caption("DATAMIND  /  DATA ANALYTICS WORKSPACE")
with right:
    st.caption("Prototype · 2026")
