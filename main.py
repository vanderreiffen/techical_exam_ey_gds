import numpy as np
import networkx as nx
import csv
import matplotlib.pyplot as plt
import random

from loguru import logger


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

    plt.suptitle(grid_title)
    plt.show()


def get_boundary_nodes(G, max_row, max_col):
    nodes_list = []
    for (x, y) in G.nodes():
        if x == 0 or y == max_row-1 or y == 0 or x == max_col-1:
            nodes_list.append((x, y))
    return nodes_list


def get_neighbor_for_internal(x, y):
    """ returns a list of neighbor nodes within the internal nodes """
    return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y+1), (x+1, y-1), (x-1, y-1), (x+1, y+1)]


def get_neighbor_for_boundary(x, y, numrows, numcols):
    """ returns a list of neighbor nodes within the boundary nodes """
    if x == 0 and y == 0:
        return [(0, 1), (1, 1), (1, 0)]
    elif x == numcols-1 and y == numrows - 1:
        return [(numrows-2, numcols-2), (numrows-1, numcols-2), (numrows-2, numcols-1)]
    elif x == numcols-1 and y == 0:
        return [(x-1, y), (x, y+1), (x-1, y+1)]
    elif x == 0 and y == numrows-1:
        return [(x+1, y), (x+1, y-1), (x, y-1)]
    elif x == 0:
        return [(x, y-1), (x, y+1), (x+1, y), (x+1, y-1), (x+1, y+1)]
    elif x == numcols-1:
        return [(x-1, y), (x, y-1), (x, y+1), (x-1, y+1), (x-1, y-1)]
    elif y == numrows-1:
        return [(x, y-1), (x-1, y), (x+1, y), (x-1, y-1), (x+1, y-1)]
    elif y == 0:
        return [(x-1, y), (x+1, y), (x, y+1), (x-1, y+1), (x+1, y+1)]


def make_node_satisfied(G, unsatisfied_nodes_list, empty_cells):
    labels = dict((n, G.nodes[n]['type']) for n in G.nodes())
    if len(unsatisfied_nodes_list) != 0:
        # choose from the random unsatisfied nodes
        node_to_shift = random.choice(unsatisfied_nodes_list)
        # choose a random empty cell
        new_position = random.choice(empty_cells)

        # move the unsatisfied node to the empty cell and switch values
        G.nodes[new_position]['type'] = G.nodes[node_to_shift]['type']
        # make the previous node empty
        G.nodes[node_to_shift]['type'] = ' '
        labels[node_to_shift], labels[new_position] = labels[new_position], labels[node_to_shift]
    else:
        pass


def get_unsatisfied_nodes_list(G, internal_nodes_list, boundary_nodes_list, threshold, numrows, numcols):
    """ returns the list of unsatisfied nodes """
    unsatisfied_nodes_list = []
    t = threshold
    for (x, y) in G.nodes():
        type_of_this_node = G.nodes[(x, y)]['type']
        if type_of_this_node == 0:
            continue
        else:
            similar_nodes = 0
            if (x, y) in internal_nodes_list:
                neighbors = get_neighbor_for_internal(x, y)
            elif (x, y) in boundary_nodes_list:
                neighbors = get_neighbor_for_boundary(x, y, numrows, numcols)

            for each in neighbors:
                if G.nodes[each]['type'] == type_of_this_node:
                    similar_nodes += 1

            if similar_nodes <= t:
                unsatisfied_nodes_list.append((x, y))

    return unsatisfied_nodes_list


# item 3
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
    display_graph(G, 'Initial Grid (Please close to continue)')

    # get boundary and internal noder
    boundary_nodes_list = get_boundary_nodes(G, numrows, numcols)
    internal_nodes_list = list(set(G.nodes()) - set(boundary_nodes_list))

    # make calculations according to threshold
    # accuracy is based on the number of iterations
    for i in range(10000):
        # get list of unsatisfied not list first
        unsatisfied_nodes_list = get_unsatisfied_nodes_list(G, internal_nodes_list, boundary_nodes_list, threshold, numrows, numcols)

        # move an unsatisfied node to an empty cell
        logger.info("iteration : {}".format(i))
        empty_cells = [n for (n, d) in G.nodes(data=True) if d['type'] == ' ']
        make_node_satisfied(G, unsatisfied_nodes_list, empty_cells)
    # display final graph
    display_graph(G, 'Output Grid')


if __name__ == '__main__':


    input_file = 'test.csv'
    grid = load_to_array(input_file)

    # show schelling model based on 2d grid
    schelling_model(grid)
