"""グラフ最適化問題を解くためのノードなどの基本構造を定義する"""

class Node(object):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """srcとdestはどちらもNodeであるものとする"""
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName()+"->"+self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """srcとdestはどちらもNode、weightは重みを表す実数とする"""
        Edge.__init__(self, src, dest)
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return self.src.getName()+"->("+self.getWeight()+")"+self.dest.getName()
