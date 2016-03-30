class Graphs():
    def __init__(self):
        self.vertex_list = {}
        self.v_no = 0

    def addVertex(self, key):
        self.v_no += 1 # i don't know why they are keeping this value
        vertex = Vertex(key)
        self.vertex_list[key] = vertex

    def getvertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def getvertices(self):
        return self.vertex_list.keys()

    def addEdges(self, f, d, w):
        if f not in self.vertex_list:
            nv = self.addVertex(f)
        if d not in self.vertex_list:
            nv = self.addVertex(d)
        self.vertex_list[f].addNeighbor(d, w)

    def __iter__(self):
        return iter(self.vertex_list.values())

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def addNeighbor(self, nbr, w):
        self.connectedTo[nbr] = w


    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


g = Graphs()
for i in range(6):
    g.addVertex(i)
all_vertices = g.getvertices()

vertex_data = g.getvertex(2)
print "All vertices", all_vertices
print "vertex", vertex_data
print "vertex list ", g.vertex_list

g.addEdges(1,2,4)
g.addEdges(2,3,9)
g.addEdges(3,4,7)
g.addEdges(3,5,3)
g.addEdges(4,0,1)
g.addEdges(5,4,8)

