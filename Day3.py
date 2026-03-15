# Lists in Python

marks=[85, 92, 78, 96, 88]
print(marks)
print (marks[0]) # access first element
print(marks[1:4]) # slicing
print(marks[1:]) # slicing from index 1 to end
print(marks[-3:-1]) # slicing using negative index

# List methods
list=[1, 2, 7, 5, 9, 2, 6]
# list.append(0) # add 0 to the end of the list
# print(list)
# list.sort() # sort the list in ascending order
# print(list)
# list.sort(reverse=True) # sort the list in descending order
# print(list)
list.reverse() # reverse the order of the list
print(list)
list.insert(3, 4) # insert 4 at index 3
print(list)
list.remove(2) # remove the first occurrence of 2
print(list)
list.pop(3) # remove the element at index 3
print(list)