import networkx as nx

from isomorphic_test import run_isomorphic_test
from utils.utils import get_random_graph_one_live_node, ALIVE_COLOR, DEAD_COLOR


# This test check if, for each node in the first graph, is present a corresponding node in the second graph with the same number of alive neighbours.
def isomorphism_test(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    live_nodes = {}
    for node in graph1:
        live_count = 0
        for adj in graph1.neighbors(node):
            if graph1.nodes[adj]['color'] == ALIVE_COLOR:
                live_count += 1
        if live_count not in live_nodes.keys():
            live_nodes[live_count] = 0
        live_nodes[live_count] += 1

    for node in graph2:
        live_count = 0
        for adj in graph2.neighbors(node):
            if graph2.nodes[adj]['color'] == ALIVE_COLOR:
                live_count += 1
        if live_count not in live_nodes.keys():
            # There is no node with your number of live neighbors
            return False
        live_nodes[live_count] -= 1

    for key, value in live_nodes.items():
        if value != 0:
            # There are some asymmetries between the two graphs, so return false
            return False

    return True


g1 = nx.Graph()
g1.add_nodes_from([
    (0, {"color": DEAD_COLOR}),
    (1, {"color": DEAD_COLOR}),
    (2, {"color": ALIVE_COLOR}),
    (3, {"color": DEAD_COLOR}),
    (4, {"color": DEAD_COLOR})])
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)

g2 = nx.Graph()
g2.add_nodes_from([
    (0, {"color": DEAD_COLOR}),
    (1, {"color": DEAD_COLOR}),
    (2, {"color": ALIVE_COLOR}),
    (3, {"color": DEAD_COLOR}),
    (4, {"color": DEAD_COLOR})])
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(1, 4)
g2.add_edge(4, 3)

run_isomorphic_test(get_random_graph_one_live_node(5, 0.6), get_random_graph_one_live_node(5, 0.6), isomorphism_test, 1)
