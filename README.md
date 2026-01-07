# SQA_PROJECT
# SQA Python API & Data Testing Project

## 1. Objective
This project demonstrates API testing and data quality testing
using Python, following SQA best practices.

## 2. Scope
- Test GET /users API
- Validate API response status, response time
- Validate mandatory fields
- Perform data quality checks (NULL, duplicate, format, row count)

## 3. Tech Stack
- Python
- requests
- pandas

## 4. Project Structure
- tests/: test cases
- utils/: reusable functions
- data/: test data (CSV)
- logs/: execution logs
- config.py: configuration

## 5. How to Run
```bash
cd D:\SQA_PROJECT
D:\SQA_PROJECT> python -m venv venv
D:\SQA_PROJECT> venv\Scripts\activate
D:\> python -m SQA_PROJECT.tests.test_api
D:\> python -m SQA_PROJECT.tests.test_data_quality
