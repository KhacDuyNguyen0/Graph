from collections import deque

class Vertex:
    def __init__(self, key, color="white", distance=float("inf"), pred=None, discovery=0, finish=0):
        self.id = key
        self.connectedTo = {}
        self.color = color
        self.distance = distance
        self.pred = pred
        self.discovery = discovery
        self.finish = finish

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance
    
    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred
    
    def setDiscovery(self, discovery):
        self.discovery = discovery

    def getDiscovery(self):
        return self.discovery

    def setFinish(self, finish):
        self.finish = finish

    def getFinish(self):
        return self.finish   

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    
    def __iter__(self):
        return iter(self.vertList.values())
    
class BFSGraph(Graph):
    def __init__(self):
        super().__init__()

    def bfs(self, start: Vertex):
        start.setDistance(0)
        start.setPred(None)
        start.setColor("gray")
        vertQueue = deque([start])
        while vertQueue:
            currentVert = vertQueue.popleft()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == "white"):
                    nbr.setColor("gray")
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.append(nbr)
            currentVert.setColor("black")    

    def traverse(self, y):
        x = y
        result = []
        while (x.getPred()):
            result.append(x.getId())
            # print(x.getId())
            x = x.getPred()
        result.append(x.getId())
        # print(x.getId())
        return result
    
class DFSGrpah(Graph):    
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        print(startVertex.getId(), end=" ")
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == "white":
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)

def bfsGraph():
    g = BFSGraph()
    for i in range(1, 15): 
        g.addVertex(i)
    
    g.addEdge(1, 2) 
    g.addEdge(1, 3) 
    g.addEdge(1, 4) 
    g.addEdge(2, 5) 
    g.addEdge(2, 6) 
    g.addEdge(4, 7) 
    g.addEdge(4, 8) 
    g.addEdge(4, 9) 
    g.addEdge(6, 10)
    g.addEdge(6, 11) 
    g.addEdge(8, 12) 
    g.addEdge(8, 13) 
    g.addEdge(9, 14)
    g.addEdge(12, 15)  

    print("The representation of this graph:")
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    
    print("Following is Breadth First Search (from vertex 1 to vertex 15)")
    g.bfs(g.getVertex(1))
    # printPath(g, g.getVertex(1), g.getVertex(15))
    print(list(reversed(g.traverse(g.getVertex(15)))))

def dfsGraph():
    g = DFSGrpah()

    for i in range(1, 15): 
        g.addVertex(i) 

    g.addEdge(1, 2) 
    g.addEdge(1, 3) 
    g.addEdge(1, 4) 
    g.addEdge(2, 5) 
    g.addEdge(2, 6) 
    g.addEdge(4, 7) 
    g.addEdge(4, 8) 
    g.addEdge(4, 9) 
    g.addEdge(6, 10)
    g.addEdge(6, 11) 
    g.addEdge(8, 12) 
    g.addEdge(8, 13) 
    g.addEdge(9, 14)
    g.addEdge(12, 15) 

    print("The representation of this graph:")
    for v in g: 
        for w in v.getConnections(): 
            print("( %s , %s )" % (v.getId(), w.getId())) 
    print("Following is Depth First Search (starting from vertex 1)") 
    g.dfs()
    
def printPath(g, s, v):
    if v.getId() == s.getId():
        print(s.getId())
    elif v.getPred() == None:
        print('No path from "%s" to "%s"' % (s.getId(), v.getId()))
    else:
        printPath(g, s, v.getPred())
        print(v.getId())

def buildGraph(wList):
    d = {}
    g = Graph()
    for line in wList:
        word = line[:]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def firstGraph():    
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

def secondGraph():
    wList = ["FOOD", "FOOT", "FOOL", "FORT", "GOOD", "PALE", "PALM", "POLE", "POLL", "POOL", "SAGE", "SALE", "SALT"]
    g = buildGraph(wList)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

def main():
    # firstGraph()
    # secondGraph()
    bfsGraph()
    dfsGraph()


if __name__ == '__main__':
    main()


