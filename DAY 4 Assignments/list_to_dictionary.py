n = input("Enter element with space between: ")
list1 = n.split()
k = input("Enter element with space between: ")
list2 = k.split()
#list1 = [1, 2, 3, 4, 5]
#list2 = ['a', 'b', 'c', 'd','e']

zipped_list = zip(list1, list2)
dictionary = dict(zipped_list)
print(dictionary)

