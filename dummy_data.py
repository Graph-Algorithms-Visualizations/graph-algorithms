from graphic_items import Node, Edge

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Linkage:
    def __init__(self, end1, end2, weight = 0):
        self.ends = []
        self.ends.append(end1)
        self.ends.append(end2)
        self.weight = weight

matrix = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

node_objs = {
    0: Node(0, 0, 0),
    1: Node(50, 50, 1),
    2: Node(100, 0, 2),
    3: Node(100, 50, 3)
}

# node_objs = {}
# # Creates a dictionary of Node Objects as value linked to their indices as keys
# def node_object_convert(dict1)
# for i in dict:
#     node_objs[i] = Vertex(dict[i][0],dict[i][1])


edge_matrix = []

for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[i])):
        if not matrix[i][j]:
            row.append(None)
        else:
            row.append(Edge(node_objs[i], node_objs[j]))
    edge_matrix.append(row)

def remove_connections(index):
    for i in range(len(edge_matrix)):
        edge_matrix[index][i] = None
        edge_matrix[i][index] = None

def remove_node(index):
    del node_objs[index]
    remove_connections(index)


def get_processed_data():
    return node_objs, edge_matrix
