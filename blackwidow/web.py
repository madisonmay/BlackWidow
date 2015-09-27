import os
import json
import re
from functools import partial   
from fnmatch import fnmatch

import networkx as nx
from networkx.readwrite import json_graph

import blackwidow.config as config
from blackwidow.node import Node
from blackwidow.viz.server import serve
from blackwidow.imports import import_path


class Web(object):
    """
    The full project web.  
    Contains the package root and list of nodes.
    """

    def __init__(self, package_root, exclude=None):
        self.files = find_files(package_root, exclude=exclude)
        self.package_root = package_root
        self.module = import_path(package_root, os.path.dirname(package_root)) 
        self.nodes = [
            Node(file, package_root=self.package_root) for file in self.files
        ]

        package_import_path = partial(import_path, package_root=os.path.dirname(package_root))
        self.package_modules = set(map(package_import_path, self.files))

        self.graph = nx.Graph()

        for node in self.nodes:
            if node.module not in self.package_modules:
                continue
            self.graph.add_node(node.module)
            self.graph.node[node.module]['name'] = node.module

            for module in node.imports:
                module = self._package_module(module)
                if module in self.package_modules:
                    self.graph.add_edge(node.module, module)

    def _package_module(self, module):
        if not module.startswith(self.module):
            module = ".".join([self.module, module])
        return module


    def visualize(self, port=None):
        """
        Dumps graph data to a json file and renders using d3's force-directed graph
        """
        json_data = json_graph.node_link_data(self.graph)
        json_data['package_name'] = self.module

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
            filepath = os.path.abspath(os.path.join(root, file))
            if any(fnmatch(filepath, pattern) for pattern in exclude):
                continue

            if filepath.endswith(".py"):
                matches.append(filepath)

    return matches


if __name__ == "__main__":
    import os, sys, argparse

    parser = argparse.ArgumentParser(description='Visualize Python Project Imports')
    parser.add_argument('package', help='name of python package to analyze')
    parser.add_argument(
        '--exclude', nargs='+', metavar="pattern", 
        help='list of files patterns to exclude'
    )
    args = parser.parse_args()

    package_name = args.package 
    package = __import__(package_name)
    if "__init__" not in package.__file__:
        raise ValueError('Not a package: %s' % package_name)
    project_path = os.path.dirname(package.__file__)

    web = Web(project_path, exclude=args.exclude)
    web.visualize()
