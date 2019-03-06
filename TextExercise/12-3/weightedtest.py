from node import Node, WeightedEdge
from weightedGraph import WeightedGraph
from shortest import weightedBFS, printWeightedPath

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node('ノード'+str(name)))
    g = WeightedGraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(WeightedEdge(nodes[0], nodes[1], weight=100.0))
    g.addEdge(WeightedEdge(nodes[0], nodes[2], weight=110.0))
    g.addEdge(WeightedEdge(nodes[1], nodes[3], weight=140.0))
    g.addEdge(WeightedEdge(nodes[2], nodes[3], weight=120.0))
    g.addEdge(WeightedEdge(nodes[0], nodes[4], weight=30.0))
    g.addEdge(WeightedEdge(nodes[4], nodes[5], weight=50.0))
    g.addEdge(WeightedEdge(nodes[5], nodes[3], weight=10.0))
    sp, weight = weightedBFS(g, nodes[0], nodes[3], toPrint=True)
    print('重みづけされたグラフに対するBFSで発見された最短経路の重み合計:', weight)
    print('重みづけされたグラフに対するBFSで発見された最短経路:', printWeightedPath(sp))

testSP()
