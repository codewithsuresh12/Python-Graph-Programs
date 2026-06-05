import networkx as nx

G = nx.star_graph(5)

center = max(G.degree(), key=lambda x: x[1])

print("Center Vertex =", center[0])