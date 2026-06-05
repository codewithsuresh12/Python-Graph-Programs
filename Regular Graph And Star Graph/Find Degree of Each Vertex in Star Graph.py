import networkx as nx

G = nx.star_graph(5)

for node in G.nodes():
    print("Vertex", node, "Degree =", G.degree(node))