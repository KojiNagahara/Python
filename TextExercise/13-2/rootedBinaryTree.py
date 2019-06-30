"""動的計画法に使用するRooted Binary Treeのpython実装。
　 このツリーでは個々のList要素に対して拾う（左側と呼称）-拾わない（右側と呼称）と
   決定した場合についての組み合わせをBinary Treeとして再帰的に表現する。
   当然、対象のList要素を拾った場合に重量オーバーになる場合はそれ以上の左側の評価は
   無駄なので、拾わない（右側）場合のツリーのみを評価対象として再帰を続けていく。
   一度導出したツリーの構造が他の部分でも導出されることが十分に予想されるので
   max_value_fastでは使う/使わないにかかわらず一度導出したツリー構造をキャッシュすることで
   高速化を図っている。これはListの要素数が増えれば増えるほど有効に働く。"""

def max_value(to_consider, avail):
  """to_considerをItemのリスト、availを重さとする。
     それらをパラメータとする0/1ナップサック問題の解である
     総価値とItemのリストからなるタプルを返す"""
  if to_consider == [] or avail == 0:
    result = (0, [])
  elif to_consider[0].weight > avail:
    # 右側の分岐のみを探索する
    result = max_value(to_consider[1:], avail)
  else:
    next_item = to_consider[0]
    # 左側の分岐を探索する
    with_value, with_to_take = max_value(to_consider[1:], avail - next_item.weight)
    with_value += next_item.value
    # 右側の分岐を探索する
    without_value, without_to_take = max_value(to_consider[1:], avail)
    # 左側と右側の探索結果でより価値の高い方を採用する
    if with_value > without_value:
      result = (with_value, with_to_take + [next_item,])
    else:
      result = (without_value, without_to_take)

  return result

def max_value_fast(to_consider, avail, memo = {}):
  """max_valueのキャッシュを利用した高速化実装。
     memoに一度計算した内容を含めておくことで再計算を省く。"""
  if (len(to_consider), avail) in memo:
    result = memo[(len(to_consider), avail)]
  elif to_consider == [] or avail == 0:
    result = (0, [])
  elif to_consider[0].weight > avail:
    # 右側の分岐のみを探索する
    result = max_value_fast(to_consider[1:], avail, memo)
  else:
    next_item = to_consider[0]
    # 左側の分岐を探索する
    with_value, with_to_take = max_value_fast(to_consider[1:], avail - next_item.weight, memo)
    with_value += next_item.value
    # 右側の分岐を探索する
    without_value, without_to_take = max_value_fast(to_consider[1:], avail, memo)
    # 左側と右側の探索結果でより価値の高い方を採用する
    if with_value > without_value:
      result = (with_value, with_to_take + [next_item,])
    else:
      result = (without_value, without_to_take)

  memo[(len(to_consider), avail)] = result
  return result
