# Program 6: Connected Graph

import networkx as nx

G = nx.Graph()

G.add_edges_from([(1,2),(2,3),(3,4)])

if nx.is_connected(G):
    print("Graph is Connected")
else:
    print("Graph is Not Connected")