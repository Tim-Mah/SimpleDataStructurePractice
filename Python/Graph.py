import random

'''
@auther Tim Mah
Date: 2022
Generates a graph structure with n vertices and random edges.
Impliments Prim's and Breadth-First searching
'''

''' Representation of a connected, undirected graph data structure
    Graph is represented by 1/2 of an adjacentcy matrix.
    (1,1), (2, 2), etc. have been removed, as has anything above 
    those cells. When printed, row 0, column 0 corresponds to the
    edge 2-1.
'''


class Graph:
  '''
      @param n: The number of vertices in this graph

      Edges are randomly drawn between n vertices and assigned 
      random weights between 1 and 100, inclusive.
  '''

  def __init__(self, n):
    ## How many total edges
    totalSlots = 0
    ## Create Adjacency Matrix
    self.matrix = [None] * (n - 1)
    for i in range(len(self.matrix)):
      totalSlots += i + 1
      self.matrix[i] = [0] * (i + 1)

    ## Generate Matrix

    ## Verts keeps track of what vertices are generated
    verts = []
    ## Edges keeps track of the number of edges
    edges = 0
    remainSlots = totalSlots
    for i in range(len(self.matrix) - 1, -1, -1):
      for j in range(i + 1):
        remainSlots -= 1
        ## Forces there to be at least n-1 edges, where n is the number of vertexes
        if n - 1 - edges == remainSlots and n - 1 - edges != 0:
          ## Added 0.9 to last condition of random.uniform because that number is highly unlikely to be chosen
          self.matrix[i][j] = int(random.uniform(1, 100.9))
          if (j + 1 not in verts):
            verts.append(j + 1)
          if (i + 2 not in verts):
            verts.append(i + 2)
          edges += 1
        else:
          ## Force edge on last column, if last chance to generate vertex
          ## 2nd condition: if last cell and vertex 1 isn't generated
          if (i + 2 not in verts
              and j == i) or (i == 2 and j == 0) and 1 not in verts:
            self.matrix[i][j] = int(random.uniform(1, 100.9))
            if (j + 1 not in verts):
              verts.append(j + 1)
            if (i + 2 not in verts):
              verts.append(i + 2)
            edges += 1
          else:
            ## Picks if slot gets an edge
            ## Original would pick close to min edges
            ##if (random.uniform(1, totalSlots) <= (vertexes-1)):
            if (random.uniform(0, 1) <= (0.5)):
              self.matrix[i][j] = int(random.uniform(1, 100.9))
              if (j + 1 not in verts):
                verts.append(j + 1)
              if (i + 2 not in verts):
                verts.append(i + 2)
              edges += 1

  '''
      Prints this graph as a half square matrix (Diagonal removed)
  '''

  def printSelf(self):
    for i in range(len(self.matrix)):
      for j in range(i + 1):
        print("[", self.matrix[i][j], "]", sep="", end='')
      print()
    print()

  '''
      Reformats the matrix into a set of adjacent vertices and a
      corrosponding set of edge weights.
      
      @return: the set of vertices and the set of edges
  '''

  def reformat(self):
    edges = [None] * (len(self.matrix) + 1)
    vertices = [[-1]] * (len(self.matrix) + 1)
    ## Turn graph into a list of edges and vertices
    ## vertices[0] represents vertex 1 (vertices go from 1-n)
    ##vertices[0] contains a list of all vertices its connected to
    ## Due to the contruction of the matrix, non-essential cells from a square matrix were removed, hence why i+2 is the vertex number and j+1 is the corrisponding adjacent vertex
    for i in range(len(self.matrix)):
      for j in range(i + 1):
        if (self.matrix[i][j] != 0):
          # Column, add row index to its list of connected vertices
          if (vertices[j] == [-1]):
            vertices[j] = [i + 2]
            edges[j] = [self.matrix[i][j]]
          else:
            v = 0
            while v < len(vertices[j]) and v < vertices[j][v]:
              v += 1
            vertices[j].insert(v, i + 2)
            edges[j].insert(v, self.matrix[i][j])

          # Row, add column index to its list of connected
          if (vertices[i + 1] == [-1]):
            vertices[i + 1] = [j + 1]
            edges[i + 1] = [self.matrix[i][j]]
          else:
            v = 0
            while v < len(vertices[i + 1]) and v < vertices[i + 1][v]:
              v += 1
            vertices[i + 1].insert(v, j + 1)
            edges[i + 1].insert(v, self.matrix[i][j])
    return (vertices, edges)

  '''
      This function traverses through the graph using 
      breadth-first and calculates the total weight of the
      resulting spanning tree.
      
      @return: the sum of the edge weights from the 
      generated spanning tree
  '''

  def BFS(self):
    vertices, edges = self.reformat()
    ## Set visited flags
    for e in vertices:
      e.append(False)

    weight = 0
    queue = [vertices[0]]
    ## This is a queue storing the previous vertex for the vertex in "queue"
    prevVertex = []
    ## Need to figure out how to add weights
    while (len(queue) > 0):
      vertex = queue.pop(0)
      # Find the index of vertex in vertices, add one
      vNum = vertices.index(vertex) + 1

      #If vertex isn't in visited
      if vertex[-1] != True:
        if (prevVertex != []):
          # Iterate over table to find what points to it and it's edge
          prev = prevVertex.pop(0)
          ## Go to index prev-1 (That's where vertex_prev is)
          for i in range(len(vertices[prev - 1])):
            ## Find vNum, should also be position of edge
            if vNum == vertices[prev - 1][i] and type(
                vertices[prev - 1][i]) == type(vNum):
              ## add edge to total
              weight += edges[prev - 1][i]
              break
        #mark vertex as visited (None)
        vertices[vNum - 1][-1] = True
        # for each vertex connected to vertex
        for i in range(len(vertex)):
          # if it isn't visited
          if vertices[vertex[i] - 1][-1] != True:
            # append vertex to queue
            queue.append(vertices[vertex[i] - 1])
            prevVertex.append(vNum)
      else:
        prevVertex.pop(0)
    return weight

  '''
      This function implements Prim's Algorithm to traverse
      this graph and calculates the weight of the resulting
      spanning tree.
      
      @return: the sum of the edge weights from the 
      generated spanning tree
  '''

  def Prim(self):
    vertices, edges = self.reformat()
    weight = 0
    visited = [False] * len(vertices)
    ## The starting node has been visited
    visited[0] = True
    for e in range(len(vertices) - 1):
      ## 100 is the max weight
      min = 101
      close = None
      ## iterate through vertices
      for i in range(len(vertices)):
        ## if vertex has been visited
        if (visited[i]):
          ## all adjacent vertices
          for j in range(len(vertices[i])):
            if not visited[vertices[i][j] - 1]:
              if min > edges[i][j]:
                min = edges[i][j]
                close = vertices[i][j]
      ## Close stores vertex numbers 1-n, so shift to 0-(n-1)
      if (close != None):
        visited[close - 1] = True
      weight += min
    return weight


'''
    @param b: Breadth-First search weight
    @param p: Prim's Minimum Spanning search weight

    This calculates the percentage by which b is greater than p.

    @return: returns the calculated precentage as float
'''


def diff(b, p):
  return (b / p * 100) - 100


'''
    @param k: The number of trials
    @param n: The number of vertices

    Calculates the average diff over k trials for graphs that
    have n vertices.

    @return: returns the average diff
'''


def test(k, n):
  sum = 0
  for i in range(k):
    graph1 = Graph(n)
    sum += diff(graph1.BFS(), graph1.Prim())

  return int(sum / k)


def main():
  print("Avg diff between BFS and Prim for a graph of 20 vertices is",
        str(test(10, 20)) + "%")
  print("Avg diff between BFS and Prim for a graph of 40 vertices is",
        str(test(10, 40)) + "%")
  print("Avg diff between BFS and Prim for a graph of 60 vertices is",
        str(test(10, 60)) + "%")


if __name__ == "__main__":
  main()
