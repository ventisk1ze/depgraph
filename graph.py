from typing import List
import networkx as nx
from objects.filedict import FileDict

class Graph:
    def __init__(self, file_dicts: List[FileDict]) -> None:
        self.file_dicts = file_dicts

    @staticmethod
    def create_edges(fd: FileDict) -> List:
        return [(fd['file_name'], i['import_name']) for i in fd['imports']]
    
    def create_graph(self):
        edges = []
        for fd in self.file_dicts:
            edges.extend(self.create_edges(fd))
        self.graph = nx.DiGraph(edges)
        return self.graph