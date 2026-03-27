print("Hello World!","this is my restart to python learning")

name = "John"
price = 26.0
expensive = True
print("My name is", name)
print("the price is", price)

print(type(name))
print(type(price))
print(expensive)
print(type(expensive))

# this is comment
'''this is multilene
comment'''

# arithmetic operators
a = 10
b = 5
sum = a+b
difference = a-b
product = a*b
quotient = a/b
print(sum)
print(quotient)
print(a**b) # exponentiation
print(a%b) # modulus : it gives the remainder when a is divided by b
# comparison operators

a=50
b=20
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a<=b) #False

# assignment operators
num = 10
# num= num + 5
num += 10 
num *=5
print(num) #100

# logical operators
a=50
b=10
print(not(a>b)) #False

val1= True
val2= False #False F should be in capital letter
print ("and operator: ", val1 and val2) #False
print ("or operator: ", val1 or val2) #True

# type conversion

a= int("10")
b= (4.5)
print(a+b) #14.5


# input function
# name= input("Enter your name:")
# age = int(input("enter your age= "))
# married = input( "are you married? (yes/no): " )
# print("welcome", name)
# print('you are', age, 'years old')
# if married == "yes":
#     print("you are married")
# else:
#     print("you are not married")


# practice problem

# Q1 Write a program to input two numbers and print their sum

# num1 = int(input("enter number 1 = "))
# num2 = int(input("enter number 2 = "))
# print ("The sum of two numbers is :", num1+num2)

# Q2 Write a program to input side of a square and print its area

# a= int(input("enter length of the side of the square: "))
# print("the area of the square is:", a*a)

# Q3 write a program to input two floating point number and print their average

# a= float(input("enter the number: "))
# b= float(input("enter the number: "))
# print("the average of two numbers is: ", (a+b)/2)

# Q4 WAP to input 2 int number a and b print true if a is greater than or equal to b. If not print false

a=int(input("enter the number 1 = "))
b= int(input("enter the number2 = "))
print('the expression is ',a>=b)

