"""ランダムウォークに登場する酔っ払いを表すオブジェクト"""
import random

class Drunk(object):
  def __init__(self, name = None):
    self.name = name
  
  def __str__(self):
    if self.name != None:
      return self.name
    return 'Anonymous'
  
class UsualDrunk(Drunk):
  def take_step(self):
    step_choices = [(0,1),(0,-1),(1,0),(-1,0)]
    return random.choice(step_choices)
