"""動的計画法に使用するRooted Binary Treeのpython実装をclass化したもの。
   関数バージョンだとキャッシュの初期化を明示的に書かないといけないので、class化することでその問題を解消する"""

class CachedBinaryTree():
  """キャッシュを考慮したRooted Binary Treeクラス"""

  def __init__(self):
    """sourceはツリーを生成するための元になるItemのList"""
    self._cache = {}
  
  def max_value(self, source, avail):
    if (len(source), avail) in self._cache:
      result = self._cache[(len(source), avail)]
    elif source == [] or avail == 0:
      result = (0, [])
    elif source[0].weight > avail:
      # 右側の分岐のみを探索する
      result = self.max_value(source[1:], avail)
    else:
      next_item = source[0]
      # 左側の分岐を探索する
      with_value, with_to_take = self.max_value(source[1:], avail - next_item.weight)
      with_value += next_item.value
      # 右側の分岐を探索する
      without_value, without_to_take = self.max_value(source[1:], avail)
      if with_value > without_value:
        result = (with_value, with_to_take + [next_item,])
      else:
        result = (without_value, without_to_take)

    self._cache[(len(source), avail)] = result
    return result
