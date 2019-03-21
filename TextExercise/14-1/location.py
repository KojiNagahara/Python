"""ランダムウォーク問題の解法用に使用する位置を表すオブジェクト。"""

class Location(object):
  def __init__(self, x, y):
    """x,yは浮動小数点数"""
    self.x, self.y = x, y
  
  def move(self, delta_x, delta_y):
    """delta_x,delta_yは浮動小数点数"""
    return Location(self.x+delta_x, self.y+delta_y)
  
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y
  
  def distance_from(self, other):
    """otherはLocationオブジェクト"""
    ox, oy = other.get_x(), other.get_y()
    x_distance, y_distance = self.x - ox, self.y - oy
    return (x_distance**2+y_distance**2)**0.5
  
  def __str__(self):
    return f'<{self.x}, {self.y}>'
