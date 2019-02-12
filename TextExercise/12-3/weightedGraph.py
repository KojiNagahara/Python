"""重み付き有向グラフの実装。"""

from node import WeightedEdge

class WeightedGraph(object):
    """edgesのDictionaryのvalueをtupleで実装"""
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Nodeが重複している')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def addEdge(self, edge):
        """edgeがWeightedEdgeであることが前提"""
        src = edge.getSource()
        dest = edge.getDestination()
        weight = edge.getWeight()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Nodeがグラフに含まれていない')
        self.edges[src].append((dest, weight))
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.childrenOf(src):
                result = result+src.getName()+'->('+dest[1]+')'+dest[0].getName()+'\n'
        
        return result[:-1]
