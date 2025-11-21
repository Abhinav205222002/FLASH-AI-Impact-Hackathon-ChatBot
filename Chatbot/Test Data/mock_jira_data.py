import pandas as pd

def get_mock_jira_data():

    jira_data = [
        {
            "Key": "JIRA-101",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Initial backend architecture setup for Spring Boot microservices",
            "Assignee": "Abhinav Raj",
            "Status": "In Progress",
            "Updated": "2025-10-26",
            "Comments": "Core project structure created. Controller/service/repo layers initialized."
        },
        {
            "Key": "JIRA-102",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Integrate Redis + MongoDB hybrid cache/store system",
            "Assignee": "Abhinav Raj",
            "Status": "In Review",
            "Updated": "2025-10-27",
            "Comments": "Unit tests added. Awaiting reviewer approval."
        },
        {
            "Key": "JIRA-103",
            "Type": "Task",
            "Priority": "Medium",
            "Summary": "Refactor service layer and optimize data access patterns",
            "Assignee": "Abhinav Raj",
            "Status": "In Progress",
            "Updated": "2025-10-28",
            "Comments": "Identified performance bottleneck in MongoDB aggregation pipeline."
        },
        {
            "Key": "JIRA-104",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Integrate AI/ML prediction engine with backend API",
            "Assignee": "Abhinav Raj",
            "Status": "To Do",
            "Updated": "2025-10-29",
            "Comments": "Blocked until ML team exposes inference endpoint."
        },
        {
            "Key": "JIRA-105",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Develop ML preprocessing engine for commit-related predictions",
            "Assignee": "Abhineet Choudhary",
            "Status": "In Progress",
            "Updated": "2025-10-28",
            "Comments": "Pipeline working; memory optimization pending."
        },
        {
            "Key": "JIRA-106",
            "Type": "Bug",
            "Priority": "High",
            "Summary": "Model training fails for large dataset",
            "Assignee": "Abhineet Choudhary",
            "Status": "Blocked",
            "Updated": "2025-10-27",
            "Comments": "Insufficient GPU memory. Needs batch-based training redesign."
        },
        {
            "Key": "JIRA-107",
            "Type": "Task",
            "Priority": "Low",
            "Summary": "Implement model monitoring and drift detection",
            "Assignee": "Abhineet Choudhary",
            "Status": "In Review",
            "Updated": "2025-10-28",
            "Comments": "Grafana dashboards added; pending QA review."
        },
        {
            "Key": "JIRA-108",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Automate ML pipeline in Jenkins CI/CD",
            "Assignee": "Abhineet Choudhary",
            "Status": "To Do",
            "Updated": "2025-10-29",
            "Comments": "Waiting for Docker image finalization."
        },

        {
            "Key": "JIRA-109",
            "Type": "Task",
            "Priority": "Medium",
            "Summary": "Implement JaCoCo XML parser for coverage extraction",
            "Assignee": "Sachin Kumar",
            "Status": "In Progress",
            "Updated": "2025-10-27",
            "Comments": "Parser implemented. Handling of nested structures pending."
        },
        {
            "Key": "JIRA-110",
            "Type": "Bug",
            "Priority": "Medium",
            "Summary": "Fix coverage mapping mismatch between test and service layer",
            "Assignee": "Sachin Kumar",
            "Status": "Blocked",
            "Updated": "2025-10-26",
            "Comments": "Issue occurs in multi-module builds. Requires build tool investigation."
        },
        {
            "Key": "JIRA-111",
            "Type": "Story",
            "Priority": "Medium",
            "Summary": "Integrate test coverage results with the regression engine",
            "Assignee": "Sachin Kumar",
            "Status": "In Progress",
            "Updated": "2025-10-28",
            "Comments": "Integration working locally. CI tests failing."
        },
        {
            "Key": "JIRA-112",
            "Type": "Story",
            "Priority": "Low",
            "Summary": "Add advanced filtering for coverage history dashboard",
            "Assignee": "Sachin Kumar",
            "Status": "To Do",
            "Updated": "2025-10-29",
            "Comments": "UI team must provide updated JSON schema."
        },
        {
            "Key": "JIRA-113",
            "Type": "Story",
            "Priority": "Medium",
            "Summary": "Develop UI dashboard layout for Git/JIRA insights",
            "Assignee": "Ayush Bhardwaj",
            "Status": "In Progress",
            "Updated": "2025-10-26",
            "Comments": "Dark mode and responsiveness added."
        },
        {
            "Key": "JIRA-114",
            "Type": "Task",
            "Priority": "Low",
            "Summary": "Connect dashboard with backend analytics API",
            "Assignee": "Ayush Bhardwaj",
            "Status": "In Review",
            "Updated": "2025-10-27",
            "Comments": "API mappings verified. Minor CSS fixes pending."
        },
        {
            "Key": "JIRA-115",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Create Kafka producer for event streaming",
            "Assignee": "Pratik Deshpande",
            "Status": "In Progress",
            "Updated": "2025-10-28",
            "Comments": "Producer functional. Adding retry logic."
        },
        {
            "Key": "JIRA-116",
            "Type": "Task",
            "Priority": "Medium",
            "Summary": "Set up multi-node Kafka cluster with schema registry",
            "Assignee": "Pratik Deshpande",
            "Status": "In Progress",
            "Updated": "2025-10-27",
            "Comments": "Cluster up. Avro schema integration ongoing."
        },
        {
            "Key": "JIRA-117",
            "Type": "Bug",
            "Priority": "High",
            "Summary": "Fix consumer lag spikes during heavy ingestion",
            "Assignee": "Pratik Deshpande",
            "Status": "Blocked",
            "Updated": "2025-10-26",
            "Comments": "Requires partition rebalancing and retry configuration."
        },
        {
            "Key": "JIRA-118",
            "Type": "Story",
            "Priority": "High",
            "Summary": "Configure MongoDB sharded cluster",
            "Assignee": "Lahu Pachpol",
            "Status": "In Progress",
            "Updated": "2025-10-26",
            "Comments": "Shards configured. Balancer tests pending."
        },
        {
            "Key": "JIRA-119",
            "Type": "Bug",
            "Priority": "Medium",
            "Summary": "Fix memory leak in connection pool manager",
            "Assignee": "Lahu Pachpol",
            "Status": "Blocked",
            "Updated": "2025-10-25",
            "Comments": "Leak traced to retry logic. Fix in progress."
        },
        {
            "Key": "JIRA-120",
            "Type": "Task",
            "Priority": "Low",
            "Summary": "Implement read/write split logic for DB load balancing",
            "Assignee": "Lahu Pachpol",
            "Status": "In Review",
            "Updated": "2025-10-27",
            "Comments": "Read routing complete. Write router under review."
        },
        {
            "Key": "JIRA-121",
            "Type": "Story",
            "Priority": "Medium",
            "Summary": "Optimize indexing strategy for large collections",
            "Assignee": "Lahu Pachpol",
            "Status": "In Progress",
            "Updated": "2025-10-28",
            "Comments": "Index advisor tool integrated."
        },

        {
            "Key": "JIRA-122",
            "Type": "Task",
            "Priority": "Medium",
            "Summary": "Enhance regression test suite with parallel execution",
            "Assignee": "Dhanashree Pawar",
            "Status": "In Progress",
            "Updated": "2025-10-27",
            "Comments": "Parallel execution working; unstable tests identified."
        },
        {
            "Key": "JIRA-123",
            "Type": "Bug",
            "Priority": "High",
            "Summary": "Fix flaky integration tests on pipeline Stage-3",
            "Assignee": "Dhanashree Pawar",
            "Status": "Blocked",
            "Updated": "2025-10-26",
            "Comments": "Failures caused by slow DB container startup."
        }
    ]

    return pd.DataFrame(jira_data)




