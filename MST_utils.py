# Undirected Graph Class
class UndirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    # Add edges to the edge list of this graph object
    # Add unique vertices to the vertices set of this graph object
    def addEdge(self, u, v, w):
        self.edges.append([u, v, w])
        self.vertices.add(u)
        self.vertices.add(v)

    # Prints edges,their weights and total weight of this graph object
    def printEdges(self):
        weight = 0
        print ("Edges")
        for u, v, w in self.edges:
            weight += w
            print("%s -- %s == %d" % (u, v, w))
        print("Total Weight", weight)

# Minimum Spanning Tree Wrapper Class
class MST:

    # Finds root of the tree that x belongs to
    def getRoot(self, x, roots):
        # If current node is the root
        if roots[x] == x:
            return x
        # else call getRoot on parent
        return self.getRoot(roots[x], roots)

    # Performs Union operation on two trees x and y. Union by rank
    def union(self, x, y, roots, ranks): 
        # Add tree with lower rank to tree with higher rank
        if ranks[x] < ranks[y]:
            roots[x] = y
        elif ranks[x] > ranks[y]:
            roots[y] = x
        # When ranks are equal, add arbitrarily and increase tree rank
        else:
            roots[y] = x
            ranks[x] += 1
    
    # Initialize a tree for each vertex of the graph
    def initForest(self, vertices, roots, ranks):
        for vertex in vertices:
            # Set parent to self
            roots[vertex] = vertex
            # set starting rank
            ranks[vertex] = 0
    
    # Returns a list of all the edges of the graph sorted by weight
    # and a list of all the vertices in the graph
    def sortEdges(self, graph):
        # Sort the edges of the graph by weight
        return graph.vertices, sorted(graph.edges, key = lambda x: x[2])

    # Kruskal MST algorithm
    def kruskalMST(self,graph):

        vertices = set()    # List of all vertices of the graph
        edges = []          # List of all the edges of the graph
        roots = {}          # Trees used to perform Kruskal's algorithm
        ranks = {}          # Ranks of each of the trees

        # Generated MST
        # Using a UndirectGraph object to store the MST
        # The graph will only contain the edges required for the mst
        mst = UndirectedGraph()

        # Sort edges of graph by weight
        vertices, edges = self.sortEdges(graph)

        # Initialize forest of trees. Where each tree is a single vertiex from the graph
        self.initForest(vertices, roots, ranks)

        # Iterator to iterate over sorted edge list
        # Pop from front is more expensicve than access by index
        i = 0 

        # Counter to keep track of no of edges added to MST
        e = 0  

        # Run MST loop
        # Need to repeat until we have (no.of vertices - 1) edges
        # Since MST for v vertices will have v-1 edges
        while e < len(vertices) - 1:

            u, v, w = edges[i]      # Read edge from sorted edge list
            i = i + 1               # Increment edge list indexer

            x = self.getRoot(u, roots)   # Find root of tree that u belongs to
            y = self.getRoot(v, roots)   # Find root of tree that v belongs to

            # If u and v dont belong to the same tree,
            # i.e their root is not the same
            # then add this edge to the MST
            if x != y:
                e = e + 1   # increment counter for no.of edges in MST
                mst.addEdge(u, v, w)
                self.union(x, y, roots, ranks)    # Combine the two trees that u and v belong to
        
        # Return the generated MST (Undirected graph Object)
        return mst
