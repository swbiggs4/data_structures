# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
	    
    def addEdge(self, u, v):
        # function to add an edge to graph
        # make a list visted to check if a node is already visited or not.
        # note this is for key == node, key has to be unique, hashable. Otherwise need a node class
        self.graph[u].append(v)
        self.visited = []

	# Function to print a BFS of graph
    def BFS(self,s):
        # create a queue for BFS
        queue = []
        # add source node in visted, enqueue it
        queue.append(s)
        self.visted.append(s)

        while queue:
             s = queue.pop(0)
             print(s)

             for neighbor in self.graph[s]:
                  if neighbor not in self.visited:
                        queue.append(neighbor)
                        self.visted.append(neighbor)
                       
    def DFS(self, s):
        # difference between DFS and BFS is recursion

        self.visited.append(s)
        # print current node 
        print(s)

        for neighbor in self.graph[s]:
            if neighbor not in self.visited:
                self.DFS(neighbor)
# Driver code 
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# This code is contributed by Neelam Yadav 
