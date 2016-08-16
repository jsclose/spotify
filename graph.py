import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])
G.add_edge(1,3, color = 'red')

#nx.draw(G)
nx.draw(G)

plt.show()