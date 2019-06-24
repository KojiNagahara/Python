from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError
import re

class GraphForm(FlaskForm):
  expression = StringField(u'式（Pythonで処理可能な式を記述してください）')
  a_value = IntegerField(u'aの値')
  b_value = IntegerField(u'bの値')
  c_value = IntegerField(u'cの値')
  x_start = IntegerField(u'x軸の開始値')
  x_end = IntegerField(u'x軸の終了値')

  def validate_expression(self, expression):
    """バリデーションの内容：
       空白禁止。
       数式を構成する演算子およびx,a,b,cと数字以外の文字禁止"""
    if expression.data == '':
      raise ValidationError('式は必須入力です')
    
    pattern = '[^0-9abcx\+\-\*\/%()\.]'
    if re.match(pattern, expression.data):
      raise ValidationError('有効な式を指定してください')
    
    divide_zero = '.*/0.*'
    if re.match(divide_zero, expression.data):
      raise ValidationError('0による割り算が式に含まれています')

  def get_param(self):
    param = {}
    param['a_value'] = self.a_value.data
    param['b_value'] = self.b_value.data
    param['c_value'] = self.c_value.data
    param['start'] = self.x_start.data
    param['end'] = self.x_end.data
    return param
