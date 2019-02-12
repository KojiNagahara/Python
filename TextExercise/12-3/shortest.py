"""最短経路問題の解法の実装"""

def printPath(path):
    """pathはNodeのList"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i][0])
        if i != len(path)-1:
            result = result + '->'
    return result

def printWeightedPath(path):
    """pathは(Node, weight)のtupleのList"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i][0])
        if i != len(path)-1:
            result = result + '->(' + str(path[i+1][1]) + ')'
    return result

def getWeight(path):
    """pathは(Node, weight)形式のtupleのList"""
    total = 0.0
    for node, weight in path:
        total += weight
    return total

def DFS(graph, start, end, path, shortest, toPrint=False):
    """graphはDigraphオブジェクト、startとendはNodeオブジェクト
       pathとshortestはNodeのリストとする。
       graph上の最短経路を返す再帰的深さ優先探索の実装。"""
    path = path + [start]
    if toPrint:
        print('現在のDFS path', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    """DFSの最短経路探索用のインターフェース。
       graphはDigraphオブジェクト、startとendはNodeオブジェクトとし、
       toPrintで途中経過を表示するかどうか制御する。"""
    return DFS(graph, start, end, [], None, toPrint)

def BFS(graph, start, end, toPrint=False):
    """幅優先探索の実装。
       graphはDigraphオブジェクト、startとendはNodeオブジェクトとし、
       toPrintで途中経過を表示するかどうか制御する。"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('現在のBFS path', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)    
    return None

def weightedBFS(graph, start, end, toPrint=False):
    """重み付きグラフに対する幅優先探索の実装。
       graphはWeightedGraphオブジェクト、startとendはNodeオブジェクトとし、
       toPrintで途中経過を表示するかどうか制御する。"""
    initPath = [(start, 0)]
    pathQueue = [initPath]
    bestPath = []
    bestWeight = 0.0
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('現在の重み付きBFS path', printWeightedPath(tmpPath))
        lastNode, lastWeight = tmpPath[-1]
        if lastNode == end:
            tmpWeight = getWeight(tmpPath)
            if bestWeight == 0.0 or tmpWeight < bestWeight:
                bestPath = tmpPath
                bestWeight = tmpWeight
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append((newPath))
    
    return (bestPath, bestWeight)
