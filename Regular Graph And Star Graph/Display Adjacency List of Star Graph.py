import networkx as nx

G = nx.star_graph(5)

for node in G.adj:
    print(node, "->", list(G.adj[node]))