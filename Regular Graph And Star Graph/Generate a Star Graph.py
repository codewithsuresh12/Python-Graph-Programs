import networkx as nx
import matplotlib.pyplot as plt

G = nx.star_graph(5)

nx.draw(G, with_labels=True)

plt.title("Star Graph")
plt.show()