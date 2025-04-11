# Rule-Based Financial Chatbot

## Overview
This is a basic rule-based chatbot built in Python that answers predefined financial queries using company 10-K data (CSV format).

## How it Works
- The chatbot loads data using pandas
- It supports a set of predefined queries via if-else logic
- It returns answers using data from `financial_data.csv`

## Supported Queries
- What is the total revenue of Apple in 2022?
- What is the net income growth of Tesla?
- What is the latest total assets of Microsoft?

## Limitations
- Only predefined questions are supported
- Does not use machine learning or NLP
- Only works with specific company-year combinations
