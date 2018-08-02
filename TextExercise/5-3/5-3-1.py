def applyToEach(L, f):
    """Lをリスト、fを1つの引数を持つ関数であるものとする。
       Lのそれぞれの要素eをf(e)に置き換えてLを更新する"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, '-2', 3.14]
print('L =', L)

#absの事前条件を満たすためにいったんすべてfloatに変換
applyToEach(L, float)
print('L =', L)

applyToEach(L, abs)
print('L =', L)

applyToEach(L, int)
print('L =', L)
