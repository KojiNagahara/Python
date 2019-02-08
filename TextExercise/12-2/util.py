"""べき集合の生成に関するユーティリティ"""

def getBinaryRep(n, num_digits):
    """nとnum_digitsが非負のint型とし、
       nの値をnum_digits桁の２進数であらわす文字列を返す"""
    result = ''
    while n > 0 :
        result = str(n%2)+result
        n = n//2
    if len(result) > num_digits :
        raise ValueError('桁数が足りません:'+str(num_digits))
    
    for i in range(num_digits - len(result)) :
        result = '0'+result
    
    return result

def genPowerset(L):
    """Lをリストとする。
       Lの要素のすべての可能な組み合わせから成るリストを返す"""
    
    powerset = []

    for i in range(1, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []

        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])

        powerset.append(subset)

    return powerset
