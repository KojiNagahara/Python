origin = '1.4, 19.2, 7.8'

textList = origin.split(',')
total = 0.0
for i in range(0, len(textList)) :
    total += float(textList[i])

print('合計は', total)