Project Title: Financial Chatbot Prototype

Objective:
To develop a simple rule-based chatbot that responds to predefined financial queries based on previously analyzed data from company 10-K reports.

Core Features:
- Rule-based logic using Python `if-else` or dictionary lookup
- Responds to 3 predefined queries: revenue, net income, and assets
- Handles unknown queries gracefully with a friendly fallback message
- Supports case-insensitive input matching

How it works:
The chatbot is written in Python and runs in the terminal. It takes user input, checks if the input matches a predefined financial query, and returns the appropriate response. For any unknown query, the bot replies with a default message.

Limitations:
- Only supports predefined questions
- No natural language understanding or dynamic data retrieval
- Cannot parse free-text financial documents

Tools Used:
- Python (Standard Library)
- (Optional) pandas for structured data reading (not implemented in this prototype)

Next Steps:
In future iterations, the chatbot can be expanded to support:
- NLP-based query parsing
- Data fetching from CSV or live APIs
- Dynamic response generation based on user intent
