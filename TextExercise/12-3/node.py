"""グラフ最適化問題を解くためのノードなどの基本構造を定義する"""

class Node(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """srcとdestはどちらもNodeであるものとする"""
        self.src = src
        self.dest = dest
    
    def __str__(self):
        return self.src.name+"->"+self.dest.name

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """srcとdestはどちらもNode、weightは重みを表す実数とする"""
        Edge.__init__(self, src, dest)
        self.weight = weight
    
    def __str__(self):
        return self.src.name+"->("+self.weight+")"+self.dest.name
