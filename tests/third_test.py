import networkx as nx

from isomorphic_test import run_isomorphic_test
from utils.utils import get_random_graph_one_live_node

ALIVE_COLOR = "green"
DEAD_COLOR = "red"


# This test check if node with the bigger number of neighbors in the first graph is the same in the second graph. The same for the node with the minor number of neighbors.
def isomorphism_test(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    major1 = 0
    minor1 = len(graph1.nodes)

    if len(graph1.nodes) != len(graph2.nodes):
        return False

    for node in graph1:
        count = 0
        for adj in graph1.neighbors(node):
            if graph1.nodes[adj]['color'] == ALIVE_COLOR:
                count += 1

        if count > major1:
            major1 = count

        if count < minor1:
            minor1 = count

    major2 = 0
    minor2 = len(graph1.nodes)

    for node in graph2:
        count = 0
        for adj in graph2.neighbors(node):
            if graph2.nodes[adj]['color'] == ALIVE_COLOR:
                count += 1

        if count > major2:
            major2 = count

        if count < minor2:
            minor2 = count

    if major1 != major2 or minor1 != minor2:
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
    (1, {"color": ALIVE_COLOR}),
    (2, {"color": DEAD_COLOR}),
    (3, {"color": DEAD_COLOR}),
    (4, {"color": DEAD_COLOR})])
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(1, 4)
g2.add_edge(4, 3)

run_isomorphic_test(get_random_graph_one_live_node(5, 0.6), get_random_graph_one_live_node(5, 0.6), isomorphism_test, 1)
