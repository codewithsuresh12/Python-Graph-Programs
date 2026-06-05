# Program 3: Number of Nodes and Edges

import networkx as nx

G = nx.Graph()

G.add_edges_from([(1,2),(2,3),(3,4),(4,1)])

print("Total Nodes =", G.number_of_nodes())
print("Total Edges =", G.number_of_edges())