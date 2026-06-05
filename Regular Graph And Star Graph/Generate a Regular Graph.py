import networkx as nx
import matplotlib.pyplot as plt

G = nx.random_regular_graph(2, 6)

nx.draw(G, with_labels=True)

plt.title("2-Regular Graph")
plt.show()