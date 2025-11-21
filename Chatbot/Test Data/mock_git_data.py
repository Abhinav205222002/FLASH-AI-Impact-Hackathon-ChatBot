import pandas as pd
import json
from datetime import datetime

# ===========================================
# Load the static 70-commit JSON into memory
# ===========================================

mock_git_commits_json = [
  {"Author": "Abhinav Raj", "Date": "2025-10-01", "Message": "[JIRA-101] Initial Spring Boot project setup"},
  {"Author": "Abhinav Raj", "Date": "2025-10-02", "Message": "[JIRA-101] Added JWT authentication service"},
  {"Author": "Abhinav Raj", "Date": "2025-10-03", "Message": "[JIRA-102] Implemented Redis cache layer"},
  {"Author": "Abhinav Raj", "Date": "2025-10-04", "Message": "[JIRA-102] MongoDB configuration and repository layer"},
  {"Author": "Abhinav Raj", "Date": "2025-10-05", "Message": "[JIRA-103] Refactored service architecture"},
  {"Author": "Abhinav Raj", "Date": "2025-10-06", "Message": "[JIRA-103] Added exception handling middleware"},
  {"Author": "Abhinav Raj", "Date": "2025-10-07", "Message": "[JIRA-104] Integrated AI/ML prediction microservice"},
  {"Author": "Abhinav Raj", "Date": "2025-10-08", "Message": "[JIRA-104] Dockerized backend and updated CI/CD"},
  {"Author": "Abhinav Raj", "Date": "2025-10-09", "Message": "[JIRA-103] Performance tuning: DB query optimization"},
  {"Author": "Abhinav Raj", "Date": "2025-10-10", "Message": "[JIRA-101] Fixed bug: Circular dependency in service layer"},

  {"Author": "Abhineet Choudhary", "Date": "2025-10-01", "Message": "[JIRA-105] ML data preprocessing pipeline added"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-02", "Message": "[JIRA-105] Model training script for scoring engine"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-03", "Message": "[JIRA-106] ML model inference API"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-04", "Message": "[JIRA-106] Integrated ML model with feature store"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-05", "Message": "[JIRA-107] Added monitoring metrics for AI service"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-06", "Message": "[JIRA-107] Optimized training pipeline for speed"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-07", "Message": "[JIRA-108] Jenkins ML automation pipeline"},
  {"Author": "Abhineet Choudhary", "Date": "2025-10-08", "Message": "[JIRA-108] Improved dataset validation logic"},

  {"Author": "Sachin Kumar", "Date": "2025-10-01", "Message": "[JIRA-109] Implemented JaCoCo XML parser"},
  {"Author": "Sachin Kumar", "Date": "2025-10-02", "Message": "[JIRA-109] Test-case to source-file mapping engine"},
  {"Author": "Sachin Kumar", "Date": "2025-10-03", "Message": "[JIRA-110] SonarQube rule integration"},
  {"Author": "Sachin Kumar", "Date": "2025-10-04", "Message": "[JIRA-110] Build optimization and cleanup"},
  {"Author": "Sachin Kumar", "Date": "2025-10-05", "Message": "[JIRA-111] Fixed coverage parser indexing bug"},
  {"Author": "Sachin Kumar", "Date": "2025-10-06", "Message": "[JIRA-112] Updated coverage threshold rules"},
  {"Author": "Sachin Kumar", "Date": "2025-10-07", "Message": "[JIRA-112] CI pipeline unit test improvements"},

  {"Author": "Ayush Bhardwaj", "Date": "2025-10-01", "Message": "[JIRA-113] UI dashboard layout created"},
  {"Author": "Ayush Bhardwaj", "Date": "2025-10-02", "Message": "[JIRA-113] Integrated Plotly graphs for analytics"},
  {"Author": "Ayush Bhardwaj", "Date": "2025-10-03", "Message": "[JIRA-114] Linked UI forms with backend APIs"},
  {"Author": "Ayush Bhardwaj", "Date": "2025-10-04", "Message": "[JIRA-114] Enhanced UX on report screens"},
  {"Author": "Ayush Bhardwaj", "Date": "2025-10-05", "Message": "[JIRA-114] Fixed UI refresh state issue"},

  {"Author": "Pratik Deshpande", "Date": "2025-10-01", "Message": "[JIRA-115] Added Kafka message producer"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-02", "Message": "[JIRA-115] Implemented retry logic for event failure"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-03", "Message": "[JIRA-116] Multi-node Kafka cluster setup"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-04", "Message": "[JIRA-116] Added schema registry with Avro"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-05", "Message": "[JIRA-117] Optimized consumer lag handling"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-06", "Message": "[JIRA-117] Improved async event handling logic"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-07", "Message": "[JIRA-115] Fixed Kafka commit offset error"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-08", "Message": "[JIRA-116] Updated topic configuration scripts"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-09", "Message": "[JIRA-117] Refactored event ingestion service"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-10", "Message": "[JIRA-115] Configured Jenkins CI for events service"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-11", "Message": "[JIRA-116] Retry backoff strategy improvements"},
  {"Author": "Pratik Deshpande", "Date": "2025-10-12", "Message": "[JIRA-117] Analytics log ingestion optimized"},

  {"Author": "Lahu Pachpol", "Date": "2025-10-01", "Message": "[JIRA-118] Configured MongoDB sharded cluster"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-02", "Message": "[JIRA-118] Improved Mongo query performance"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-03", "Message": "[JIRA-119] Added migration scripts for DB upgrade"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-04", "Message": "[JIRA-119] Fixed connection pool leak issue"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-05", "Message": "[JIRA-120] Implemented read/write split module"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-06", "Message": "[JIRA-120] Automated backup/restore job"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-07", "Message": "[JIRA-121] Improved schema validation rules"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-08", "Message": "[JIRA-121] Optimized indexing for large collections"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-09", "Message": "[JIRA-118] Added VPC peering configuration"},
  {"Author": "Lahu Pachpol", "Date": "2025-10-10", "Message": "[JIRA-119] Security patch update applied"},

  {"Author": "Dhanashree Pawar", "Date": "2025-10-01", "Message": "[JIRA-122] CI pipeline for automated test execution"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-02", "Message": "[JIRA-122] Regression test suite improvements"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-03", "Message": "[JIRA-123] Refactored flaky integration tests"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-04", "Message": "[JIRA-123] Integrated Allure reports"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-05", "Message": "[JIRA-122] Added merge-quality gates"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-06", "Message": "[JIRA-123] Fixed test pipeline Stage-3"},
  {"Author": "Dhanashree Pawar", "Date": "2025-10-07", "Message": "[JIRA-122] Enhanced dynamic test data generator"}
]

# ===========================================
# PUBLIC FUNCTION TO FETCH COMMITS BY DATE
# ===========================================

def get_mock_git_commits(start_date, end_date):

    df = pd.DataFrame(mock_git_commits_json)

    df["Date"] = pd.to_datetime(df["Date"])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    return df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]






