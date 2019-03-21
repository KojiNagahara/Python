"""ランダムウォークの実行ロジックの記述"""
from field import Field
from location import Location
from drunk import UsualDrunk

def walk(field, drunk, step_number):
  """field:Fieldインスタンス
     drunk:Drunkサブクラスのインスタンス
     step_number:0以上の整数
     step_number回移動するランダムウォークを実行する"""
  start = field.get_location(drunk)
  for step in range(step_number):
    field.move_drunk(drunk)
  return start.distance_from(field.get_location(drunk))

def simulate_walks(step_number, trial_number, drunk):
  """step_number:0以上の整数
     trial_number:正の整数
     drunk:Drunkのサブクラスのインスタンス
     step_number回移動するランダムウォークをtrial_number回シミュレートする。
     各シミュレートの初期位置と終了位置をリストとして返す"""
  homer = drunk()
  origin = Location(0, 0)
  distances = []
  for trial in range(trial_number):
    f = Field()
    f.add_drunk(homer, origin)
    distances.append(round(walk(f, homer, step_number), 1))
  return distances

def test(walk_lengths, trial_number, drunk):
  for step_number in walk_lengths:
    distances = simulate_walks(step_number, trial_number, drunk)
    print(f'{drunk.__name__}クラスを使用した{step_number}回のランダムウォークの実行結果：')
    print('平均移動距離 = ', round(sum(distances)/len(distances), 4))
    print('最大移動距離 = ', max(distances), ', 最小移動距離 = ', min(distances))


test((10, 100, 1000, 10000), 100, UsualDrunk)
