lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("length of list:", len(lst))
print("first element:", lst[0])
print("last element:", lst[-1])

lst.append('Papaya')
print("updated list:", lst)

lst.remove('Guava')
print("updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("updated list", lst)

lst.reverse()
print("reversed list:", lst)

print("Multipication on list:", lst*2)
