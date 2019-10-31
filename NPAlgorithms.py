from modify import Graph

def intToBinary(number, size):
        binary = [0 for i in range(size)]
        i = 0
        while number > 0:
            binary[i] = number%2
            number = number // 2
            i += 1
        
        return binary

def setBits(binary):
        counter = 0
        for i in binary:
            if i == 1:
                counter += 1
        return counter

def visitAllNeighborClique(visited, binary):
    n = len(binary)
    for i in range(n):
        if binary[i] == 1 and visited[i] == False:
            return False
    return True

# utility functions for NP algorithms
class AlgorithmManager:

    def __init__(self, graph):
        self.graph = graph


    def runAlgorithm(self, id):
        if id == 1:
            return self.minimumDominantSet()
        elif id == 2:
            return self.maximumIndependentSet()
        elif id == 3:
            return self.maximumClique() 



    def minimumDominantSetUtil(self, binary):
        n = len(self.graph.adjacencyList)
        visited = [False for i in range(n)]
        for i in range(n):
            if binary[i] == 1:
                visited[i] = True
                for j in self.graph.adjacencyList[i]:
                    visited[j.toNode.key] = True
        for i in range(n):
            if visited[i] == False:
                return False
        
        return True

    def minimumDominantSet(self):
        # ID:1
        n = len(self.graph.adjacencyList)

        minimumSet = []
        minimum = n
        rangeToCover = 2**n
        for i in range(rangeToCover):
            binary = intToBinary(i,n)
            involvedNodes = setBits(binary)

            if self.minimumDominantSetUtil(binary) == True:
                if minimum > involvedNodes:
                    minimum = involvedNodes
                    minimumSet = binary
        
        print(str(minimumSet))
        return minimumSet
        
        #print the dominating number
        # for i in range(0,n-1):
        #     if minimumSet[i] == 1:
        #         print(i)


    def maximumIndependentSetUtil(self,binary):
        n = len(self.graph.adjacencyList)
        visited = [False for i in range(n)]
        
        for i in range(n):
            if binary[i] == 1:
                visited[i] = True

        for i in range(n):
            if visited[i] == True:
                for j in self.graph.adjacencyList[i]:
                    if visited[j.toNode.key] == True:
                        return False
        
        return True


    def maximumIndependentSet(self):
        #ID:2
        n = len(self.graph.adjacencyList)

        maximumSet = []
        maximum = 0
        rangeToCover = 2**n

        for i in range(rangeToCover):
            binary = intToBinary(i,n)
            involvedNodes = setBits(binary)

            if self.maximumIndependentSetUtil(binary) == True:
                if maximum < involvedNodes:
                    maximum = involvedNodes
                    maximumSet = binary
        
        print(str(maximumSet))
        return maximumSet
        # for i in range(n):
        #     if maximumSet[i] == 1:
        #         print(i)

    

    def maximumCliqueUtil(self, binary):

        n = len(self.graph.adjacencyList)
        for i in range(n):
            if binary[i] == 1:
                visited = [False for j in range(n)]
                visited[i] = True
                for j in self.graph.adjacencyList[i]:
                    visited[j.toNode.key] = True
                
                if not visitAllNeighborClique(visited, binary):
                    return False

        return True


    def maximumClique(self):
        #ID:3
        n = len(self.graph.adjacencyList)

        maximumSet = [0 for i in range(n)]
        maximum = 0
        rangeToCover = 2**n
        
        for i in range(rangeToCover):
            binary = intToBinary(i,n)
            involvedNodes = setBits(binary)

            if self.maximumCliqueUtil(binary) == True:
                if maximum < involvedNodes:
                    maximum = involvedNodes
                    maximumSet = binary
        
        # for i in range(n):
        #     if maximumSet[i] == 1:
        #         print(i)
        print(str(maximumSet))
        return maximumSet