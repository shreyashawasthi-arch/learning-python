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

# str= input("Write a string to find the occurence of $: ")
# print(str.find("$"))

# Conditional statements

# Day= input("Enter the day of the week: ").lower() # convert input to lowercase

# if Day == "monday":
#     print("You cannot cut hairs on monday") #indentation is important in python
# elif Day == "tuesday":
#     print("You cannot cut hairs on tuesday")
# elif Day == "wednesday":
#     print("You can cut hairs on wednesday")
# elif Day == "thursday":
#     print("You cannot cut hairs on thursday")       
# elif Day == "friday":
#     print("You can cut hairs on friday")
# elif Day == "saturday":
#     print("You cannot cut hairs on saturday")
# else:    print("You can cut hairs on sunday")

#nesting of if statements

# age = int(input("Enter your age: "))

# if (age>= 21):
#     if(age>= 37):
#         print("you are not eligible for UPSC")
#     else:
#         print("you are are eligible to apply for UPSC")
# else:    print("you are not eligible to apply for UPSC")

# Practice problem

# Q1 WAP to check if a number entered by the user is odd or even

# number= int(input("Enter a number: "))
# if(number%2==0):
#     print("The number is even")
# else: print("The number is odd")

# Q2 WAP to find the greatest of three numbers entered by the user

# num1= int(input("Enter number 1: "))
# num2= int(input("Enter number 2: "))
# num3= int(input("Enter number 3: "))
# if(num1> num2 and num3):
#     print("Number 1 is the greatest")
# elif(num2> num1 and num3):
#     print("Number 2 is greatest")
# else: print ("Number 3 is the greatest")


# Q3 WAP to check if a number is multiple of 7 or not

number= int(input("Enter a number: "))
if(number%7==0):
    print("The number is a multiple of 7")
else: print("The number is not a multiple of 7")