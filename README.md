# Codinator

Codinator is a code review tool that leverages human-readable requirements specified in a YAML file to automate the code review process. By integrating Codinator into your GitHub workflow, you can ensure that your pull requests meet the specified coding standards before merging.

## Getting Started
### Prerequisites
- Git
- Python 3.x
- A GitHub account with repository access

### Open AI API Key
Codinator uses the OpenAI API to generate human-readable feedback. To use Codinator, you will need to sign up for an API key at [OpenAI](https://beta.openai.com/signup/).

## Installation
#### 1. Clone the Codinator Repository into your project:
```
git clone git@github.com:cadigun/codinator-ai.git
```
#### 2. Navigate to the Codinator Directory:
```
cd codinator
```
#### 3. Install Required Dependencies:
```angular2html
pip install -r requirements.txt
```

## Setting Up the Specification File
Codinator uses a YAML file to define the code review requirements. An example specification file is provided in the repository. 
Make sure to update the default branch to that of your repository. You can modify the requirements to suit your project's needs.
```angular2html
project:
  name: "project_name"
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
In the root of your repository, create a new file under `.github/workflows/` with a .yml extension, for example, see `codinator_review.yml` in this project.
#### 2. Define the Workflow:
Copy the content of the example workflow in this repository found in `./github/workflows/codinator_review.yml`.
#### 3. Modify Run Codinator with the Correct Path:
Replace `path/to/codinator.py` with the actual path to the codinator.py file in your repository.
```
      run: |
          output=$(python path/to/codinator.py)
```

## Usage
Once the workflow is set up, Codinator will automatically run on each pull request, checking the changes against the specified requirements and providing feedback.

## Contributing
Contributions to Codinator are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

