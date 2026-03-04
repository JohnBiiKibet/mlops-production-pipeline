---
title: MLOps Production Pipeline
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: app.py
pinned: false
---




🛡️ Real-Time Fraud Detection Pipeline
An interactive MLOps dashboard built with Streamlit to demonstrate real-time transaction analysis, risk scoring, and model health monitoring. This system simulates a high-stakes fintech environment located in the Berlin-AWS-Region [User Code].


🚀 Overview
This application serves as a Proof-of-Concept (PoC) for a machine learning-powered fraud detection system. It bridges the gap between manual transaction entry and automated risk assessment using simulated inference logic and real-time drift monitoring. 


Key Features
Manual Transaction Entry: Input custom amounts (KES) and locations (e.g., Nairobi, London) to test model behavior [User Code].
Real-Time Prediction: Immediate classification into HIGH RISK or LOW RISK based on heuristic-driven anomaly detection [User Code].
Confidence Metrics: Dynamic scoring that tracks model certainty and historical deltas [User Code].
MLOps Monitoring: Live visualizations for Inference Latency and Model Accuracy to detect performance degradation.
Drift Analysis: Automated captions highlighting data distribution status [User Code].


🛠️ Technical Stack
Framework: Streamlit for the web interface.
Data Processing: Pandas and NumPy for synthetic data generation and manipulation.
Infrastructure: Containerized for Kubernetes with GitHub Actions for CI/CD automation.

⚙️ Installation & Local Setup
To run this dashboard locally, ensure you have Python 3.7+ installed. 
Medium
Medium
Clone the Repository


git clone <your-repo-url>
cd <project-folder>


Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

streamlit run app.py


Launch the App

streamlit run app.py



📊 MLOps Lifecycle Integration
This dashboard represents a Level 0 (Manual) to Level 1 (Automated) MLOps maturity stage by providing: 
GitHub
GitHub
Explainability: Visual indicators of "why" a transaction was flagged.
Infrastructure as Code: Ready-to-deploy specs for production environments.
Continuous Monitoring: Integrated tracking of system latency and accuracy metrics. 
