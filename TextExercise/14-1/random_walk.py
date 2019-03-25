"""ランダムウォークの実行ロジックの記述"""
from field import Field
from location import Location
from drunk import UsualDrunk, ColdHater, SunFlower

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

def get_final_locations(step_number, trial_number, drunk):
  locations = []
  d = drunk()
  for t in range(trial_number):
    f = Field()
    f.add_drunk(d, Location(0, 0))
    for s in range(step_number):
      f.move_drunk(d)
    locations.append(f.get_location(d))
  return locations

def get_path(drunk, step_number):
  locations = []
  d = drunk()
  f = Field()
  f.add_drunk(d, Location(0, 0))
  for step in range(step_number):
    f.move_drunk(d)
    locations.append(f.get_location(d))
  return locations
  

def test(walk_lengths, trial_number, drunk):
  for step_number in walk_lengths:
    distances = simulate_walks(step_number, trial_number, drunk)
    print(f'{drunk.__name__}クラスを使用した{step_number}回のランダムウォーク(試行回数{trial_number}回)の実行結果：')
    print('平均移動距離 = ', round(sum(distances)/len(distances), 4))
    print('最大移動距離 = ', max(distances), ', 最小移動距離 = ', min(distances))

def simulate_all(drunk_kinds, walk_lengths, trial_number):
  for class_name in drunk_kinds:
    test(walk_lengths, trial_number, class_name)

if __name__ == '__main__':
  #test((10, 100, 1000, 10000), 100, UsualDrunk)
  simulate_all((UsualDrunk, ColdHater, SunFlower), (100, 1000), 10)