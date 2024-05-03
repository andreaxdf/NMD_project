import csv
import os

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

from game.game import Game
from utils.utils import get_random_graph_one_live_node

CSV_FILENAME = "data/graph_ends.csv"

P_VALUES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def execute_game_until_the_end(graph1, show_steps: bool = False):
    game1 = Game(graph1)

    if show_steps:
        color1 = [data['color'] for v, data in graph1.nodes(data=True)]
        nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
        plt.title("Graph1")
        plt.show()

    step = 0
    while True:
        step += 1
        # Run the game for N steps and then execute the isomorphic test

        is_finished: int = game1.game_iteration()

        if show_steps:
            color1 = [data['color'] for v, data in graph1.nodes(data=True)]
            nx.draw(graph1, with_labels=True, node_color=color1, node_size=800, edge_color='black')
            plt.title("Graph1")
            plt.show()

        if is_finished != 0:
            return is_finished, step


def gather_game_information():
    filename = CSV_FILENAME

    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nodes', 'p', 'steps', 'end'])

        for p in P_VALUES:
            for nodes in range(10, 51, 10):
                for k in range(0, 1000):
                    graph = get_random_graph_one_live_node(nodes, p)
                    ret, steps = execute_game_until_the_end(graph)

                    writer.writerow([nodes, p, steps, ret])
            print(f"Iterations with p={p} finished")


# Return the percentages of games which finished with all nodes dead for each different p
def get_game_statistic(df: pd.DataFrame):

    for p in P_VALUES:
        p_df = df[df['p'] == p]

        end1 = (p_df['end'] == 1).sum()
        end2 = (p_df['end'] == 2).sum()

        print("p=" + str(p) + ": " + str(end1 / (end2 + end1)))

    return


gather_game_information()

result_df = pd.read_csv(CSV_FILENAME)

get_game_statistic(result_df)
