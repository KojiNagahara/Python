"""動的計画法のクラス実装をテストするモジュール。"""
import random
import time
from item import Item
from binaryTree import CachedBinaryTree

def build_items():
  names = ['時計', '絵画', 'ラジオ', '花瓶', '本', 'PC']
  values = [175, 90, 20, 50, 10, 200]
  weights = [10, 9, 4, 2, 1, 20]
  items = []
  for i in range(len(values)):
    items.append(Item(names[i], values[i], weights[i]))
  return items

def build_many_items(number_of_items, max_value, max_weight):
  """test用のデータ作成自動化"""
  items = []
  for i in range(number_of_items):
    items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_value)))
  return items

def test(items, avail):
  """クラスを利用したテスト。"""
  start = time.perf_counter()
  print('対象Item：')
  for item in items:
    print(item)
  
  tree = CachedBinaryTree()
  value, taken = tree.max_value(items, avail)
  elapsed = time.perf_counter() - start
  print('取得Item：')
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')
  print(f'処理にかかった時間:{elapsed}')


print('小規模テスト')
test(build_items(), 20)
print('大規模テスト')
test(build_many_items(20, 10, 10), 50)
