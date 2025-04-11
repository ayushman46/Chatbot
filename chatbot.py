import pandas as pd

# Load the data
df = pd.read_csv('10K_Financial_Data_Microsoft_Tesla_Apple.csv')

# Rule-based chatbot logic
def simple_chatbot(user_query):
    if user_query == "What is the total revenue of Apple in 2022?":
        result = df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2022)]['Total Revenue (B)'].values
        if result.size > 0:
            return f"Apple's total revenue in 2022 was ${result[0]} billion."
        else:
            return "Sorry, the data for Apple in 2022 is not available."

    elif user_query == "What is the net income growth of Tesla?":
        tesla_df = df[df['Company'] == 'Tesla'].sort_values('Fiscal Year')
        tesla_df['Growth (%)'] = tesla_df['Net Income (B)'].pct_change() * 100
        last_year_growth = tesla_df.iloc[-1]['Growth (%)']
        return f"Tesla's net income grew by {last_year_growth:.2f}% compared to the previous year."

    elif user_query == "What is the latest total assets of Microsoft?":
        ms_df = df[df['Company'] == 'Microsoft'].sort_values('Fiscal Year')
        latest = ms_df.iloc[-1]
        return f"The latest total assets of Microsoft are ${latest['Total Assets (B)']} billion."

    elif user_query == "What is the operating income of Google in 2021?":
        result = df[(df['Company'] == 'Google') & (df['Fiscal Year'] == 2021)]['Operating Income (B)'].values
        if result.size > 0:
            return f"Google's operating income in 2021 was ${result[0]} billion."
        else:
            return "Sorry, the data for Google in 2021 is not available."

    elif user_query == "What is the total equity of Amazon in the latest fiscal year?":
        amazon_df = df[df['Company'] == 'Amazon'].sort_values('Fiscal Year')
        latest = amazon_df.iloc[-1]
        return f"The total equity of Amazon in the latest fiscal year is ${latest['Total Equity (B)']} billion."

    elif user_query == "What is the revenue growth of Apple over the last 3 years?":
        apple_df = df[df['Company'] == 'Apple'].sort_values('Fiscal Year')
        apple_df['Revenue Growth (%)'] = apple_df['Total Revenue (B)'].pct_change() * 100
        recent_growth = apple_df.iloc[-1]['Revenue Growth (%)']
        return f"Apple's revenue grew by {recent_growth:.2f}% over the last year."

    elif user_query == "What is the net income of Tesla in 2020?":
        result = df[(df['Company'] == 'Tesla') & (df['Fiscal Year'] == 2020)]['Net Income (B)'].values
        if result.size > 0:
            return f"Tesla's net income in 2020 was ${result[0]} billion."
        else:
            return "Sorry, the data for Tesla in 2020 is not available."

    elif user_query == "What is the debt-to-equity ratio of Microsoft in 2022?":
        if 'Total Debt (B)' in df.columns and 'Total Equity (B)' in df.columns:
            result = df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 2022)]
            if not result.empty:
                debt_to_equity = result.iloc[0]['Total Debt (B)'] / result.iloc[0]['Total Equity (B)']
                return f"Microsoft's debt-to-equity ratio in 2022 was {debt_to_equity:.2f}."
            else:
                return "Sorry, the data for Microsoft in 2022 is not available."
        else:
            return "Sorry, the required data for calculating the debt-to-equity ratio is missing."

    else:
        return "Sorry, I can only answer predefined questions. Try asking about revenue, net income, or assets."

# Main loop
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    print("Type your question or type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Bot:", response)
