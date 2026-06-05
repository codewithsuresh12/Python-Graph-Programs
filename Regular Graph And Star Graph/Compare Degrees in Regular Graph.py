import networkx as nx

G = nx.cycle_graph(6)

for node in G.nodes():
    print("Vertex", node, "Degree =", G.degree(node))