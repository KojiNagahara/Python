"""貪欲アルゴリズムで使用するItemクラスとそれにまつわる関数の定義"""

class Item():
    """ナップサックに詰める対象の品物"""
    def __init__(self, n, v, w):
        """初期化。weightについては割り算の分母になるのと質量なので０以下の値は入れない"""
        self.__name = n
        self.__value = v
        if float(w) <= 0.0:
            raise ValueError(v)
        self.__weight = w

    def getName(self):
        """名前取得"""
        return self.__name

    def getWeight(self):
        """質量取得"""
        return self.__weight

    def getValue(self):
        """価値取得"""
        return self.__value

    def __str__(self):
        """文字列表現"""
        return f'[{self.name}] weight = {self.weight}, value = {self.value}'

def value(item):
    """「価値の高いもの」を基準に取る場合"""
    return item.getValue()

def weightInverse(item):
    """「重量の軽いもの」を基準に取る場合"""
    return 1.0/item.getWeight()

def density(item):
    """「価値/重量比」を基準に取る場合"""
    return item.getValue()/item.getWeight()
