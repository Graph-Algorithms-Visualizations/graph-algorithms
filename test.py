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

node = {}
# Creates a dictionary of Node Objects as value linked to their indices as keys
for i in dict:
    node[i] = Node(dict[i][0],dict[i][1])