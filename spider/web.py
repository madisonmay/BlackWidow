import os

from spider.node import Node


class Web(object):
    """
    The full project web.  
    Contains a list of nodes.
    """

    def __init__(self, package_root, exclude=None):
        files = find_files(package_root, exclude=exclude)
        self.package_root = package_root
        self.nodes = [
            Node(file, package_root=self.package_root) for file in files
        ]


def find_files(dir, exclude=None):
    """
    Given a root directory, compiles a list of python files to analyze.
    If a discovered python file is provided in the list of excluded, it will be ignored
    """
    if not exclude:
        exclude = []

    matches = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py") and not file in exclude:
                matches.append(
                    os.path.abspath(os.path.join(root, file))
                )

    return matches


if __name__ == "__main__":
    web = Web('/home/m/Indico/IndicoApi/indicoapi')
    print web.package_root
