def filter_files_by_type(changed_files, file_types):
    return [file for file in changed_files if any(file.endswith(file_type) for file_type in file_types)]
