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
        self.matrix_size = matrix_size
        self.G = nx.grid_2d_graph(matrix_size, matrix_size)
        self.pos = dict((n, n) for n in self.G.nodes())
        self.labels = dict(((i, j), i * 10 + j) for i, j in self.G.nodes())

    def display_graph(self):
        pass

    def calculate(self):
        pass


if __name__ == '__main__':
    pass
