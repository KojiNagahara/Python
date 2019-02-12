"""力づくで解くアルゴリズムの実装"""

def chooseBest(pSet, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pSet:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)
