from graphic_items import Node, Edge
from PyQt5.QtGui import QColor

def processFrontendData(node_objs, edge_matrix):

    node_data = {
        key: {
            'x': val.center.x(),
            'y': val.center.y(),
            'color': (val.color.red(), val.color.green(), val.color.blue())
        }
        for key, val in node_objs.items()
    }

    edge_data = [[{'color': (edge.color.red(), edge.color.green(), edge.color.blue())} if edge else None for edge in row] for row in edge_matrix]
    return {
        'nodes': node_data,
        'edges': edge_data
    }


def processBackendData(node_data, edge_data):

    node_objs = {
        key: Node(val['x'], val['y'], key, QColor(val['color'][0], val['color'][1], val['color'][2]))
        for key, val in node_data.items()
    }

    edge_matrix = []
    for i in range(len(edge_data)):
        row = []
        for j in range(len(edge_data)):
            if edge_data[i][j]:
                row.append(Edge(node_objs[i], node_objs[j], QColor(edge_data[i][j]['color'][0], edge_data[i][j]['color'][1],
                                                                   edge_data[i][j]['color'][2])))
            else:
                row.append(None)
        edge_matrix.append(row)

    return node_objs, edge_matrix