"""力づくで解くアルゴリズムの実装"""
from item import Item
from util import genPowerset

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

def buildItems():
    """データ初期化"""
    names = ['時計', '絵画', 'ラジオ', '花瓶', '本', 'PC']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def test(maxWeight = 20):
    items = buildItems()
    pSet = genPowerset(items)
    taken, val = chooseBest(pSet, maxWeight, Item.getValue, Item.getWeight)
    print('取得した品物の価値:'+str(val))
    print('取得した品物:')
    for item in taken:
        print(item)

test()