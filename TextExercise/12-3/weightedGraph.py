"""重み付き有向グラフの実装。"""

from node import WeightedEdge

class WeightedGraph(object):
    """edgesのDictionaryのvalueをtupleで実装"""
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def addNode(self, node):
        if node in self._nodes:
            raise ValueError('Nodeが重複している')
        else:
            self._nodes.append(node)
            self._edges[node] = []
    
    def addEdge(self, edge):
        """edgeがWeightedEdgeであることが前提"""
        src = edge.src
        dest = edge.dest
        weight = edge.weight
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Nodeがグラフに含まれていない')
        self._edges[src].append((dest, weight))
    
    def childrenOf(self, node):
        return self._edges[node]
    
    def hasNode(self, node):
        return node in self._nodes
    
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self.childrenOf(src):
                result = result+src.name+'->('+dest[1]+')'+dest[0].name+'\n'
        
        return result[:-1]
