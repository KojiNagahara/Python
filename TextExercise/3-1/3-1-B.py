while True:
    origin = int(input('正の整数を入力してください ： '))
    if origin > 0 :
        break
    print('正の整数だって言ってんだろ')

found = False
print('元の数', origin)
for pwr in range(2, 6) :
    for root in range(origin, 1, -1) :
        if origin == root**pwr :
            print('root', root, 'pwr', pwr)
            found = True

if not found :
    print('該当する組み合わせは見つかりませんでした')

