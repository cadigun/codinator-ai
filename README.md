# Codinator
Codinator-ai is a ChatGPT-powered code review tool that uses YAML-defined requirements, written in plain human language to post comments on PRs.
When integrated into a GitHub workflow, Codinator-ai automatically reviews each PR against these requirements and posts comments directly on the PR, highlighting any issues or deviations from the defined standards. This ensures that code meets the specified quality criteria before it is merged into the main codebase.

It works with all programming languages and can be customized to suit the specific requirements of your project.

#### Example of Codinator-ai in action:
<img width="727" alt="Screenshot 2024-03-08 at 12 03 46 PM" src="https://github.com/cadigun/codinator-ai/assets/10423381/d3616572-a45d-4d66-8883-2170a42a0efb">

## Getting Started
### Prerequisites
#### Open AI API Key
Codinator uses the OpenAI API to generate human-readable feedback. To use Codinator, you will need to sign up for an API key at [OpenAI](https://beta.openai.com/signup/).

## Installation
#### 1. Clone the Codinator Repository into your project:
```
git clone git@github.com:cadigun/codinator-ai.git
```

## Setting Up the Specification File
Codinator uses a YAML file to define the code review requirements. An example specification file is provided in the repository. 
Make sure to update the default branch to that of your repository. You can modify the requirements to suit your project's needs.
```angular2html
project:
  name: your_project_name
  default_branch: main
  files_types:
  # File types to be reviewed by Codinator
    - ".go"
    - ".java"
  requirements:
  # Add your code review guidelines here.
    - "Class names should be in PascalCase."
    - "Use descriptive names for test methods (e.g., shouldReturnTrueWhenConditionMet)."
    - "Do not use matcher type of any in tests."
    - "All files must end with a newline."
    - "Constants should be in UPPER_SNAKE_CASE."
    - "Provide Javadoc comments for all public classes and methods."
    - "Each public method should have corresponding unit tests."
```

## Configuring GitHub Secrets
To use Codinator with GitHub Actions, you need to set up GitHub Secrets for environment variables. These variables can include API keys or other sensitive information required by your script.

For instructions on how to set up GitHub Secrets, please refer to the [GitHub documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

## Integrating Codinator into Your GitHub Workflow
#### 1. Create a Workflow YAML File:
In the root of your repository, create a new file under `.github/workflows/` with a .yml extension. For example, see `codinator.yml` in this project's .github folder.
#### 2. Define the Workflow:
Copy the content of the example workflow in this repository found in `./github/workflows/codinator.yml`.
#### 3. If your default branch name is not main, modify the `on` section:
```angular2html
on:
  pull_request:
    branches:
      - your_default_branch_name
```
#### 4. Modify `Run Python script` with the Relative Path from your project:
In the `Run Python script` step, replace the command `python codinator.py` with the relative path to run the codinator.py script in your project.
e.g.
```angular2html
    run: |
        stdout=$(python path/to/your_project/codinator-ai/codinator.py | sed 's/`/\\`/g' | sed ':a;N;$!ba;s/\n/\\n/g')
```
## Usage
Once the workflow is set up, Codinator will automatically run on each pull request, checking the changes against the specified requirements and providing feedback.

## Contributing
Contributions to Codinator are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

