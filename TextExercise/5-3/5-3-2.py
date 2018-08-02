#mapにタプルを使用
for num in map(abs, (-1, 2.2, 3.14)):
    print(num)

print()

#mapにrangeを使用
for num in map(abs, range(-5, 0)):
    print(num)

print()

#mapに不揃いなlistを使用
L1 = [1, 2, 3, 4]
L2 = [100, 99, 98]
for num in map(min, L1, L2):
    print(num)

print()

for num in map(max, L1, L2):
    print(num)

#ラムダ式
L = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4, 5], [3, 2, 1, 0]):
    L.append(i)
print(L)