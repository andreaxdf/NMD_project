import csv
import time

import networkx as nx

from tests.dummy_test import isomorphism_test as test1
from tests.first_test import isomorphism_test as test2
from tests.second_test import isomorphism_test as test3
from tests.third_test import isomorphism_test as test4
from utils.utils import get_random_graph_one_live_node
from isomorphic_test import run_isomorphic_test

CSV_FILE = 'execution_times_more.csv'


def execute_test(filename: str, isomorphism_test_list: list, steps: int, nodes: int, p: float):
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
                                         cycling_check=1)  # TODO should cycling_check parameter be 1? Better in the case of unusually isomorphic graphs
            end = time.time()

            # 'Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time', 'NX execution time'
            info = [i, name, nodes, p, is_isomorphic, result, end - start, end_nx - start_nx]

            info_list.append(info)

        print(f"Step {i} finished")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        for info in info_list:
            writer.writerow(info)


def gather_more_information(filename: str, test_list):
    p_values = [0.2, 0.4, 0.6, 0.8, 1.0]

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time',
                         'NX execution time'])

    for p in p_values:
        for nodes in range(10, 500, 10):
            print(f"Starting run with: p={p}, nodes={nodes}.")
            execute_test(filename, test_list, 3, nodes, p)


def gather_information(filename, test_list):
    p_values = [0.2, 0.4, 0.6, 0.8, 1.0]
    nodes_steps_values = [(10, 10), (100, 3), (1000, 1)]  # (number of nodes, how many graphs should be tried)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Step', 'Function', 'Nodes', 'p', 'Is isomorphic', 'Test result', 'Test execution time',
                         'NX execution time'])

    for p in p_values:
        for nodes, steps in nodes_steps_values:
            print(f"Starting run with: p={p}, steps={steps}, nodes={nodes}.")
            execute_test(test_list, steps, nodes, p)


function_list = [(test1, "dummy_test"), (test2, "first_test"), (test3, "second_test"), (test4, "third_test")]

# TODO scegliere test da abbinare

gather_more_information(CSV_FILE, function_list)
