import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Final Revenue Audit")

# 1. CACHE LOADING (Saves your 4GB RAM)
@st.cache_data
def load_data():
    return pd.read_csv("revenue_leakage_final.csv")

try:
    df = load_data()
    df["billing_month"] = pd.to_datetime(df["billing_month"])

    st.title("💰 Revenue Leakage Recovery Dashboard")
    st.markdown(f"**Data Audit Date:** {df['billing_month'].max().strftime('%B %Y')}")

    # ---------------------
    # 2. KPI SECTION (Mapped to your CSV)
    # ---------------------
    total_logged = df["revenue_logged"].sum()
    total_leakage = df["revenue_leakage"].sum()
    leakage_pct = (total_leakage / total_logged) * 100 if total_logged > 0 else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Revenue Logged", f"${total_logged:,.0f}")
    c2.metric("Total Leakage", f"${total_leakage:,.0f}", delta_color="inverse")
    c3.metric("Leakage Rate", f"{leakage_pct:.2f}%")

    st.markdown("---")

    # ---------------------
    # 3. ANALYSIS (Mapped to 'client_name_logged')
    # ---------------------
    left, right = st.columns(2)

    with left:
        # Grouping by the correct column in your CSV
        client_data = df.groupby("client_name_logged")["revenue_leakage"].sum().reset_index()
        fig_client = px.bar(client_data, x="client_name_logged", y="revenue_leakage", 
                            title="Revenue Leakage by Client", color="revenue_leakage")
        st.plotly_chart(fig_client, use_container_width=True)

    with right:
        # Grouping by the correct column in your CSV
        aging_data = df.groupby("aging_bucket")["revenue_leakage"].sum().reset_index()
        fig_aging = px.pie(aging_data, names="aging_bucket", values="revenue_leakage", 
                           title="Leakage Aging (Urgency)")
        st.plotly_chart(fig_aging, use_container_width=True)

    # ---------------------
    # 4. EXCEPTION TABLE
    # ---------------------
    st.subheader("🔍 Priority Audit Exceptions")
    st.dataframe(df[df["revenue_leakage"] > 0].sort_values("revenue_leakage", ascending=False).head(15))

except Exception as e:
    st.error(f"Logic Error: {e}")
