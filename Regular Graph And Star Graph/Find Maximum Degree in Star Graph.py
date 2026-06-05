import networkx as nx

G = nx.star_graph(5)

vertex = max(G.degree(), key=lambda x: x[1])

print("Vertex =", vertex[0])
print("Maximum Degree =", vertex[1])