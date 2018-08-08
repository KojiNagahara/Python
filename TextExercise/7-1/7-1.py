def sumDigits(s):
    """sを文字列とする。
       文字列内に含まれる数値を合計した値を返す。"""
    sum = 0
    for c in s:
        try:
            sum += int(c)
        except ValueError:
            continue
    return sum

print('sumDigits(\'123\') :', sumDigits('123'))
print('sumDigits(\'a2b3c\') :', sumDigits('a2b3c'))
print('sumDigits(\'abc\') :', sumDigits('abc'))


