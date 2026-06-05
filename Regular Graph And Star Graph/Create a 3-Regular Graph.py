import networkx as nx
import matplotlib.pyplot as plt

G = nx.random_regular_graph(3, 8)

nx.draw(G, with_labels=True)

plt.title("3-Regular Graph")
plt.show()