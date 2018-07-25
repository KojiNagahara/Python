while True:
    originText = input('正の整数を入力してください ： ')
    if int(originText) <= 0 :
        print('正の整数だって言ってんだろ')
    else:
        break
# Javaの感覚だとoriginTextはwhile内のローカル変数に見えるけどPythonではそうではないらしい？
origin = int(originText)

# 演算に使用する変数
pwr = 2
root = origin
isFound = False

print('元の数', origin)
while pwr < 6 :
    while root > 1 :
        if origin == root**pwr :
            print('root', root, 'pwr', pwr)
            isFound = True
        root -= 1
    pwr += 1
    root = origin

if not isFound :
    print('該当する組み合わせは見つかりませんでした')

