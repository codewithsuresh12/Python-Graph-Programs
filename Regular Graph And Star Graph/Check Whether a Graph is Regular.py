import networkx as nx

G = nx.cycle_graph(6)

degrees = [G.degree(v) for v in G.nodes()]

if len(set(degrees)) == 1:
    print("Regular Graph")
else:
    print("Not a Regular Graph")