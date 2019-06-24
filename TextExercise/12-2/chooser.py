"""力づくで解くアルゴリズムの実装"""

def chooseBest(pSet, maxWeight):
    bestVal = 0.0
    bestSet = None
    for items in pSet:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += item.value
            itemsWeight += item.weight
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)
