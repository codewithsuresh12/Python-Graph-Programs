# Program 1: Generate a Simple Graph

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

nx.draw(G, with_labels=True)

plt.title("Simple Undirected Graph")
plt.show()