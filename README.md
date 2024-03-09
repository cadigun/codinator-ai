# Codinator AI
Codinator-ai is a ChatGPT-powered tool that automates code review and enforcement of coding standards using.
It uses YAML-defined requirements written in plain human language to analyze your code changes and provides feedback directly in your pull requests.

## Examples
For practical examples of how to use Codinator AI in your projects, check out the [codinator-ai-samples](https://github.com/cadigun/codinator-ai-samples/pulls) repository.
This repository contains sample projects and specification files to help you get started and understand how Codinator AI can be applied to your project.

## Prerequisites
#### Open AI API Key
To use Codinator AI, you will need to sign up for an API key at [OpenAI](https://beta.openai.com/signup/).

## Getting Started
#### 1. Create a Specification File
Create a specification file in your repository based on the sample provided in `.codinator-spec-sample`. This file should define the rules and standards that Codinator AI will enforce in your code reviews.
```
project:
  name: "codinator-ai"
  default_branch: "main"
  files_types:
  # define the file types that will be reviewed by Codinator
    - ".go"
    - ".java"
  requirements:
  # human readable requirements
    - "Class names should be in PascalCase."
    - "Use descriptive names for test methods (e.g., shouldReturnTrueWhenConditionMet)."
    - "Do not use matcher type of any in tests."
```

#### 2. Set Up GitHub Secrets
Navigate to your repository's Settings > Secrets > Actions.
<img width="1159" alt="Actions_secrets_·_cadigun_codinator-ai" src="https://github.com/cadigun/codinator-ai/assets/10423381/612bb4d3-ce00-4ebc-a854-997edc80fee1">
Add the following secrets:
- **OPENAI_API_KEY**: Your OpenAI API key.
- **SPEC_FILE_PATH**: Path to your specification file (relative to the root of your repository e.g., your_project/.codinator-spec-sample).
- **ACCESS_TOKEN_GITHUB**: Your GitHub API access token with repo permissions.
- **CHAT_GPT_MODEL**: (Optional) Your preferred Chat GPT model. Default is gpt-3.5-turbo. 
- **CHAT_GPT_CHARACTER_LIMIT**: (Optional) Maximum character limit for the chat response. Default is 1000.

#### 3.  Set Up the GitHub Workflow
Copy `.github/workflows/codinator.yml` into your project's root directory.
This file contains the workflow that will run Codinator AI on each pull request.
If you don't have a `.github/workflows` directory, create one in the root of your repository.

**NOTE**: If the default branch name of your repository is not main, modify the `on` section:
```angular2html
on:
  pull_request:
    branches:
      - your_default_branch_name
```

## Support
If you encounter any issues or have questions, please feel free to open an issue on the Codinator AI GitHub repository.
For contributions, create a fork of the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

