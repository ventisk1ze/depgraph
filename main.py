import json
from project import Project
from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

p = Project(r'C:\Users\User\Desktop\Programming\pm4py-core', debug=False)

g = Graph(p.get_imports())

nx.draw(g.create_graph(), with_labels=True)
plt.show()