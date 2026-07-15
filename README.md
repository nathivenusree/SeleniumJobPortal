# Selenium Job Portal Automation

## Project Overview
This project automates a Django Job Portal using Selenium WebDriver and Pytest.

## Technologies
- Python
- Selenium
- Pytest
- Page Object Model (POM)
- WebDriver Manager
- HTML Reports

## Features
- Login Test
- Jobs Page Test
- Apply Job Test
- HTML Reports
- Screenshots on Failure
- Logging

## Project Structure

SeleniumJobPortal/
│
├── pages/
├── tests/
├── utils/
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── requirements.txt
└── README.md

## Run Tests

pytest -v

## Generate HTML Report

pytest --html=reports/report.html --self-contained-html