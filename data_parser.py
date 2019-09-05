from graphic_items import Node, Edge


def processFrontendData(node_objs, edge_matrix):

    node_data = {
        key: {
            'x': val.center.x(),
            'y': val.center.y()
        }
        for key, val in node_objs.items()
    }

    edge_data = [[1 if edge else 0 for edge in row] for row in edge_matrix]
    return {
        'nodes': node_data,
        'edges': edge_data
    }


def processBackendData(node_data, edge_data):

    node_objs = {
        key: Node(val['x'], val['y'], key)
        for key, val in node_data.items()
    }

    edge_matrix = []
    for i in range(len(edge_data)):
        row = []
        for j in range(len(edge_data)):
            if edge_data[i][j]:
                row.append(Edge(node_objs[i], node_objs[j]))
            else:
                row.append(None)
        edge_matrix.append(row)

    return node_objs, edge_matrix