import json
from project import Project
from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

p = Project(r'C:\Users\User\Desktop\Programming\rosreestr2coord\rosreestr2coord', debug=False)

g = Graph(p.get_imports()).create_graph()


color_map = ['red' if node in p.import_names else 'blue' for node in list(g.nodes().keys())]


nx.draw_kamada_kawai(g, with_labels=True, node_size=1000, node_color=color_map)

with open('imports.txt', 'w+', encoding='utf-8') as f:
    print(*p.import_names, sep='\n', file=f)

plt.show()