# Program 4: Degree of Vertices

import networkx as nx

G = nx.Graph()

G.add_edges_from([(1,2),(2,3),(3,4),(4,1)])

for node in G.nodes():
    print("Degree of", node, "=", G.degree(node))