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


class ColdHater(Drunk):
  """寒いのが苦手なので南に行きたがる"""
  def take_step(self):
    step_choices = [(0,1),(0,-2),(1,0),(-1,0)]
    return random.choice(step_choices)


class SunFlower(Drunk):
  """太陽のいる方角（東か西）にしか行かない"""
  def take_step(self):
    step_choices = [(1,0),(-1,0)]
    return random.choice(step_choices)
