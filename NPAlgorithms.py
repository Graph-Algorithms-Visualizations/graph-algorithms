from modify import Graph

def intToBinary(number, size):
    """
    Converts a decimal number to binary form

    Parameters:
    ==========
    number: Integer
        The Number to be converted into binary form

    size: Integer
        The maximum length of the returning binary list

    Returns:
    =======
    list:
        Returns a list of length size consisting of 0's and 1's 
        representing binary form of number
    """
    binary = [0 for i in range(size)]
    i = 0
    while number > 0:
        binary[i] = number%2
        number = number // 2
        i += 1
    
    return binary

def setBits(binary):
    """
    Calculates the number of ones in the binary

    Parameters:
    ==========
    binary: List
        The binary list of a decimal number

    Returns:
    =======
    Integer:
        Returns number of 1's in the binary representation
    """    
    counter = 0
    for i in binary:
        if i == 1:
            counter += 1
    return counter

def visitAllNeighborClique(visited, binary):
    """
    Checks wether all considered nodes in binary are visited 
    or not. This function is used as a utility function for the 
    clique subroutine

    Parameters:
    ==========
    visited: list
        The information of visited and unvisited node

    binary: list
        The nodes which are under consideration

    Returns:
    =======
    bool:
        If all considered nodes are visited then True
        otherwise False
    """
    n = len(binary)
    for i in range(n):
        if binary[i] == 1 and visited[i] == False:
            return False
    return True

class AlgorithmManager:

    def __init__(self, graph):
        self.graph = graph


    
    def runAlgorithm(self, id):
        """
        Runs the corresponding algorithm

        Parameters:
        ==========
        id: Integer
           represents the algorithm id 
        """
        if id == 1:
            return self.minimumDominantSet()
        elif id == 2:
            return self.maximumIndependentSet()
        elif id == 3:
            return self.maximumClique() 



    def minimumDominantSetUtil(self, binary):
        """
        Checks wether the binary consideration of nodes is a
        valid Dominant Set or not

        Parameters:
        ==========
        binary: list
            The nodes which are under consideration

        Returns:
        =======
        bool:
            If all considered nodes form a Dominant Set then True
            otherwise False
        """
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
        """
        Calculates the dominant set of minimum size

        Returns:
        =======
        list:
            A list comprising of 0's and 1's of length equal 
            to number of nodes in graph.
            0: Represents the node was not considered
            1: Represents the node was considered
        """
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
        
        return minimumSet
        
        


    def maximumIndependentSetUtil(self,binary):
        """
        Checks wether the binary consideration of nodes is a
        valid independent set or not

        Parameters:
        ==========
        binary: list
            The nodes which are under consideration

        Returns:
        =======
        bool:
            If all considered nodes form an Independent Set then True
            otherwise False
        """
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
        """
        Calculates the independent set of maximimum size

        Returns:
        =======
        list:
            A list comprising of 0's and 1's of length equal 
            to number of nodes in graph.
            0: Represents the node was not considered
            1: Represents the node was considered
        """
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
                    
        return maximumSet

    

    def maximumCliqueUtil(self, binary):
        """
        Checks wether the binary consideration of nodes is a
        valid clique or not

        Parameters:
        ==========
        binary: list
            The nodes which are under consideration

        Returns:
        =======
        bool:
            If all considered nodes forms a clique then True
            otherwise False
        """
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
        """
        Calculates the clique of maximimum size

        Returns:
        =======
        list:
            A list comprising of 0's and 1's of length equal 
            to number of nodes in graph.
            0: Represents the node was not considered
            1: Represents the node was considered
        """
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

        return maximumSet