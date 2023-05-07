import numpy as np
from tabulate import tabulate
class Graph():
    def __init__(self, node_names):
        self.node_names = node_names
        self.node_count = len(node_names)
        self.adjacency_matrix = np.zeros((self.node_count,self.node_count),dtype=int)
    def add_edge(self, node1, node2):
        i = self.node_names.index(node1)
        j = self.node_names.index(node2)
        self.adjacency_matrix[i][j] = 1
        self.adjacency_matrix[j][i] = 1

    def DFS(self):
        pass
    def BFS(self):
        pass
    def print_graph_simple(self):

        for i,row in enumerate(self.adjacency_matrix):
            for val in row:
                print(val, end=' ')
            print()
        pass
    def print_graph_beauty(self):
        print(tabulate(self.adjacency_matrix, headers='firstrow', tablefmt='grid'))
    def show_graphical(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        graph = nx.Graph(self.adjacency_matrix)
        label_dict = {}
        for i,node in enumerate(self.node_names):
            label_dict[i] = node
        nx.draw(graph,labels=label_dict, with_labels=True)
        plt.savefig("Graph.png")
