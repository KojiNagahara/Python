def fastFib(n, memo = {}):
    """一度計算した結果をキャッシュしてフィボナッチ数列を計算する"""
    if n == 0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

print(fastFib(0))
print(fastFib(1))
print(fastFib(2))
print(fastFib(5))
print(fastFib(10))
print(fastFib(50))
print(fastFib(100))
