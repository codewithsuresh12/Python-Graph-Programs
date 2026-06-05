# Program 7: BFS Traversal

import networkx as nx

G = nx.Graph()

G.add_edges_from([
    (1,2),
    (1,3),
    (2,4),
    (3,5)
])

bfs = list(nx.bfs_tree(G, source=1))

print("BFS Traversal:")
print(bfs)