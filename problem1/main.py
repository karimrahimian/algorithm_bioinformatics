from Graph import Graph
from CSV_Reader import CSV_Reader
if __name__ =="__main__":
    filename = "data/graph.csv"

    reader = CSV_Reader(filename)
    node_names = reader.get_node_names()
    graph = Graph(node_names)
    reader.open_file()
    reader.splip_head()
    while (True):
        edge = reader.get_next_edge()
        if edge == None:
            break
        graph.add_edge(edge[0],edge[1])

    reader.close_file()

    graph.print_graph_beauty()
    graph.show_graphical()