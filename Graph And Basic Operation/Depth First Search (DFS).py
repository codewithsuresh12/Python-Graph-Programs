# Program 8: DFS Traversal

import networkx as nx

G = nx.Graph()

G.add_edges_from([
    (1,2),
    (1,3),
    (2,4),
    (3,5)
])

dfs = list(nx.dfs_tree(G, source=1))

print("DFS Traversal:")
print(dfs)