# import pandas as pd

# def get_mock_jira_data():
#     jira_data = [
#         {
#             "Key": "JIRA-101",
#             "Type": "Story",
#             "Priority": "High",
#             "Summary": "Implement module to extract and analyze code changes from Git repository",
#             "Assignee": "Abhinav Raj",
#             "Status": "In Progress",
#             "Updated": "2025-10-26",
#             "Comments": "Backend logic implemented. REST endpoint pending."
#         },
#         {
#             "Key": "JIRA-102",
#             "Type": "Story",
#             "Priority": "High",
#             "Summary": "Develop ML model to predict and prioritize test cases based on code changes",
#             "Assignee": "Abhineet Choudhary",
#             "Status": "Blocked",
#             "Updated": "2025-10-28",
#             "Comments": "Model training stuck due to missing historical test data. Blocked."
#         },
#         {
#             "Key": "JIRA-103",
#             "Type": "Task",
#             "Priority": "Medium",
#             "Summary": "Implement parser to map test cases to source code using JaCoCo coverage data",
#             "Assignee": "Sachin Kumar",
#             "Status": "In Progress",
#             "Updated": "2025-10-27",
#             "Comments": "Parser reading coverage files correctly. Integration next."
#         },
#         {
#             "Key": "JIRA-104",
#             "Type": "Story",
#             "Priority": "High",
#             "Summary": "Integrate AI-based regression test selector into Jenkins CI pipeline",
#             "Assignee": "Abhinav Raj",
#             "Status": "To Do",
#             "Updated": "2025-10-25",
#             "Comments": "Waiting for model service endpoint to be finalized."
#         },
#         {
#             "Key": "JIRA-105",
#             "Type": "Task",
#             "Priority": "Medium",
#             "Summary": "Create dashboard to visualize test case prioritization and execution results",
#             "Assignee": "Ayush Bhardwaj",
#             "Status": "In Review",
#             "Updated": "2025-10-28",
#             "Comments": "Frontend done. Awaiting backend API integration."
#         },
#     ]
#     return pd.DataFrame(jira_data)
