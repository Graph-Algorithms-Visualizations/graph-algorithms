class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Edge:
    def __init__(self, end1, end2, weight = 0):
        self.ends = []
        self.ends.append(end1)
        self.ends.append(end2)
        self.weight = weight

#testing data

dict1 = {
    0 : [1,2],
    1 : [4,5],
    2 : [6,7]
}

edge_matrix = [[None,None,1],
        [None,None,1],
        [1,1,None]]


#

node = {}
# Creates a dictionary of Node Objects as value linked to their indices as keys
for i in dict:
    node[i] = Node(dict[i][0],dict[i][1])


# edge_matrix is the matrix consisting of connections
# Sample edge_matrix:
# edge_matrix = [[None,None,1],
#         [None,None,1],
#         [1,1,None]]
# node is dictionary of Node Objects as value linked to their indices as keys
# Sample node dictionary for testing:
# {0: [1, 2], 1: [4, 5], 2: [6, 7]}

def remove_connections(index):
    for i in range(len(edge_matrix)):
        edge_matrix[index][i] = None
        edge_matrix[i][index] = None

def remove_node(index):
    del node[index]
    remove_connections(index)

