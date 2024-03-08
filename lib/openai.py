import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set your API key here
openai.api_key = os.environ.get("OPENAI_API_KEY")

PROMPT_TEXT = """
As a code reviewer, please provide helpful review comments for the following code changes. Focus on the following aspects:
%s

Be specific and provide actionable feedback, including line numbers and code snippets where appropriate.
Use examples and developer references to point out best practices where necessary.
Use a clear and friendly tone, with emojis 😊. 

Here are the code changes:
%s

Thank you for your help!
"""

def get_openai_response(requirements, git_diff):
    if not requirements:
        return "No requirements provided"
    if not git_diff:
        return "No git diff provided"
    prompt = PROMPT_TEXT % (requirements, git_diff)
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return completion.choices[0].message.content