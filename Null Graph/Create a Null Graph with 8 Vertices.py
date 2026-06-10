# Q2. Create a Null Graph with 8 Vertices

import networkx as nx
import matplotlib.pyplot as plt

G = nx.empty_graph(8)

nx.draw(G, with_labels=True)
plt.show()