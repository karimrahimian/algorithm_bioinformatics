from Graph import Graph
from CSV_Reader import CSV_Reader
from GraphTraverser import GraphTraverser
if __name__ =="__main__":
    filename = "data/graph.csv"

    reader = CSV_Reader(filename)
    node_names = reader.get_node_names()
    graph = Graph(node_names)

    reader.open_file()
    reader.skip_head()

    while (True):
        edge = reader.get_next_edge()
        if edge == None:
            break
        graph.add_edge(edge[0],edge[1])

    reader.close_file()

    graph.print_graph_beauty()
    graph.show_graphical()

    operation =GraphTraverser()

    print("BFS algorithm ")
    tree_bfs = operation.bfs_traverse(graph)
    operation.print_graph_beauty(tree_bfs)
    operation.show_graphical(tree_bfs, graph.node_names, "BFS")

    print ("DFS algorithm ")
    tree_dfs = operation.dfs_traverse(graph)
    operation.print_graph_beauty(tree_dfs)
    operation.show_graphical(tree_dfs,graph.node_names,"DFS")