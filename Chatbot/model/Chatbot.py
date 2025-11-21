# -*- coding: utf-8 -*-
"""ImpactHackathon.ipynb





!pip install PyGithub google-generativeai streamlit pyngrok pandas matplotlib plotly

import os

os.environ['GITHUB_TOKEN'] = "my_github_token"
os.environ['GOOGLE_API_KEY'] = "my_google_api_key"
os.environ['NGROK_AUTH_TOKEN'] = "my_ngrok_auth_token"

rm -f app.py

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import os
# import requests
# import pandas as pd
# import streamlit as st
# from datetime import datetime
# from pyngrok import ngrok
# import google.generativeai as genai
# import plotly.express as px
# 
# 
# mock_jira_path = "/content/mock_jira_data.py"
# mock_git_path = "/content/mock_git_data.py"
# 
# jira_scope = {}
# exec(open(mock_jira_path).read(), jira_scope)
# get_mock_jira_data = jira_scope["get_mock_jira_data"]
# 
# git_scope = {}
# exec(open(mock_git_path).read(), git_scope)
# get_mock_git_commits = git_scope["get_mock_git_commits"]
# 
# 
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# 
# model = genai.GenerativeModel("gemini-2.5-pro")
# 
# 
# 
# st.set_page_config(page_title="GitHub + JIRA Dashboard + Chatbot", layout="wide")
# 
# st.title("📊 Git Commit Dashboard + 🧩 JIRA Issue Tracker + 🤖 Chatbot")
# 
# 
# 
# st.sidebar.header("🔧 Configuration")
# 
# start_date = st.sidebar.date_input("Select Start Date", datetime(2025, 10, 1))
# end_date = st.sidebar.date_input("Select End Date", datetime.now())
# 
# developer_list = ["Abhinav Raj","Pratik Deshpande","Lahu Pachpol", "Abhineet Choudhary", "Sachin Kumar","Dhanashree Pawar" "Ayush Bhardwaj"]
# selected_developer = st.sidebar.selectbox("Select Developer for JIRA:", developer_list)
# 
# 
# 
# st.header("📈 Git Commit Logs")
# 
# if st.button("Fetch Git Commits"):
#     df_git = get_mock_git_commits(start_date, end_date)
# 
#     if df_git.empty:
#         st.warning("No commits found in this date range.")
#     else:
#         st.dataframe(df_git)
# 
#         st.success(f"Showing {len(df_git)} commits between {start_date} and {end_date}")
# 
# 
#         st.session_state.git_context = df_git.to_string(index=False)
# 
# 
#         st.subheader("📊 Commit Count per Developer")
# 
#         commit_counts = df_git["Author"].value_counts().reset_index()
#         commit_counts.columns = ["Developer", "Commit Count"]
# 
#         fig = px.bar(
#             commit_counts,
#             x="Developer",
#             y="Commit Count",
#             color="Developer",
#             text="Commit Count",
#             title="Commit Count by Developer (Selected Date Range)",
#             template="plotly_white"
#         )
# 
#         fig.update_traces(textposition="outside")
#         fig.update_layout(showlegend=False)
# 
#         st.plotly_chart(fig, use_container_width=True)
# 
# 
# st.header("🧩 JIRA Issue Tracker")
# 
# def fetch_jira_for_user(user_name):
#     df = get_mock_jira_data()
#     return df[df["Assignee"].str.lower().str.contains(user_name.lower())]
# 
# def analyze_jira(df):
#     if df.empty:
#         return "No active JIRA for this developer."
# 
#     total = len(df)
#     blocked = df[df["Comments"].str.contains("block", case=False)]
#     progress = df[df["Status"].str.contains("progress", case=False)]
# 
#     summary = f"Total Open JIRA: {total}\n\n"
# 
#     if not blocked.empty:
#         summary += "🚧 Blocked Issues:\n"
#         for _, r in blocked.iterrows():
#             summary += f"- {r['Key']} — {r['Summary']} ({r['Comments']})\n"
# 
#     if not progress.empty:
#         summary += "\n⚙️ In Progress:\n"
#         for _, r in progress.iterrows():
#             summary += f"- {r['Key']} — {r['Summary']}\n"
# 
#     summary += "\n📋 Status Table:\n"
#     summary += df[['Key','Status','Assignee']].to_string(index=False)
#     return summary
# 
# if st.button("Fetch JIRA Details"):
#     df_jira = fetch_jira_for_user(selected_developer)
#     st.dataframe(df_jira)
# 
#     st.session_state.jira_context = df_jira.to_string(index=False)
# 
#     st.text(analyze_jira(df_jira))
# 
# 
# st.header("🤖 Chatbot")
# 
# query = st.text_input("Ask anything about Git commits or JIRA issues:")
# 
# def build_context():
#     ctx = ""
# 
#     if "git_context" in st.session_state:
#         ctx += "\n=== Git Commit Log ===\n" + st.session_state.git_context
# 
#     if "jira_context" in st.session_state:
#         ctx += "\n\n=== JIRA Issues ===\n" + st.session_state.jira_context
# 
#     return ctx if ctx.strip() else "No data loaded yet."
# 
# if st.button("Ask Chatbot"):
#     context = build_context()
# 
#     prompt = f"""
# You are an expert AI project assistant.
# Use ONLY the data in the context below.
# 
# If the question is outside this data, answer:
# "I can only answer based on available Git & JIRA data."
# 
# Context:
# {context}
# 
# User Question:
# {query}
# 
# Give a structured, accurate response.
# """
# 
#     with st.spinner("Chatbot thinking..."):
#         response = model.generate_content(prompt)
# 
#     st.subheader("🤖 Chatbot Response")
#     st.write(response.text)
# 
# 
# 
# st.markdown("---")
# st.subheader("🌍 Generate Public Share Link")
# 
# if st.button("Start Public Link"):
#     try:
#         ngrok.kill()
#         public_url = ngrok.connect(8501)
#         st.success(f"Your App is Live at: {public_url}")
#     except Exception as e:
#         st.error(f"Ngrok error: {e}")
#

from pyngrok import ngrok
import subprocess


!ngrok config add-authtoken $NGROK_AUTH_TOKEN


process = subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8501"])
public_url = ngrok.connect(8501)
print(f"🌍 Your public app link: {public_url}")