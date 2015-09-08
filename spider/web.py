import os
import json

import networkx as nx
from networkx.readwrite import json_graph

import spider.config as config
from spider.node import Node
from spider.viz.server import serve


class Web(object):
    """
    The full project web.  
    Contains the package root and list of nodes.
    """

    def __init__(self, package_root, exclude=None):
        files = find_files(package_root, exclude=exclude)
        self.package_root = package_root
        self.nodes = [
            Node(file, package_root=self.package_root) for file in files
        ]

        self.graph = nx.Graph()

        for node in self.nodes:
            self.graph.add_node(node.module)
            self.graph.node[node.module]['name'] = node.module

        for node in self.nodes:
            for module in node.imports:
                self.graph.add_edge(node.module, module)

    def visualize(self, port=None):
        """
        Dumps graph data to a json file and renders using d3's force-directed graph
        """
        json_data = json_graph.node_link_data(self.graph)

        parent_dir = os.path.abspath(os.path.dirname(__file__))
        viz_dir = os.path.join(parent_dir, 'viz', 'static')
        json_file = os.path.join(viz_dir, 'graph.json')
        html_file = os.path.join(viz_dir, 'graph.html')
        relative_path = os.path.relpath(html_file, viz_dir)

        with open(json_file, 'w') as fd:
            json.dump(json_data, fd)

        if not port:
            port = config.PORT

        serve(directory=viz_dir, filename=relative_path, port=port)


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
    import sys
    path = sys.argv[1]
    web = Web(path)
    web.visualize()
