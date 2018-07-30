def isPrime(target):
    """簡単な素数判定。素数ならTrue、素数でなければFalseを返す"""
    for n in range(2, target):
        if target%n == 0:
            return False
    return True

#リスト内包（単純な演算）
simple = [x**2 for x in range(1, 6)]
print(simple)

#リスト内包（条件によるデータ抽出：素数の2乗をリストに抽出）
onlyPrime = [x**2 for x in range(2, 11) if isPrime(x)]
print(onlyPrime)

