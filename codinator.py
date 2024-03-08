from lib.reader import read_spec_from_yaml
from lib.git import git_diff, git_changed_files
from lib.util import filter_files_by_type
from lib.openai import get_openai_response
import os
import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.debug("Running Codinator...")
    filepath = os.environ.get("SPEC_FILE_PATH") or '.codinator-spec-sample'
    spec = read_spec_from_yaml(filepath)
    if not spec.requirements:
        logging.debug("No requirements specified. Exiting...")
        return

    requirements_text = "\n".join(f"- {req}" for req in spec.requirements)
    logging.debug(f'Code Review Requirements:\n{requirements_text}')

    changed_files = git_changed_files(spec.default_branch)
    # print the changed files array into line by line

    files_to_be_checked = filter_files_by_type(changed_files, spec.files_types)
    if not files_to_be_checked:
        logging.debug("No files to be checked. Exiting...")
        return

    logging.debug(f"Files to be reviewed:'\n'.join(files_to_be_checked)")

    for file in files_to_be_checked:
        print(f"** ------------- {file} ------------- **:")
        file_diff = git_diff(spec.default_branch, file)
        print(f"{get_openai_response(requirements_text, file_diff)}\n\n")

if __name__ == '__main__':
    main()