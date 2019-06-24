"""力づく実装のテスト用モジュール"""
from item import Item
from util import genPowerset
from chooser import chooseBest
import time

def buildItems():
    """データ初期化"""
    names = ['時計', '絵画', 'ラジオ', '花瓶', '本', 'PC']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]

    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def test(maxWeight=20):
    start = time.perf_counter()
    items = buildItems()
    pSet = genPowerset(items)
    taken, val = chooseBest(pSet, maxWeight)
    elapsed = time.perf_counter() - start
    print('取得した品物の価値:'+str(val))
    print('取得した品物:')
    for item in taken:
        print(item)
    print(f'処理にかかった時間:{elapsed}')


test()
test(5)
test(100)
