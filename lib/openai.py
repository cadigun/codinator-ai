import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set your API key here
openai.api_key = os.environ.get("OPENAI_API_KEY")

MSG = """
We have a list of requirements that must be satisfied by any code pull request. Additionally, we have the git diff of changes that happened in the code. Please review the changes based on the requirements and provide code review comments.

Requirements:
%s

Git Diff:
%s

Please provide Code Review Comments.
"""

def get_openai_response(requirements, git_diff):
    if not requirements:
        return "No requirements provided"
    if not git_diff:
        return "No git diff provided"
    prompt = MSG % (requirements, git_diff)
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