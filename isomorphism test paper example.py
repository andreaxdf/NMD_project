import time
import random

import networkx as nx
import matplotlib.pyplot as plt

ALIVE_COLOR = "green"
DEAD_COLOR = "red"


def isomorphism_test(graph1, graph2, list1, list2, color1, color2):
    isomorphism = False
    list_info1 = []
    list_info2 = []

    num_node = 0
    for node in graph1:
        alive = 0
        near = 0
        for index in range(5):
            if num_node != index and graph1.has_edge(node, list1[index]) and color1[index] == ALIVE_COLOR:
                near += 1
                alive += 1
            elif num_node != index and graph1.has_edge(node, list1[index]) and color1[index] == DEAD_COLOR:
                near += 1
        state = color1[num_node]
        tuple_info = (node, state, alive, near)
        list_info1.append(tuple_info)
        num_node += 1

    num_node = 0
    for node in graph2:
        alive = 0
        near = 0
        for index in range(5):  # node 2 num_node 1 index 0 color white
            if num_node != index and graph2.has_edge(node, list2[index]) and color2[index] == ALIVE_COLOR:
                near += 1
                alive += 1
            elif num_node != index and graph2.has_edge(node, list2[index]) and color2[index] == DEAD_COLOR:
                near += 1
        state = color2[num_node]
        tuple_info = (node, state, alive, near)
        list_info2.append(tuple_info)
        num_node += 1

    list0 = []
    index2 = 0
    for index1 in range(len(list_info1)):
        couple1 = list_info1[0]
        for couple2 in list_info2:
            if couple1[1] == couple2[1] and couple1[2] == couple2[2] and couple1[3] == couple2[3]:
                couple = (couple1[0], couple2[0])
                list0.append(couple)
                list_info1.pop(0)
                list_info2.pop(index2)
                index1 = 0
                index2 = 0
                break
            else:
                index2 += 1

    if len(list_info1) == 0:
        isomorphism = True

    return isomorphism


def game_iteration(graph, node_list, color):
    colornew = []
    position = 0

    for node in graph:
        alive = 0
        near = 0
        for neighbour in range(graph.number_of_nodes()):
            if position != neighbour and graph.has_edge(node, node_list[neighbour]) and color[neighbour] == ALIVE_COLOR:
                near += 1
                alive += 1
            elif position != neighbour and graph.has_edge(node, node_list[neighbour]) and color[
                neighbour] == DEAD_COLOR:
                near += 1

        if color[position] == ALIVE_COLOR and 1 <= alive < near:
            colornew.append(ALIVE_COLOR)
        elif color[position] == DEAD_COLOR and alive == 1:
            colornew.append(ALIVE_COLOR)
        else:
            colornew.append(DEAD_COLOR)
        position += 1

    return colornew


def example(graph1, graph2):
    list1 = []
    list2 = []
    for node in graph1:
        list1.append(node)
    for node in graph2:
        list2.append(node)

    color1 = [data['color'] for v, data in graph1.nodes(data=True)]
    color2 = [data['color'] for v, data in graph2.nodes(data=True)]
    # nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
    # plt.title("Graph1")
    # plt.show()
    # nx.draw(graph2, with_labels=True, node_color=color2, node_size=800, edge_color='black')
    # plt.title("Graph2")
    # plt.show()

    for step in range(3):
        is_isomorphic = isomorphism_test(graph1, graph2, list1, list2, color1, color2)
        print(is_isomorphic)
        first = game_iteration(graph1, list1, color1)
        color1 = first
        second = game_iteration(graph2, list2, color2)
        color2 = second
        # nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
        # plt.title("Graph1")
        # plt.show()
        # nx.draw(graph2, with_labels=True, node_color=color2, node_size=800, edge_color='black')
        # plt.title("Graph2")
        # plt.show()
        step += 1


def get_erdos_renyi_graph(num_nodes: int, p: float, alive_threshold: float):
    graph = nx.erdos_renyi_graph(num_nodes, p)

    for node in graph:

        if random.random() > alive_threshold:
            graph.nodes[node]['color'] = ALIVE_COLOR
        else:
            graph.nodes[node]['color'] = DEAD_COLOR

    return graph
