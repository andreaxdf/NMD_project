import networkx as nx

from isomorphic_test import run_isomorphic_test
from utils.utils import get_random_graph_one_live_node

ALIVE_COLOR = "green"
DEAD_COLOR = "red"


# Find the connected component starting from start_node using dfs search. While searching the component, mark all the visited nodes as visited.
def get_connected_component(start_node: int, graph: nx.Graph, visited: set) -> list:
    stack = [start_node]

    component = []

    if graph.nodes[start_node]['color'] == DEAD_COLOR:
        # There is not even a single node, since the start is not alive.
        return []

    while stack:
        node = stack.pop()
        component.append(node)
        visited.add(node)
        for adj in graph.neighbors(node):
            if graph.nodes[adj]['color'] == ALIVE_COLOR and adj not in visited:
                stack.append(adj)

    return component


# This test check if for each connected component in the first graph there is a corresponding connected component in the second graph with the same dimension.
def isomorphism_test(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    connected_components = {}
    visited1 = set()

    for node in graph1:
        if graph1.nodes[node]['color'] == ALIVE_COLOR and node not in visited1:
            length = len(get_connected_component(node, graph1, visited1))

            if length not in connected_components.keys():
                connected_components[length] = 0
            connected_components[length] += 1

    visited2 = set()

    for node in graph2:
        if graph2.nodes[node]['color'] == ALIVE_COLOR and node not in visited2:
            length = len(get_connected_component(node, graph2, visited2))

            if length not in connected_components.keys():
                # There is not a connected component with the same length in the other graph
                return False
            connected_components[length] -= 1

    for value in connected_components.values():
        if value != 0:
            # There are some asymmetries between the two graphs, so they are not isomorphic
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

print(run_isomorphic_test(get_random_graph_one_live_node(5, 0.6), get_random_graph_one_live_node(5, 0.6), isomorphism_test, 1))
