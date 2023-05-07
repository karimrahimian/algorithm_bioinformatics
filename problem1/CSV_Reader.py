import csv
class CSV_Reader():
    def __init__(self,csv_filename):
        self.csv_filename = csv_filename
        self.spiliter = "\t"
    def open_file(self):
        self.file_handler = open(self.csv_filename,"r")
        self.csv_reader = csv.reader(self.file_handler)
    def splip_head(self):
        try:
            next(self.csv_reader)
        except:
            pass
    def close_file(self):
        self.file_handler.close()
    def get_next_edge(self):
        try:
            line = next(self.csv_reader)
            node1 = line[0].split(self.spiliter)[0]
            node2 = line[0].split(self.spiliter)[1]

            return (node1,node2)
        except :
            return None
    def get_node_names(self):
        with open(self.csv_filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            nodes = []
            while (True):
                try:
                    line = None
                    line = next(csv_reader)
                except Exception as e:
                    print(e)
                if line == None:
                    break
                node = line[0].split(self.spiliter)
                nodes.append(node[0])
                nodes.append(node[1])

            nodes = list(set(nodes))
            nodes.sort()
            file.close()
        return nodes

