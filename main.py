import numpy as np
import networkx as nx
import csv
import matplotlib.pyplot as plt
import random


def load_to_array(csv_file):
    data = list(csv.reader(open(csv_file)))
    return np.array(data)


# class BaseModel:
#     def __init__(self, matrix_size):
#         # initialize graph
#         self.matrix_size = matrix_size
#         self.G = nx.grid_2d_graph(matrix_size, matrix_size)
#         self.pos = dict((n, n) for n in self.G.nodes())
#
#         # randomize nodes
#         for n in self.G.nodes():
#             self.G.nodes[n]['type'] = random.randint(0, 2)
#
#         self.labels = dict((n, 'X' if self.G.nodes[n]['type'] == 1 else 'O') for n in self.G.nodes())
#
#         self.type1_node_list = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 1]
#         self.type2_node_list = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 2]
#         self.empty_cells = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 0]
#
#         self.boundary_nodes_list = self._get_boundary_nodes(self.G)
#         self.internal_nodes_list = list(set(self.G.nodes()) - set(self.boundary_nodes_list))
#
#     def display_graph(self):
#         nodes_y = nx.draw_networkx_nodes(self.G, self.pos, node_color='yellow', nodelist=self.type1_node_list)
#         nodes_b = nx.draw_networkx_nodes(self.G, self.pos, node_color='blue', nodelist=self.type2_node_list)
#         nodes_w = nx.draw_networkx_nodes(self.G, self.pos, node_color='white', nodelist=self.empty_cells)
#
#         # nx.draw(self.G, self.pos, with_labels=False)
#         nx.draw_networkx_edges(self.G, self.pos)
#         nx.draw_networkx_labels(self.G, self.pos, labels=self.labels)
#         plt.show()
#
#     def _get_boundary_nodes(self):
#         nodes_list = []
#         for (u, v) in self.G.nodes():
#             if u == 0 or u == N - 1 or v == 0 or v == N - 1:
#                 nodes_list.append((u, v))
#         return nodes_list
#
#     def _get_neighbor_for_internal(self, x, y):
#         return [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1),
#                 (x + 1, y + 1)]
#
#     def get_neighbor_for_boundary(u, v):
#         if u == 0 and v == 0:
#             return [(0, 1), (1, 1), (1, 0)]
#         elif u == N - 1 and v == N - 1:
#             return [(N - 2, N - 2), (N - 1, N - 2), (N - 2, N - 1)]
#         elif u == N - 1 and v == 0:
#             return [(u - 1, v), (u, v + 1), (u - 1, v + 1)]
#         elif u == 0 and v == N - 1:
#             return [(u + 1, v), (u + 1, v - 1), (u, v - 1)]
#         elif u == 0:
#             return [(u, v - 1), (u, v + 1), (u + 1, v), (u + 1, v - 1), (u + 1, v + 1)]
#         elif u == N - 1:
#             return [(u - 1, v), (u, v - 1), (u, v + 1), (u - 1, v + 1), (u - 1, v - 1)]
#         elif v == N - 1:
#             return [(u, v - 1), (u - 1, v), (u + 1, v), (u - 1, v - 1), (u + 1, v - 1)]
#         elif v == 0:
#             return [(u - 1, v), (u + 1, v), (u, v + 1), (u - 1, v + 1), (u + 1, v + 1)]
#
#     def _calculate(self):
#         pass
#
#
# class Schelling(BaseModel):
#     # def _
#     def _calculate(self):
#         pass


def display_graph(G):
    nodes_y = nx.draw_networkx_nodes(G, pos, node_color='yellow', nodelist=type1_node_list)
    nodes_b = nx.draw_networkx_nodes(G, pos, node_color='blue', nodelist=type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G, pos, node_color='white', nodelist=empty_cells)

    # nx.draw(G, pos, with_labels=False)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.show()


def get_boundary_nodes(G):
    nodes_list = []
    for (u, v) in G.nodes():
        if u == 0 or u == N-1 or v == 0 or v == N-1:
            nodes_list.append((u,v))
    return nodes_list


def get_neighbor_for_internal(x, y):
    return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y+1) ,(x+1, y-1), (x-1, y-1), (x+1, y+1)]

def schelling_model(grid_source):
    numrows = len(grid_source)
    numcols = len(grid_source[0])

    G = nx.grid_2d_graph(numrows, numcols)
    pos = dict((n, n) for n in G.nodes())

    for n in G.nodes():
        G.nodes[n]['type'] = random.randint(0, 2)

    # create labels for nodes
    labels = dict((n, G.nodes[n]['type']) for n in G.nodes())




if __name__ == '__main__':
    schelling = Schelling(20)
    schelling.display_graph()
