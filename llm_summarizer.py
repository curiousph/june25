# This program demonstrates how to connect to an LLM API (such as OpenAI's GPT) to summarize questions.
# You need an API key and the openai package installed (`pip install openai`).

import openai

def summarize_question(question, api_key):
    """
    Sends a question to the LLM API and returns a summary.
    Args:
        question (str): The question to summarize.
        api_key (str): Your OpenAI API key.
    Returns:
        str: The summarized question.
    """
    openai.api_key = api_key

    # Compose the prompt for summarization
    prompt = f"Summarize the following question in one or two sentences:\n\n{question}"

    # Call the OpenAI API (GPT-3.5/4)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes questions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.5
    )

    summary = response['choices'][0]['message']['content'].strip()
    return summary

if __name__ == "__main__":
    # Get user input for the question and API key
    question = input("Enter the question to summarize: ")
    api_key = input("Enter your OpenAI API key: ")
    try:
        summary = summarize_question(question, api_key)
        print("\nSummary:")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")