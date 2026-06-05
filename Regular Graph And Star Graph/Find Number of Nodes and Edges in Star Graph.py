import networkx as nx

G = nx.star_graph(5)

print("Vertices =", G.number_of_nodes())
print("Edges =", G.number_of_edges())