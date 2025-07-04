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
    # Set the OpenAI API key for authentication
    openai.api_key = api_key

    # Compose the prompt for summarization
    prompt = f"Summarize the following question in one or two sentences:\n\n{question}"

    # Call the OpenAI API (using ChatCompletion endpoint)
    # - model: specifies which LLM to use (e.g., "gpt-3.5-turbo" or "gpt-4")
    # - messages: conversation history; here, a system prompt and the user prompt
    # - max_tokens: limits the length of the summary
    # - temperature: controls randomness (lower is more focused)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes questions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.5
    )

    # Extract the summary text from the API response
    summary = response['choices'][0]['message']['content'].strip()
    return summary

if __name__ == "__main__":
    # Prompt the user to enter a question to summarize
    question = input("Enter the question to summarize: ")
    # Prompt the user to enter their OpenAI API key
    api_key = input("Enter your OpenAI API key: ")
    try:
        # Call the summarization function and print the result
        summary = summarize_question(question, api_key)
        print("\nSummary:")
        print(summary)
    except Exception as e:
        # Handle any errors (e.g., network issues, invalid API key)
        print(f"Error: {e}")