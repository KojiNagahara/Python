def getThreeValue():
    return (1, 'text', 3.14)

#戻り値を受ける変数がタプルのデータ総数より少ない場合
first, second = getThreeValue()
print('最初の要素', first, '２番目の要素', second)

#戻り値を受ける変数がタプルのデータ総数より多い場合
first, second, third, fourth = getThreeValue()
print('最初の要素', first, '２番目の要素', second)
print('３番目の要素', third, '4番目の要素', fourth)
