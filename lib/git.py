import subprocess

def git_changed_files(branch_name):
    # Run the git diff command with the --name-only option to list changed files
    command = ['git', 'diff', branch_name, "--name-only"]
    result = subprocess.run(command, capture_output=True, text=True)
    # Check if the command was successful
    if result.returncode == 0:
        # Split the output by newlines to get a list of files
        files = result.stdout.strip().split('\n')
        return files
    else:
        # If the command failed, print the error and return an empty list
        print("Error running git diff:", result.stderr)
        return []

def git_diff(branch_name, file_path):
    # Run the git diff command against the specified branch
    command = ['git', 'diff', branch_name, '--', file_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return result.stdout