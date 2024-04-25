import networkx as nx
import numpy as np

from utils.utils import ALIVE_COLOR, DEAD_COLOR


class Game:

    def __init__(self, graph):
        self.graph = graph
        self.previous_states = []

    def get_live_nodes(self):
        graph = self.graph

        live_nodes = np.zeros(len(graph.nodes))

        for node in graph:
            if graph.nodes[node]['color'] == ALIVE_COLOR:
                live_nodes[node] = 1

        return live_nodes

    def _is_finished(self, verbose: bool = False) -> bool:
        current_state: np.ndarray = self.get_live_nodes()

        if np.all(current_state == 0):
            if verbose:
                print("All nodes are zeros")
            return True

        for state in self.previous_states:
            if np.array_equal(state, current_state):
                if verbose:
                    print("Previous state repeated")
                return True
        return False

    def _update_states(self) -> None:
        self.previous_states.append(self.get_live_nodes())

    # Do a game iteration and return if the game is finished or not
    def game_iteration(self) -> bool:
        graph = self.graph

        colornew = {}

        for node in graph:
            alive = 0
            near = 0
            for neighbour in graph.neighbors(node):
                if graph.nodes[neighbour]['color'] == ALIVE_COLOR:
                    near += 1
                    alive += 1
                elif graph.nodes[neighbour]['color'] == DEAD_COLOR:
                    near += 1

            if graph.nodes[node]['color'] == ALIVE_COLOR and 1 <= alive < near:
                colornew[node] = ALIVE_COLOR
            elif graph.nodes[node]['color'] == DEAD_COLOR and alive == 1:
                colornew[node] = ALIVE_COLOR
            else:
                colornew[node] = DEAD_COLOR

        for node, new_color in colornew.items():
            graph.nodes[node]['color'] = new_color

        ret = self._is_finished()

        # Update the previous states of the game
        self._update_states()

        return ret
