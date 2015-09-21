import os
import ast
import itertools

from blackwidow.error import BlackWidowIOError, BlackWidowValueError
from blackwidow.imports import Import, import_path, imported_modules


class Node(object):
    """
    A node in the python project graph.
    Contains a list of outgoing edges.
    """

    def __init__(self, filename, package_root=None):
        if not package_root:
            raise BlackWidowValueError("No 'package_root' specified.")
        self.filename = filename
        self.package_root = package_root
        self.module = import_path(filename, os.path.dirname(package_root))
        self.edges = imported_modules(filename, package_root=package_root)
        self.imports = list(itertools.chain(*[edge.imports for edge in self.edges]))
