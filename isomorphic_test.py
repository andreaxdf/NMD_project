import networkx as nx
from matplotlib import pyplot as plt

from game.game import Game


# cycling_check: indicates every how many steps the isomorphism test must be executed
def run_isomorphic_test(graph1, graph2, isomorphism_test, cycling_check=5, show_steps=False):

    assert cycling_check > 0

    if show_steps:
        color1 = [data['color'] for v, data in graph1.nodes(data=True)]
        nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
        plt.title("Graph1")
        plt.show()
        color2 = [data['color'] for v, data in graph2.nodes(data=True)]
        nx.draw(graph2, with_labels=True, node_color=color2, node_size=800, edge_color='black')
        plt.title("Graph2")
        plt.show()

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
            color1 = [data['color'] for v, data in graph1.nodes(data=True)]
            nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
            plt.title("Graph1")
            plt.show()
            color2 = [data['color'] for v, data in graph2.nodes(data=True)]
            nx.draw(graph2, with_labels=True, node_color=color2, node_size=800, edge_color='black')
            plt.title("Graph2")
            plt.show()

        if not is_isomorphic:
            return False

        if is_finished1 != 0 or is_finished2 != 0:
            # print("GAME FINISHED")
            return is_isomorphic
