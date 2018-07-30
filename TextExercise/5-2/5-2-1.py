import copy

source = [1, 2, 3, 4, 5]

print('id(source) =', id(source))

#スライス表記を使ったクローン
for value in source[1:3]:
    print(value)

print()

#list(L)を使ったクローン
copied = list(source)
for value in copied:
    print(value)
print('id(copied) =', id(copied))

print()

#copy.deepCopyを使ったクローン
deep = copy.deepcopy(source)
for value in deep:
    print(value)
print('id(deep) =', id(deep))
