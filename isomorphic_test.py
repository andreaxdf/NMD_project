import networkx as nx
from matplotlib import pyplot as plt

import utils.utils
from game.game import Game


def run_isomorphic_test(graph1, graph2, isomorphism_test, cycling_check=5, show_steps=False):
    """ cycling_check: indicates every how many steps the isomorphism test must be executed """

    assert cycling_check > 0

    if show_steps:
        utils.utils.show_graph(graph1)
        utils.utils.show_graph(graph2)

    game1 = Game(graph1)
    game2 = Game(graph2)

    is_finished1 = 0
    is_finished2 = 0

    while True:
        # Run the game for N steps and then execute the isomorphic test
        for i in range(cycling_check):
            is_finished1: int = game1.game_iteration()
            is_finished2: int = game2.game_iteration()
            if is_finished1 != 0 or is_finished2 != 0:
                break
        is_isomorphic = isomorphism_test(graph1, graph2)
        if show_steps:
            utils.utils.show_graph(graph1)
            utils.utils.show_graph(graph2)

        if not is_isomorphic:
            return False

        if is_finished1 != 0 or is_finished2 != 0:
            return is_isomorphic
