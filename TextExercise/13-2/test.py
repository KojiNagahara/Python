"""動的計画法の実装をテストするモジュール。"""
import random
from item import Item
from rootedBinaryTree import max_value, max_value_fast

def small_test():
  """小規模テスト"""
  names = ['a', 'b', 'c', 'd']
  values = [6, 7, 8, 9]
  weights = [3, 3, 2, 5]
  items = []
  for i in range(len(values)):
    items.append(Item(names[i], values[i], weights[i]))
  value, taken = max_value(items, 5)
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')

def build_many_items(number_of_items, max_value, max_weight):
  """big_test用のデータ作成自動化"""
  items = []
  for i in range(number_of_items):
    items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_value)))
  return items

def big_test(number_of_items):
  """大規模テスト。ただあまり大規模になると視認性が悪くなるので少し表示に工夫する必要はある"""
  items = build_many_items(number_of_items, 10, 10)
  print('対象Item：')
  for item in items:
    print(item)
  
  value, taken = max_value(items, 100)
  print('取得Item：')
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')

def big_test_fast(number_of_items):
  """大規模テスト。ただあまり大規模になると視認性が悪くなるので少し表示に工夫する必要はある"""
  items = build_many_items(number_of_items, 10, 10)
  print('対象Item：')
  for item in items:
    print(item)
  
  value, taken = max_value_fast(items, 100)
  print('取得Item：')
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')

print('small_testの実施結果')
small_test()
print('big_testの実施結果')
big_test(20)
print('big_test_fastの実施結果')
big_test_fast(20)
