from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError
import re

class GraphForm(FlaskForm):
  expression = StringField(u'式（Pythonで処理可能な式を記述してください）')
  a_value = IntegerField(u'aの値(省略時1)')
  b_value = IntegerField(u'bの値(省略時1)')
  c_value = IntegerField(u'cの値(省略時1)')
  x_start = IntegerField(u'x軸の開始値(省略時0)')
  x_end = IntegerField(u'x軸の終了値(省略時10)')

  def validate_expression(self, expression):
    """バリデーションの内容：
       空白禁止。"""
    if expression.data == '':
      print('check1')
      raise ValidationError("式は必須入力です")

  def validate_a_value(self, a_value):
    if a_value.data == None:
      a_value.data = 1

  def validate_b_value(self, b_value):
    if b_value.data == None:
      b_value.data = 1

  def validate_c_value(self, c_value):
    if c_value.data == None:
      c_value.data = 1

  def validate_x_start(self, x_start):
    if x_start.data == None:
      x_start.data = 0

  def validate_x_end(self, x_end):
    if x_end.data == None:
      x_end.data = 10

  def get_param(self):
    param = {}
    param['a_value'] = self.a_value.data
    param['b_value'] = self.b_value.data
    param['c_value'] = self.c_value.data
    param['start'] = self.x_start.data
    param['end'] = self.x_end.data
    return param
