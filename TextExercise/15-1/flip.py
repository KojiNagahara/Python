"""コイン投げのシミュレーションによる大数の法則の確認"""
import random

def flip(number):
  """numberは正の整数"""
  heads = 0
  for i in range(number):
    if random.choice(('H', 'T')) == 'H':
      heads += 1
  return heads/number

def simulate(flip_number, trial_number):
  """number_for_trial、trial_numberともに正の整数"""
  frac_heads = []
  for i in range(trial_number):
    frac_heads.append(flip(flip_number))
  mean = sum(frac_heads)/len(frac_heads)
  return mean

if __name__ == '__main__':
  for i in range(10):
    print(f'コイン投げ10回の試行の平均：{simulate(10, 1)}')
  for i in range(10):
    print(f'コイン投げ10回の試行を100回実行した場合の平均：{simulate(10, 100)}')
  print(f'コイン投げ100回の試行を10000回実行した場合の平均：{simulate(100, 10000)}')
  print(f'コイン投げ100回の試行を10000回実行した場合の平均：{simulate(100, 10000)}')