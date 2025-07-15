import networkx as nx


G = nx.Graph()
G.add_edge("A", "B", weight=3)
G.add_edge("A", "market", weight=6)
G.add_edge("B", "D", weight=2)
G.add_edge("B", "bakery", weight=5)
G.add_edge("C", "D", weight=4)
G.add_edge("C", "market", weight=1)
G.add_edge("D", "bakery", weight=1)


def shortest_path(route):
    path_final = []
    for i in range(len(route)-1):
        path = nx.dijkstra_path(G, route[i], route[i + 1])
        path_final = path_final + path
    return path_final

route = ["A", "market", "bakery", "A"]

print(shortest_path(route))
