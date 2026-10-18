print('Hello world')


list1 = [1, 3, 5, 65, 34, 33]
for a in list1:
    print(a * 2)

print(20 * '*')

mapping = list(map(lambda a : a ** 2, list1))
print(mapping)