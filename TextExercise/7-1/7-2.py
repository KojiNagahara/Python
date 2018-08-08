def findAnEven(L):
    """Lをint型の要素を持つリストとする。
       Lに最初に現れる偶数を返す。
       Lが偶数を含まなければValueErrorを引き起こす。"""
    evenList = [x for x in L if x%2 ==0]
    if len(evenList) == 0:
        raise ValueError('Lに奇数しか含まれていません。')
    else:
        return evenList[0]

try:
    source = [1, 2, 3, 4, 5]
    print(source)
    print('findAnEven(source) :', findAnEven(source))

    source = [1, 3, 5]
    print(source)
    print('findAnEven(source) :', findAnEven(source))
except (ValueError) as msg:
    print('Exception raised. msg:', msg)

try:
    source = [1, '3', 5]
    print(source)
    print('findAnEven(source) :', findAnEven(source))
except (TypeError) as msg:
    print('Exception raised. msg:', msg)