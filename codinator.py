from lib.reader import read_spec_from_yaml
from lib.git import git_diff, git_changed_files
from lib.util import filter_files_by_type
from lib.openai import get_openai_response
import argparse
import os
import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Codinator - Code Review Automation")
    parser.add_argument("--filepath", type=str, help="Path to the spec file")
    args = parser.parse_args()

    logging.debug("Running Codinator...")
    # use arg parse for file path
    filepath = args.filepath or os.environ.get("SPEC_FILE_PATH") or '.codinator-spec-sample'
    spec = read_spec_from_yaml(filepath)
    if not spec.requirements:
        logging.debug("No requirements specified. Exiting...")
        return

    requirements_text = "\n".join(f"- {req}" for req in spec.requirements)
    logging.debug(f'Code Review Requirements:\n{requirements_text}')

    changed_files = git_changed_files(spec.default_branch)
    files_to_be_checked = filter_files_by_type(changed_files, spec.files_types)
    if not files_to_be_checked:
        print("##### Codinator review complete! :sparkles")
        logging.debug("No files to be checked. Exiting...")
        return

    logging.debug('Reviewing changes to the following files: \n%s',
                  '\n'.join(files_to_be_checked))

    for file in files_to_be_checked:
        print(f"#### ------------- {file} -------------")
        file_diff = git_diff(spec.default_branch, file)
        print(f"{get_openai_response(requirements_text, file_diff)}\n\n")

if __name__ == '__main__':
    main()