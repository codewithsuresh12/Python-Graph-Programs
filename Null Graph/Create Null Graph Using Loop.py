# Q4. Create Null Graph Using Loop

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for i in range(5):
    G.add_node(i)

nx.draw(G, with_labels=True)
plt.show()