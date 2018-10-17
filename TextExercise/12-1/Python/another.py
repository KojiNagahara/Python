"""Itemではないクラスでもgreedy.pyが有効であることを検証するためのクラス"""
class Another(object):
    """中身はItemと基本同じ"""
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
        return '['+self.__name+'] weight = '+str(self.__weight)+', value = '+str(self.__value)
