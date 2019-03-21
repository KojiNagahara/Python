"""ランダムウォーク問題の解法用に使用する場を表すオブジェクト。"""
from location import Location

class Field(object):
  def __init__(self):
    self.drunks = {}
  
  def add_drunk(self, drunk, location):
    if drunk in self.drunks:
      raise ValueError('重複オブジェクトを登録しようとした')
    else:
      self.drunks[drunk] = location

  def move_drunk(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('存在しないオブジェクトが指定された')
    x_distance, y_distance = drunk.take_step()
    current_location = self.drunks[drunk]
    self.drunks[drunk] = current_location.move(x_distance, y_distance)
  
  def get_location(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('存在しないオブジェクトが指定された')
    return self.drunks[drunk]