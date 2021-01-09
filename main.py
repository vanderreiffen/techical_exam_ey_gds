import numpy as np
import networkx as nx
import csv
import matplotlib.pyplot as plt
import random

# item 1 on the exam
def load_to_array(csv_file):
    """ Loads CSV to array """
    data = list(csv.reader(open(csv_file)))
    return np.array(data)


def display_graph(G, grid_title = 'Figure 1'):
    """ Load G (grid) customized it according to data types and displays the plot"""
    # initialize graph
    pos = dict((n, n) for n in G.nodes())
    # create labels for nodes
    labels = dict((n, G.nodes[n]['type']) for n in G.nodes())

    # group node types according to list
    type1_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 'x']
    type2_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 'o']
    empty_cells = [n for (n, d) in G.nodes(data=True) if d['type'] == ' ']

    # draw network and label nodes according to type
    nodes_y = nx.draw_networkx_nodes(G, pos, node_color='yellow', nodelist=type1_node_list)
    nodes_b = nx.draw_networkx_nodes(G, pos, node_color='blue', nodelist=type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G, pos, node_color='white', nodelist=empty_cells)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=labels)

    plt.figure(grid_title)
    plt.show()


def get_boundary_nodes(G, max_row, max_col):
    nodes_list = []
    for (x, y) in G.nodes():
        if x == 0 or y == max_row-1 or y == 0 or x == max_col-1:
            nodes_list.append((x, y))
    return nodes_list


def get_neighbor_for_internal(x, y):
    return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y+1) ,(x+1, y-1), (x-1, y-1), (x+1, y+1)]


def get_neighbor_for_boundary(N, u, v):
    if u == 0 and v == 0:
        return [(0, 1), (1, 1), (1, 0)]
    elif u == N-1 and v == N - 1:
        return [(N-2, N-2), (N-1, N-2), (N-2, N-1)]
    elif u == N-1 and v == 0:
        return [(u-1, v), (u, v+1), (u-1, v+1)]
    elif u == 0 and v == N-1:
        return [(u+1, v), (u+1, v-1), (u, v-1)]
    elif u == 0:
        return [(u, v-1), (u, v+1), (u+1, v), (u+1, v-1), (u+1, v+1)]
    elif u == N-1:
        return [(u-1, v), (u, v-1), (u, v+1), (u-1, v+1), (u-1, v-1)]
    elif v == N-1:
        return [(u, v-1), (u-1, v), (u+1, v), (u-1, v-1), (u+1, v-1)]
    elif v == 0:
        return [(u-1, v), (u+1, v), (u, v+1), (u-1, v+1), (u+1, v+1)]


def make_node_satisfied(unsatisfied_nodes_list, empty_cells):
    if len(unsatisfied_nodes_list) != 0:
        node_to_shift = random.choice(unsatisfied_nodes_list)
        new_position = random.choice(empty_cells)

        G.nodes[new_position]['type'] = G.nodes[node_to_shift]['type']
        G.nodes[node_to_shift]['type'] = 0
        labels[node_to_shift], labels[new_position] = labels[new_position], labels[node_to_shift]
    else:
        pass


def get_unsatisfied_nodes_list(G, internal_nodes_list, boundary_nodes_list, threshold):
    unsatisfied_nodes_list = []
    t = threshold
    for (u, v) in G.nodes():
        type_of_this_node = G.nodes[(u, v)]['type']
        if type_of_this_node == 0:
            continue
        else:
            similar_nodes = 0
            if (u, v) in internal_nodes_list:
                neighbors = get_neighbor_for_internal(u,v)
            elif (u, v) in boundary_nodes_list:
                neighbors = get_neighbor_for_boundary(u,v)

            for each in neighbors:
                if G.nodes[each]['type'] == type_of_this_node:
                    similar_nodes += 1

            if similar_nodes <= t:
                unsatisfied_nodes_list.append((u,v))

    return unsatisfied_nodes_list


# item 2
def schelling_model(grid_source, threshold=3):
    """ Shows schelling model """
    numrows = len(grid_source)
    numcols = len(grid_source[0])

    # create grid
    G = nx.grid_2d_graph(numrows, numcols)

    for i, j in G.nodes():
        G.nodes[(i, j)]['type'] = grid_source[i][j]

    # diagonal edges
    for ((x, y), d) in G.nodes(data=True):
        if (x + 1 <= numcols - 1) and (y + 1 <= numrows - 1):
            G.add_edge((x, y), (x + 1, y + 1))
    for ((x, y), d) in G.nodes(data=True):
        if (x + 1 <= numcols - 1) and (y - 1 >= 0):
            G.add_edge((x, y), (x + 1, y - 1))

    # display initial graph
    display_graph(G)

    # get boundary and internal noder
    boundary_nodes_list = get_boundary_nodes(G, numrows, numcols)
    internal_nodes_list = list(set(G.nodes()) - set(boundary_nodes_list))

    # make calculations according to threshold
    # accuracy is based on the number of iterations
    for i in range(10000):
        # get list of unsatisfied not list first
        unsatisfied_nodes_list = get_unsatisfied_nodes_list(G, internal_nodes_list, boundary_nodes_list)
        make_node_satisfied(unsatisfied_nodes_list, empty_cells)

    # display final graph
    display_graph(G)


if __name__ == '__main__':
    input_file = 'test.csv'
    grid = load_to_array(input_file)

    # show schelling model based on 2d grid
    schelling_model(grid)
