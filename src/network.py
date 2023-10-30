import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([
    (1, {"type": "School"}),
    (2, {"type": "Road"}),
    (3, {"type": "Road"}),
    (4, {"type": "Road"}),
    (5, {"type": "Road"}),
    (6, {"type": "Library"}),
    (7, {"type": "Road"}),
    (8, {"type": "Road"}),
    (9, {"type": "Road"}),
    (10, {"type": "Road"}),
    (11, {"type": "Cinema"}),
    (12, {"type": "Road"}),
    (13, {"type": "Road"}),
    (14, {"type": "Bus Station"}),
    (15, {"type": "Road"}),
    (16, {"type": "Road"}),
    (17, {"type": "Parc"}),
    (18, {"type": "Parc"}),
    (19, {"type": "Parc"}),
    (20, {"type": "Road"}),
    (21, {"type": "Road"}),
    (22, {"type": "Road"}),
    (23, {"type": "School"}),
    (24, {"type": "Road"}),
    (25, {"type": "Road"}),
    (26, {"type": "Road"}),
    (27, {"type": "Post Office"}),
    (28, {"type": "Road"}),
    (29, {"type": "Road"}),
    (30, {"type": "Bus Station 2"}),
    (31, {"type": "Road"}),
    (32, {"type": "Mall"}),
    (33, {"type": "Road"}),
    (34, {"type": "Road"}),
    (35, {"type": "Road"}),
    (36, {"type": "Road"}),
    (37, {"type": "Road"}),
    (38, {"type": "Home"}),
])

G.add_edges_from([
    (1, 2), # School
    (2, 3), (3, 4), (4, 5), # School 1 to Library
    (5, 6), (5, 7), # Library
    (7, 8), (8, 9), (9, 10), # Library to Cinema
    (9, 17), #  Parc Entry
    (17, 18), (18, 19), (19, 16), # Parc
    (10, 11), (10, 12), # Cinema
    (12, 13), # Cinema to Bus Station 1
    (13, 14), (13, 15), # Bus Station 1
    (15, 16), (16, 20), (20, 21), (21, 22), # Bus Station 1 to School 2
    (22, 23), # School 2
    (20, 24),
    (24, 25),
    (25, 26),
    (26, 27), (26, 28),
    (28, 29),
    (29, 30), (29, 31),
    (24, 32),
    (32, 33), (32, 34),
    (34, 35),
    (35, 36),
    (36, 37),
    (37, 38)
    ])

print(list(G.nodes))
print(list(G.edges))
print(list(G.adjacency()))
print(nx.astar_path(G, 1, 8))

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()  