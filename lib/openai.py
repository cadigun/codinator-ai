import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set your API key here
openai.api_key = os.environ.get("OPENAI_API_KEY")

PROMPT_TEXT = """
Please provide a thorough and technical code review in less than %s words, using the following guidelines:
%s

Your response must be concise, and clear, and you need to provide actionable feedback, reference line numbers and code snippets.
Give examples and developer references to point out best practices where necessary.
Use a friendly tone, emojis are allowed 😊. 

Here are the code changes:
%s

Thank you for your help!
"""

def get_openai_response(requirements, git_diff):
    if not requirements:
        return "No requirements provided"
    if not git_diff:
        return "No git diff provided"
    if not openai.api_key:
        return "No OpenAI API key found"

    try:
        max_tokens = int(os.environ.get("CHAT_GPT_CHARACTER_LIMIT", "1000"))
    except ValueError:
        max_tokens = 1000

    prompt = PROMPT_TEXT % (max_tokens, requirements, git_diff)
    completion = openai.chat.completions.create(
        model=os.environ.get("CHAT_GPT_MODEL") or "gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content