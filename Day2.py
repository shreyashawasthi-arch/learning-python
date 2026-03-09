print("This is String \nThis is new line")
print("This is string  \t This is tab space")

str1 = "Hello"
str2= "World"
finalstr= str1+str2
print(finalstr)
print (len(finalstr))
print(finalstr[4])

str= "Python is great"
print(str[1:7]) # slicing
print(str[:5]) # slicing from start
print(str[3:]) # slicing till end
print(str[-4:-2]) # slicing using negative index
print(str.endswith("eat")) # check if string ends with "eat"
print(str.replace("is", "was")) # replace "is" with "was"
print(str.find("is")) # find index of "is"
print(str.count("i")) # count occurrences of "i"


#practice problem

# Q1 WAP to input user' First name and print its length

# name=(input("Enter your First name: "))
# print(len(name))

# Q2 WAP to find the occurence of "$" in a string

str= input("Write a string to find the occurence of $: ")
print(str.find("$"))

# Conditional statements

Day= ("monday")

if Day == "monday":
    print("You cannot cut hairs on monday")
elif Day == "tuesday":
    print("You cannot cut hairs on tuesday")
elif Day == "wednesday":
    print("You can cut hairs on wednesday")
elif Day == "thursday":
    print("You cannot cut hairs on thursday")       
elif Day == "friday":
    print("You can cut hairs on friday")
elif Day == "saturday":
    print("You cannot cut hairs on saturday")
else:    print("You can cut hairs on sunday")