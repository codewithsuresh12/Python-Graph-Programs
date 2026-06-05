import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.star_graph(5)
G2 = nx.cycle_graph(6)

plt.figure(figsize=(10,5))

plt.subplot(121)
nx.draw(G1, with_labels=True)
plt.title("Star Graph")

plt.subplot(122)
nx.draw(G2, with_labels=True)
plt.title("Regular Graph")

plt.show()