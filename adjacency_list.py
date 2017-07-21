'''
Edge object representing a buyer or a seller. Has string method for debugging
'''
class Edge(object):

    def __init__(self, vId, uId):
        self.v = vId
        self.u = uId
        self.geography = set()
        self.industry = set()
        self.weight = None
    
    def __str__(self):
        g = self.geography
        i = self.industry
        w = self.weight
        u = self.u
        return "Match Id: {}\nGeographies: {}\nIndustries: {}\nWeight: {}".format(u, g, i, w)

'''
Node object representing a buyer or a seller. Has string method for debugging
'''
class Node(object):

    def __init__(self, nId, nType):
        self.id = nId
        self.type = nType
        self.edges = {}
    
    def __str__(self):
        output = []
        output.append('Node Id: {} | Node Type: {}'.format(self.id, self.type))
        for e in self.edges.values():
            output.append(str(e))
        output.append('============================')
        return '\n\n'.join(output)

'''
Undirected graph. Nodes are sellers and buyers. 
Edges represent matches and corresponding weights
'''
class Graph(object):

    def __init__(self):
        self.adj = {}

    # Add node to adjacency list
    def addNode(self, nId, nType):
        if nId not in self.adj:
            self.adj[nId] = Node(nId, nType)
        return self.adj[nId]

    # Get not from adjaceny list
    def getNode(self, nId):
        # Check that node exists
        if nId not in self.adj:
            raise KeyError('Node missing from graph.')
        return self.adj[nId]

    # Add directed edge from seller to buyer tand back
    def addEdge(self, sellerId, buyerId, geo, ind):
        self.addDirectedEdge(sellerId, buyerId, geo, ind, 'seller')
        self.addDirectedEdge(buyerId, sellerId, geo, ind, 'buyer')

    # Add directed from one vertex to another
    def addDirectedEdge(self, vId, uId, geo, ind, nType):
        # Create node if necessary
        self.addNode(vId, nType)

        # Get node and edges dictionary associated with from node id
        node = self.getNode(vId)
        edges = node.edges

        # Get or add edge between vertices
        try:
            edge = edges[uId]
        except KeyError:
            edge = Edge(vId, uId)
            edges[uId] = edge
        
        edge.geography.add(geo)
        edge.industry.add(ind)
        edge.weight = len(edge.geography) + len(edge.industry)

    # Returns a sorted list of nodes from adj dictionary
    def getNodes(self):
        nodes = list(self.adj.values())
        nodes.sort(key=lambda n: n.id)
        return nodes

    # Return a sorted list of edges adjacent to given node
    def getSortedEdges(self, node):
        # Generates list from dict of node's outgoing edges
        edges = list(node.edges.values())

        # Sort list of edges by weight (hi-low), then id of edge's other end (A-Z)
        edges.sort(key=lambda e: (-e.weight, e.u))

        return edges

        