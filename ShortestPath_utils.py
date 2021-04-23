import numpy as np
import sys

class Graph():
  
  def __init__(self):
    self.path = ""
  

  #function to print path
  def printPath(self, parent, node):
    path=""
    if parent[node] == -1:
      self.path = str(node+1)
      return self.path
    self.printPath(parent, parent[node])
    path = str(node+1)
    self.path = self.path +"-"+ path
    return(self.path)

  #function to print the Distance Vector
  def printGraph(self, distance, source, parent):
    
    print("Vertex\t\tDistance\tPath")
    for node in range(len(distance)):
      print(source,"to",node+1,"\t\t",int(distance[node]),"\t\t",self.printPath(parent, node))
      

  def readFromFile(self, input):
    #read graph from file
    with open(input, 'r') as file:
      lines = [line.strip().split() for line in file]

    #get number of vertices, edges and type of Graph
    vertices, edges, graphType = int(lines[0][0]), int(lines[0][1]), lines[0][2]

    #find if source node is provided
    if len(lines) > edges + 1:
      src = lines[edges+1][0]
    else:
      src = lines[1][0]

    #create a matrix of zeros for graph
    G = np.zeros((vertices, vertices))
    
    #add weights to the graph matrix
    for i in range(1,edges + 1):
      u, v, w = int(lines[i][0])-1, int(lines[i][1])-1, int(lines[i][2])
      G[u][v] = w
    
    #considering edges in undirected graph as bidirectional 
    if lines[0][2] == 'U':
      for i in range(vertices):
        for j in range(vertices):
          if G[i][j] != 0:
            G[j][i] = G[i][j]

    return G, int(src)

class Dijkstra:
  global distance, shortPathTree

  def __init__(self, graph):
    #initializing number of vertices
    self.V = len(graph)
    self.graph = graph

  def minDistance(self, distance, shortPathTree):
    min = sys.maxsize
    
    for v in range(self.V):
      #print(v," ",distance[v]," Min ",min)
      if distance[v] < min and shortPathTree[v] == False:
        min = distance[v]
        min_index = v

    return min_index

  def dijkstra(self, src):

    #initializing distance matrix to infinity
    distance = [sys.maxsize] * self.V
    #parent list to maintain intermediate vertices between source and destination
    parent = [-1] * self.V
    src = src - 1
    distance[src] = 0

    #initializing visited nodes array to False
    shortPathTree = [False] * self.V
    
    for index in range(self.V):
      u = self.minDistance(distance, shortPathTree)
      shortPathTree[u] = True
      path=""
      for v in range(self.V):
        if self.graph[u][v] > 0 and shortPathTree[v] == False and distance[v] > distance[u] + self.graph[u][v]:
          distance[v] = distance[u] + self.graph[u][v]
          parent[v] = u
      
    return distance, parent
    