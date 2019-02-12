"""有向グラフと双方向グラフの実装"""

from node import Edge

class Digraph(object):
    """有向グラフの実装"""
    #nodesはNodeオブジェクトのList。
    #edgesは各nodeと子ノードへのマップするためのDictionary。
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
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Nodeがグラフに含まれていない')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.childrenOf(src):
                result = result+src.getName()+'->'+dest.getName()+'\n'
        
        return result[:-1]

class Graph(Digraph):
    """双方向グラフの実装"""
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
