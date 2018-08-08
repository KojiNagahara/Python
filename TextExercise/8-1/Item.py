class Item(object):
    """一般的な商品を表すクラス。"""
    #インスタンス変数は__priceと__name。
    #消費税の計算用に税率をクラス変数として保持

    taxRate = 0.08
    
    def __init__(self, name, price):
        """インスタンス生成時に商品名と税抜き価格を指定して初期化する"""
        self.__name = name
        self.__price = float(price)
    
    def __str__(self):
        """文字列表現を返す。"""
        return "{" + str(self.getName()) + ", " + str(self.getPrice()) + "}"
    
    def __eq__(self, other):
        return self.getName() == other.getName() and self.getPrice() == other.getPrice()

    def getName(self):
        """商品名を返す。"""
        return self.__name
    
    def getPrice(self):
        """税抜き価格を整数値で返す"""
        return int(self.__price)
    
    def getPriceWithTax(self):
        return int(self.__price*(1.0+Item.taxRate))



item = Item('リンゴ', 100)
print(item)
print('税込み価格は', item.getPriceWithTax())

def getItems():
    itemList = [Item('桃', 200), Item('ブドウ', 180), Item('梨', 150)]
    for oneItem in itemList:
        yield oneItem

for i in getItems():
    print(i)
