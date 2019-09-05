from graphic_items import Node, Edge

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

edge_matrix = []

for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[i])):
        if not matrix[i][j]:
            row.append(None)
        else:
            row.append(Edge(node_objs[i], node_objs[j]))
    edge_matrix.append(row)


def get_processed_data():
    return node_objs, edge_matrix
