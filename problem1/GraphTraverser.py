import numpy as np
class GraphTraverser():
    def __init__(self):
        pass
    def dfs_traverse(self,graph):

        visited = [False] * graph.node_count
        tree = np.zeros((graph.node_count,graph.node_count))
        def dfs_run(node):
            visited[node] = True
            for neighbor in range(graph.node_count):
                if graph.adjacency_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    tree[node][neighbor] = 1
                    dfs_run(neighbor)

        for i in range(graph.node_count):
            if not visited[i]:
                dfs_run(i)
        return tree
    def bfs_traverse(self,graph):
        from collections import deque
        visited = [False] * graph.node_count
        tree = np.zeros((graph.node_count,graph.node_count))

        def bfs_run(node):
            queue = deque([node])
            visited[node] = True
            while queue:
                curr_node = queue.popleft()
                for neighbor in range(graph.node_count):
                    if graph.adjacency_matrix[curr_node][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        tree[curr_node][neighbor] = 1
                        queue.append(neighbor)

        for i in range(graph.node_count):
            if not visited[i]:
                bfs_run(i)

        return tree
    def print_graph_simple(self,adjacency_matrix):
        for i,row in enumerate(adjacency_matrix):
            for val in row:
                print(val, end=' ')
            print()
        pass
    def print_graph_beauty(self,adjacency_matrix):
        from tabulate import tabulate
        print(tabulate(adjacency_matrix, headers='firstrow', tablefmt='grid'))
    def show_graphical(self,adjacency_matrix,node_names,filename):
        import networkx as nx
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10,10),dpi=100)
        graph = nx.Graph(adjacency_matrix)
        label_dict = {}
        for i,node in enumerate(node_names):
            label_dict[i] = node
        nx.draw(graph,labels=label_dict, with_labels=True,node_size=3000,font_size = 23)
        plt.savefig(f"{filename}.png")