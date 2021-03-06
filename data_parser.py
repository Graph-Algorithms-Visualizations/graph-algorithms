from graphic_items import Node, Edge
from PyQt5.QtGui import QColor

def processFrontendData(nodeList, adjacencyList):

    node_data = {
        node.key: {
            'x': node.center.x(),
            'y': node.center.y(),
            'color': (node.color.red(), node.color.green(), node.color.blue())
        }
        for node in nodeList
    }

    edge_data = [
        [{
            'from': edge.fromNode.key,
            'to': edge.toNode.key,
            'color': (edge.color.red(), edge.color.green(), edge.color.blue())
        }
                  for edge in row]
        for row in adjacencyList
    ]

    return {
        'nodes': node_data,
        'edges': edge_data
    }


def processBackendData(node_data, edge_data):


    nodeList = [Node(val['x'], val['y'], QColor(val['color'][0], val['color'][1], val['color'][2])) for key, val in node_data.items()]

    adjacencyList = [
        [Edge(nodeList[edge['from']], nodeList[edge['to']], QColor(edge['color'][0] , edge['color'][1], edge['color'][2]))
         for edge in edges]
        for edges in edge_data
    ]

    return nodeList, adjacencyList