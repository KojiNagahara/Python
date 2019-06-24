"""動的計画法で使用するItemクラスとそれにまつわる関数の定義"""

class Item(object):
    """ナップサックに詰める対象の品物"""
    def __init__(self, n, v, w):
        """初期化。weightについては割り算の分母になるのと質量なので０以下の値は入れない"""
        self.name = n
        self.value = v
        self.weight = w
        self.density = v/w

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        if float(w) <= 0.0:
            raise ValueError(w)
        self.__weight = w

    def __str__(self):
        """文字列表現"""
        return f'[{self.name}] weight = {self.weight}, value = {self.value}'
