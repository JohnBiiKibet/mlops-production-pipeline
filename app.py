

import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Fintech MLOps Dashboard", layout="wide")

# --- HEADER ---
st.title("🛡️ Real-Time Fraud Detection Pipeline")
st.markdown("""
**System Status:** `Operational` | **Environment:** `Production` | **Location:** `Berlin-AWS-Region`
""")

# --- SIDEBAR: SIMULATE INPUT ---
st.sidebar.header("Manual Transaction Entry")
amount = st.sidebar.number_input("Transaction Amount (KES)", min_value=0, value=5000)
location = st.sidebar.selectbox("Location", ["Nairobi", "Berlin", "London", "Mombasa"])
is_new_device = st.sidebar.checkbox("New Device?")

# --- MAIN INTERFACE: THE "MODEL" ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Analysis")
    if st.button("Run Prediction"):
        with st.spinner('Analyzing patterns...'):
            time.sleep(1) # Simulate inference latency
            
            # Mock Logic: Real MLOps engineers show the "why" behind a prediction
            if amount > 100000 or (is_new_device and amount > 20000):
                st.error("🚩 HIGH RISK: Potential Fraud Detected")
                st.metric("Confidence Score", "94.2%", delta="-5.1% (Anomaly)")
            else:
                st.success("✅ LOW RISK: Transaction Approved")
                st.metric("Confidence Score", "98.8%", delta="Steady")

with col2:
    st.subheader("MLOps Model Monitoring")
    # Mocking real-time monitoring data
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['Inference Latency (ms)', 'Model Accuracy']
    )
    st.line_chart(chart_data)
    st.caption("Drift Monitoring: Data distribution is within normal parameters.")

# --- FOOTER: THE TECHNICAL PROOF ---
st.divider()
st.info("Technical MLOps Specs: This pipeline uses GitHub Actions for CI/CD and is containerized for Kubernetes deployment.")
