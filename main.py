import numpy as np
import networkx as nx
import csv
import matplotlib.pyplot as plt
import random


def load_to_array(csv_file):
    data = list(csv.reader(open(csv_file)))
    return np.array(data)


class BaseModel:
    def __init__(self, matrix_size):
        # initialize graph
        self.matrix_size = matrix_size
        self.G = nx.grid_2d_graph(matrix_size, matrix_size)
        self.pos = dict((n, n) for n in self.G.nodes())

        # randomize nodes
        for n in self.G.nodes():
            self.G.nodes[n]['type'] = random.randint(0, 2)

        self.labels = dict((n, 'X' if self.G.nodes[n]['type'] == 1 else 'O') for n in self.G.nodes())

        self.type1_node_list = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 1]
        self.type2_node_list = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 2]
        self.empty_cells = [n for (n, d) in self.G.nodes(data=True) if d['type'] == 0]

    def display_graph(self):
        nodes_y = nx.draw_networkx_nodes(self.G, self.pos, node_color='yellow', nodelist=self.type1_node_list)
        nodes_b = nx.draw_networkx_nodes(self.G, self.pos, node_color='blue', nodelist=self.type2_node_list)
        nodes_w = nx.draw_networkx_nodes(self.G, self.pos, node_color='white', nodelist=self.empty_cells)

        # nx.draw(self.G, self.pos, with_labels=False)
        nx.draw_networkx_edges(self.G, self.pos)
        nx.draw_networkx_labels(self.G, self.pos, labels=self.labels)
        plt.show()

    def _calculate(self):
        pass


class Schelling(BaseModel):
    # def _
    def _calculate(self):
        pass


if __name__ == '__main__':
    schelling = Schelling(20)
    schelling.display_graph()
