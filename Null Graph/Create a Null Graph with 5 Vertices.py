# Q1. Create a Null Graph with 5 Vertices

import networkx as nx
import matplotlib.pyplot as plt

G = nx.empty_graph(5)

nx.draw(G, with_labels=True,node_color="red",node_size=700)
plt.show()