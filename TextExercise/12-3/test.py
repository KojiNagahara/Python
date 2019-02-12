from node import Node, Edge
from graph import Digraph
from shortest import shortestPath, printPath, BFS

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node('ノード'+str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], toPrint=True)
    print('DFSで発見された最短経路:', printPath(sp))
    sp = BFS(g, nodes[0], nodes[5], toPrint=True)
    print('BFSで発見された最短経路:', printPath(sp))

testSP()
