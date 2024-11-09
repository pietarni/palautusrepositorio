class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_arr(self, arr):
        return "\n - " + "\n - ".join(arr) if len(arr) > 0 else "-"

    def __str__(self):
        return (
            f"\nName: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_arr(self.authors)}"
            f"\n\nDependencies: {self._stringify_arr(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_arr(self.dev_dependencies)}"
        )
