import toml
from urllib import request

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_object = toml.loads(content)["tool"]["poetry"]

        name = toml_object["name"]
        description = toml_object["description"]
        dependencies = toml_object["dependencies"]
        dev_dependencies = toml_object["dev-dependencies"]

        project = Project(
            name,
            description,
            dependencies,
            dev_dependencies
        )

        return project
