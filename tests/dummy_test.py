import networkx as nx

from isomorphic_test import run_isomorphic_test
from utils.utils import ALIVE_COLOR, get_random_graph_one_live_node


def isomorphism_test(graph1: nx.Graph, graph2: nx.Graph) -> bool:

    live_nodes1 = 0
    for node in graph1:
        if graph1.nodes[node]['color'] == ALIVE_COLOR:
            live_nodes1 += 1

    live_nodes2 = 0
    for node in graph2:
        if graph2.nodes[node]['color'] == ALIVE_COLOR:
            live_nodes2 += 1

    return live_nodes1 == live_nodes2


run_isomorphic_test(get_random_graph_one_live_node(5, 0.6), get_random_graph_one_live_node(5, 0.6), isomorphism_test, 1)