def isIn(t1, t2):
    if t1 in t2 or t2 in t1:
        return True
    else:
        return False

print('abcとabを引数に与えたisInの結果：', isIn('abc', 'ab'))
print('abとcaabbを引数に与えたisInの結果：', isIn('ab', 'caabb'))
print('abcとxyzを引数に与えたisInの結果：', isIn('abc', 'xyz'))