# import pandas as pd
# from datetime import datetime, timedelta
# from mock_jira_data import get_mock_jira_data

# def get_mock_git_data():
#     jira_df = get_mock_jira_data()

#     developers = jira_df["Assignee"].unique().tolist()

#     commits = []
#     base_date = datetime(2025, 10, 1)

#     # Create 10 commits per developer
#     commit_messages = [
#         "Implemented logic",
#         "Fixed bug",
#         "Refactored module",
#         "Improved performance",
#         "Updated API integration",
#         "Enhanced logging",
#         "Added validation",
#         "Updated documentation",
#         "Improved test cases",
#         "Final cleanup"
#     ]

#     day_offset = 0

#     for dev in developers:
#         dev_jiras = jira_df[jira_df["Assignee"] == dev]["Key"].tolist()

#         for i in range(10):
#             jira_id = dev_jiras[i % len(dev_jiras)]  # Rotate between their Jira issues

#             commits.append({
#                 "Author": dev,
#                 "Date": (base_date + timedelta(days=day_offset)).strftime("%Y-%m-%d"),
#                 "Message": f"[{jira_id}] {commit_messages[i]}",
#                 "Commit SHA": f"mocksha{dev[:2].lower()}{i}"
#             })

#             day_offset += 1

#     return pd.DataFrame(commits)
# import pandas as pd
# from datetime import datetime, timedelta

# def get_mock_git_commits(start_date, end_date):
    
#     data = []

#     developers = [
#         "Abhinav Raj",
#         "Abhineet Choudhary",
#         "Sachin Kumar",
#         "Ayush Bhardwaj",
#         "Pratik Deshpande",
#         "Lahu Pachpol",
#         "Dhanashree Pawar"
#     ]

#     jira_ids = ["JIRA-101", "JIRA-102", "JIRA-103", "JIRA-104", "JIRA-105"]

#     base_date = datetime(2025, 10, 1)

#     for dev in developers:
#         for i in range(10):
#             commit_date = base_date + timedelta(days=i * 3)

#             data.append({
#                 "Commit SHA": f"mocksha{i}{dev[:2]}",
#                 "Author": dev,
#                 "Date": commit_date.strftime("%Y-%m-%d"),
#                 "Message": f"[{jira_ids[i % len(jira_ids)]}] Commit {i+1} by {dev}"
#             })

#     df = pd.DataFrame(data)

#     df["Date"] = pd.to_datetime(df["Date"])
#     start_date = pd.to_datetime(start_date)
#     end_date = pd.to_datetime(end_date)

#     return df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
