"""貪欲アルゴリズムのテスト実行用モジュール"""
from item import Item, value, weightInverse, density
from greedy import greedy

def buildItems():
    """データ初期化"""
    names = ['時計', '絵画', 'ラジオ', '花瓶', '本', 'PC']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def testGreedy(items, maxWeight, keyFunction):
    """各ソート基準を使ったアルゴリズム実行のテスト"""
    taken, val = greedy(items, maxWeight, keyFunction)
    print('取得した品物の総価値 : ', val)
    for item in taken:
        print(' ', item)

def testGreedys(maxWeight = 20):
    """テストのエントリポイント"""
    items = buildItems()
    print('価値を基準としたアルゴリズム実行の結果 ...')
    testGreedy(items, maxWeight, value)
    print('重量を基準としたアルゴリズム実行の結果 ...')
    testGreedy(items, maxWeight, weightInverse)
    print('価値/重量比を基準としたアルゴリズム実行の結果 ...')
    testGreedy(items, maxWeight, density)

testGreedys()
