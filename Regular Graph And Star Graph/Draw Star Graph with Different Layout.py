import networkx as nx
import matplotlib.pyplot as plt

G = nx.star_graph(6)

pos = nx.circular_layout(G)

nx.draw(G, pos, with_labels=True)

plt.title("Star Graph - Circular Layout")
plt.show()