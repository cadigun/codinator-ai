import yaml
class Specification:
    def __init__(self, name, files_types, default_branch, requirements):
        self.name = name
        self.files_types = files_types
        self.default_branch = default_branch
        self.requirements = requirements

def read_spec_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        project = data['project']
        spec = Specification(
            name=project['name'],
            files_types=project['files_types'],
            default_branch=project['default_branch'],
            requirements=project['requirements']
        )
        return spec