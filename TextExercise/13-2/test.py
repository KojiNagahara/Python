"""動的計画法の実装をテストするモジュール。"""
import random
import time
from item import Item
from rootedBinaryTree import max_value, max_value_fast

def build_items():
  names = ['時計', '絵画', 'ラジオ', '花瓶', '本', 'PC']
  values = [175, 90, 20, 50, 10, 200]
  weights = [10, 9, 4, 2, 1, 20]
  items = []
  for i in range(len(values)):
    items.append(Item(names[i], values[i], weights[i]))
  return items

def small_test(chooser):
  """小規模テスト"""
  start = time.perf_counter()
  items = build_items()
  value, taken = chooser(items, 20)
  elapsed = time.perf_counter() - start
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')
  print(f'処理にかかった時間:{elapsed}')

def build_many_items(number_of_items, max_value, max_weight):
  """big_test用のデータ作成自動化"""
  items = []
  for i in range(number_of_items):
    items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_value)))
  return items

def big_test(items):
  """大規模テスト。ただあまり大規模になると結果の視認性が悪くなるので少し表示に工夫したい"""
  start = time.perf_counter()
  print('対象Item：')
  for item in items:
    print(item)
  
  value, taken = max_value(items, 100)
  elapsed = time.perf_counter() - start
  print('取得Item：')
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')
  print(f'処理にかかった時間:{elapsed}')

def big_test_fast(items):
  """大規模テスト。small_testと同様の実装方針だとmax_value_fastのキャッシュが残ってしまってできなかった"""
  start = time.perf_counter()
  print('対象Item：')
  for item in items:
    print(item)
  
  value, taken = max_value_fast(items, 100, {})
  elapsed = time.perf_counter() - start
  print('取得Item：')
  for item in taken:
    print(item)
  print(f'取得したItemの総価値：{value}')
  print(f'処理にかかった時間:{elapsed}')


print('small_testの実施結果')
small_test(max_value)
print('高速化したアルゴリズムを用いたsmall_testの実施結果')
small_test(max_value_fast)

items = build_many_items(20, 10, 10)
print('big_testの実施結果')
big_test(items)
print('高速化したアルゴリズムを用いたbig_testの実施結果')
big_test_fast(items)
