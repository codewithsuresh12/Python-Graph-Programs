# Program 5: Adjacency List

import networkx as nx

G = nx.Graph()

G.add_edges_from([(1,2),(1,3),(2,4)])

for node in G.adj:
    print(node, "->", list(G.adj[node]))