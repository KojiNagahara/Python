"""有向グラフと双方向グラフの実装"""

from node import Edge

class Digraph(object):
    """有向グラフの実装"""
    #nodesはNodeオブジェクトのList。
    #edgesは各nodeと子ノードへのマップするためのDictionary。
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
        src = edge.src
        dest = edge.dest
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Nodeがグラフに含まれていない')
        self._edges[src].append(dest)
    
    def childrenOf(self, node):
        return self._edges[node]
    
    def hasNode(self, node):
        return node in self._nodes
    
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self.childrenOf(src):
                result = result+src.name+'->'+dest.name+'\n'
        
        return result[:-1]

class Graph(Digraph):
    """双方向グラフの実装"""
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.dest, edge.src)
        Digraph.addEdge(self, rev)
