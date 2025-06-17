import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["Hauptbahnhof", "Willy-Brandt-Platz", "Konstablerwache", "Höchst", "Galluswarte", "Bockenheimer Warte", "Bornheim Mitte", "Südbahnhof", "Ostendstraße", "Frankfurt West"]
G.add_nodes_from(nodes)

edges = [
    ("Hauptbahnhof", "Willy-Brandt-Platz", 2), ("Willy-Brandt-Platz", "Konstablerwache", 3),
    ("Konstablerwache", "Ostendstraße", 2), ("Hauptbahnhof", "Galluswarte", 2),
    ("Galluswarte", "Frankfurt West", 3), ("Frankfurt West", "Bockenheimer Warte", 2),
    ("Bockenheimer Warte", "Bornheim Mitte", 4), ("Bornheim Mitte", "Konstablerwache", 3),
    ("Hauptbahnhof", "Südbahnhof", 5), ("Hauptbahnhof", "Höchst", 6)
]
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Frankfurt am Main Metro and Train Map")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_sequence = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Node degrees:")
for node, degree in degree_sequence.items():
    print(f"  Station {node}: {degree}")