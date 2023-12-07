import math
from datetime import datetime
from project import Project
from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx
import argparse

parser = argparse.ArgumentParser(
    prog='Depgraph v0.0.1',
    description='This module creates graph of project dependencies',
    epilog='That`s all, folks!'
)

parser.add_argument('project', help='Path to project')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-l', '--logging', action='store_true')

args = parser.parse_args()

start = datetime.now()
print(f'Started processing at {start}')

p = Project(args.project, debug=args.debug)
print(f'Collected imports in {datetime.now() - start}')

g = Graph(p.get_imports()).create_graph()
print(f'Created nx graph in {datetime.now() - start}')

color_map = ['red' if node in p.import_names else 'blue' for node in g.nodes().keys()]

nx.draw(g, pos=nx.spring_layout(g, k=10/math.sqrt(g.order())), with_labels=True, node_size=1000, node_color=color_map)
print(f'Drew the graph in {datetime.now() - start}')

plt.show()