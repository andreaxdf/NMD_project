import csv
import os
import random
import time

import networkx as nx

import utils.utils
from isomorphic_test import run_isomorphic_test
from tests.dummy_test import isomorphism_test as test1
from tests.first_test import isomorphism_test as test2
from tests.second_test import isomorphism_test as test3
from tests.third_test import isomorphism_test as test4
from utils.utils import get_random_graph_one_live_node

CSV_FILE = 'data/execution_times.csv'
CSV_FILE_MORE = 'data/execution_times_more.csv'
CSV_FILE_FEW_CHANGES = 'data/execution_times_with_few_changes.csv'


def execute_test_with_few_changes(filename: str, isomorphism_test_list: list, steps: int, nodes: int, p: float,
                                  cycling_check: int, changes: int):
    """ Execute the tests on the same randomly created graph, but one of them has one less edge. """

    info_list = []

    for i in range(steps):
        graph1 = get_random_graph_one_live_node(nodes, p)
        graph2 = graph1.copy()

        # Re-color the copied graph, otherwise the game always starts from the same node
        utils.utils.color_graph(graph2)

        # Randomly delete a number of edges equal to the parameter changes
        for k in range(changes):
            remove_one_random_edge(graph2)

        start_nx = time.time()
        is_isomorphic = nx.is_isomorphic(graph1, graph2)
        end_nx = time.time()

        for test, name in isomorphism_test_list:
            start = time.time()
            result = run_isomorphic_test(graph1, graph2, test,
                                         cycling_check=cycling_check)
            end = time.time()

            # 'Step', 'Function', 'Nodes', 'p', 'changes', 'cycling check', 'Is isomorphic', 'Test result', 'Test execution time', 'NX execution time'
            info = [i, name, nodes, p, changes, cycling_check, is_isomorphic, result, end - start, end_nx - start_nx]

            info_list.append(info)

        print(f"Step {i} finished")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        for info in info_list:
            writer.writerow(info)


def remove_one_random_edge(graph):
    """ Remove a randomly chosen edge from the graph. """

    edges = list(graph.edges())

    if len(edges) > 0:
        edge_to_remove = random.choice(edges)
        graph.remove_edge(*edge_to_remove)


def execute_test(filename: str, isomorphism_test_list: list, steps: int, nodes: int, p: float, cycling_check: int):
    info_list = []

    for i in range(steps):
        graph1 = get_random_graph_one_live_node(nodes, p)
        graph2 = get_random_graph_one_live_node(nodes, p)

        start_nx = time.time()
        is_isomorphic = nx.is_isomorphic(graph1, graph2)
        end_nx = time.time()

        for test, name in isomorphism_test_list:
            start = time.time()
            result = run_isomorphic_test(graph1, graph2, test,
                                         cycling_check=cycling_check)
            end = time.time()

            # 'Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time', 'NX execution time'
            info = [i, name, nodes, p, is_isomorphic, result, end - start, end_nx - start_nx]

            info_list.append(info)

        print(f"Step {i} finished")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        for info in info_list:
            writer.writerow(info)


def gather_information_with_few_changes(test_list):
    filename = CSV_FILE_FEW_CHANGES

    p_values = [0.2, 0.4, 0.6, 0.8, 1.0]

    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Step', 'Function', 'Nodes', 'p', 'changes', 'cycling check', 'Is isomorphic', 'Test result', 'Test execution time',
                         'NX execution time'])

    for p in p_values:
        for nodes in range(10, 101, 10):
            for changes in range(1, 4):
                for cycling_check in [1, 5, 10]:
                    print(f"Starting run with: p={p}, nodes={nodes}, changes={changes}.")
                    execute_test_with_few_changes(filename, test_list, 10, nodes, p, cycling_check, changes)


def gather_more_information(test_list):
    filename = CSV_FILE_MORE

    p_values = [0.2, 0.4, 0.6, 0.8, 1.0]

    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time',
                         'NX execution time'])

    for p in p_values:
        for nodes in range(10, 500, 10):
            print(f"Starting run with: p={p}, nodes={nodes}.")
            execute_test(filename, test_list, 3, nodes, p, 10)


def gather_information(test_list):
    filename = CSV_FILE_MORE

    p_values = [0.2, 0.4, 0.6, 0.8, 1.0]
    nodes_steps_values = [(10, 10), (100, 3), (1000, 1)]  # (number of nodes, how many graphs should be tried)

    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time',
                         'NX execution time'])

    for p in p_values:
        for nodes, steps in nodes_steps_values:
            print(f"Starting run with: p={p}, steps={steps}, nodes={nodes}.")
            execute_test(filename, test_list, steps, nodes, p, 10)

def graph_test():
    graph1 = get_random_graph_one_live_node(5, 0.5)
    graph2 = graph1.copy()

    utils.utils.show_graph(graph1)

    # Re-color the copied graph, otherwise the game always starts from the same node
    utils.utils.color_graph(graph2)

    utils.utils.show_graph(graph2)

    # Randomly delete a number of edges equal to the parameter changes
    for k in range(3):
        remove_one_random_edge(graph2)


function_list = [(test1, "dummy_test"), (test2, "first_test"), (test3, "second_test"), (test4, "third_test")]

gather_information_with_few_changes(function_list)
