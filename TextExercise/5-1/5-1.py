def findExtremeDivisors(n1, n2):
    """正の整数n1とn2の最小公約数 > 1と最大公約数から成るタプルを返す
    公約数がない場合(None, None)を返す。"""
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2)+1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisors(16, 32)
print('1より上の最小公約数', minDivisor, '最大公約数', maxDivisor)

divisors = findExtremeDivisors(9, 15)
print('1より上の最小公約数', divisors[0], '最大公約数', divisors[1])