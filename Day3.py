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

#tuples in Python

tup= (1, 2, 3, 4, 5)
print(type(tup))
print(tup[0])
print(tup[1:3])

print(tup.index(3)) # find index of 3
print(tup.count(4)) # count occurrences of 4

# practice problem

# Q1 Wap to ask the user to enter name of their 3 favourite movies and store them in a list

# movies = [input("Enter your favourite movie 1: "), input("Enter your favourite movie 2: "), input("Enter your favourite movie 3: ") ]
# print("Your favourite movies are: ", movies)

# Q2 WAP to check if a list contains a palindrome of elements

list1= [1, 2, 3, 4, 5, 4, 3, 2, 1]

copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")



# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]

grade= ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

grade2 = ["C", "D", "A", "A", "B", "B", "A"]
grade2.sort()
print(grade2)