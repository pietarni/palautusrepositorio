from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        poetry = data["tool"]["poetry"]
        group_dev_dependencies = poetry["group"]["dev"]["dependencies"]
        
        return Project(
            poetry["name"],
            poetry["description"],
            poetry["license"],
            poetry["authors"],
            poetry["dependencies"],
            group_dev_dependencies
        )