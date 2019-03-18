"""動的計画法に使用するRooted Binary Treeのpython実装"""

def max_value(to_consider, avail):
  """to_considerをItemのリスト、availを重さとする。
     それらをパラメータとする0/1ナップサック問題の解である
     総価値とItemのリストからなるタプルを返す"""
  if to_consider == [] or avail == 0:
    result = (0, [])
  elif to_consider[0].getWeight() > avail:
    # 右側の分岐のみを探索する
    result = max_value(to_consider[1:], avail)
  else:
    next_item = to_consider[0]
    # 左側の分岐を探索する
    with_value, with_to_take = max_value(to_consider[1:], avail-next_item.getWeight())
    with_value += next_item.getValue()
    # 右側の分岐を探索する
    without_value, without_to_take = max_value(to_consider[1:], avail)
    if with_value > without_value:
      result = (with_value, with_to_take+[next_item,])
    else:
      result = (without_value, without_to_take)

  return result