"""ランダムウォークの実行結果をプロットするためのモジュール"""
import pylab
from random_walk import simulate_walks, get_final_locations, get_path
from drunk import UsualDrunk, ColdHater, SunFlower

class StyleIterator(object):
  def __init__(self, styles):
    self.index = 0
    self.styles = styles
  
  def next_style(self):
    result = self.styles[self.index]
    if self.index == len(self.styles) - 1:
      self.index = 0
    else:
      self.index += 1
    return result


def simulate_drunks(trial_number, drunk, walk_lengths):
  mean_distances = []
  for step_number in walk_lengths:
    print(f'{step_number}ステップのシミュレーション開始：')
    trials = simulate_walks(step_number, trial_number, drunk)
    mean = sum(trials)/len(trials)
    mean_distances.append(mean)
  return mean_distances

def simulate_all(drunk_kinds, walk_lengths, trial_number):
  style_choice = StyleIterator(('m-', 'r:', 'k-.'))
  # 元ソースに日本語フォントの設定コードを追加。前提としてIPAフォントのインストールが必要。
  # 参考：https://qiita.com/hatunina/items/a77128c7f50b19ad2c51
  font = {'family':'Noto Sans CJK JP'}
  pylab.rc('font', **font)
  # 各クラス毎のプロット開始
  for drunk in drunk_kinds:
    current_style = style_choice.next_style()
    print(f'{drunk}クラスのシミュレーション開始')
    means = simulate_drunks(trial_number, drunk, walk_lengths)
    pylab.plot(walk_lengths, means, current_style, label=drunk.__name__)
    pylab.title(f'各クラスのランダムウォークの平均距離（試行回数{trial_number}回）')
    pylab.xlabel('歩数')
    pylab.ylabel('原点からの距離')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()
  # pylab.show()が自動実行される環境の場合はpylab.show()をコメントアウトする。
  pylab.show()

def plot_locations(drunk_kinds, step_number, trial_number):
  style_choice = StyleIterator(('k+', 'r^', 'mo'))
  # 元ソースに日本語フォントの設定コードを追加。前提としてIPAフォントのインストールが必要。
  # 参考：https://qiita.com/hatunina/items/a77128c7f50b19ad2c51
  font = {'family':'Noto Sans CJK JP'}
  pylab.rc('font', **font)
  # 各クラス毎のプロット開始
  for drunk in drunk_kinds:
    locations = get_final_locations(step_number, trial_number, drunk)
    x_values, y_values = [], []
    for location in locations:
      x_values.append(location.get_x())
      y_values.append(location.get_y())
    mean_x = sum(x_values)/len(x_values)
    mean_y = sum(y_values)/len(y_values)
    current_style = style_choice.next_style()
    pylab.plot(x_values, y_values, current_style,
      label=f'{drunk.__name__} 平均位置: <{mean_x}, {mean_y}>')
    pylab.title(f'{step_number}ステップ後の終了位置')
    pylab.xlabel('東西位置')
    pylab.ylabel('南北位置')
    pylab.legend(loc='lower left')
  # pylab.show()が自動実行される環境の場合はpylab.show()をコメントアウトする。
  pylab.show()

def trace_walk(drunk_kinds, step_number):
  style_choice = StyleIterator(('k+', 'r^', 'mo'))
  # 元ソースに日本語フォントの設定コードを追加。前提としてIPAフォントのインストールが必要。
  # 参考：https://qiita.com/hatunina/items/a77128c7f50b19ad2c51
  font = {'family':'Noto Sans CJK JP'}
  pylab.rc('font', **font)
  for drunk in drunk_kinds:
    locations = get_path(drunk, step_number)
    x_values, y_values = [], []
    for location in locations:
      x_values.append(location.get_x())
      y_values.append(location.get_y())
    current_style = style_choice.next_style()
    pylab.plot(x_values, y_values, current_style,
      label=f'{drunk.__name__}')
    pylab.title(f'{step_number}ステップ実行時のランダムウォークの軌跡')
    pylab.xlabel('東西位置')
    pylab.ylabel('南北位置')
    pylab.legend(loc='best')
  # pylab.show()が自動実行される環境の場合はpylab.show()をコメントアウトする。
  pylab.show()

if __name__ == '__main__':
  #simulate_all((UsualDrunk, ColdHater, SunFlower), (10, 100, 1000, 10000, 100000), 100)
  #plot_locations((UsualDrunk, ColdHater, SunFlower), 100, 200)
  trace_walk((UsualDrunk, ColdHater, SunFlower), 200)