import math
import random

import networkx as nx

ALIVE_COLOR = "green"
DEAD_COLOR = "red"


def color_graph(graph: nx.Graph):
    for node in graph:
        graph.nodes[node]['color'] = DEAD_COLOR

    nodes = len(graph)

    random_node = math.floor(random.random() * nodes)

    graph.nodes[random_node]['color'] = ALIVE_COLOR

    return graph


def get_random_graph_one_live_node(num_nodes: int, p: float):
    graph = nx.erdos_renyi_graph(num_nodes, p)

    return color_graph(graph)


def get_erdos_renyi_graph(num_nodes: int, p: float, alive_threshold: float):
    graph = nx.erdos_renyi_graph(num_nodes, p)

    for node in graph:

        if random.random() > alive_threshold:
            graph.nodes[node]['color'] = ALIVE_COLOR
        else:
            graph.nodes[node]['color'] = DEAD_COLOR

    return graph
