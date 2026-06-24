# python Basics
'''
# print your name

print("Hello,my name is nisha!!")

# Add two Numbers

a = 5
b = 10

sum = a+b

print("The sum is;",sum)

# Ask user's name

name = input("what is your name:")
print(name)

# simple calculator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Addition :",a+b)        
print("subtraction :",a-b)        
print("Multiplication :",a*b)        
print("Division :",a/b)
'''
# print() formatting using sep and end
'''
print("Apple" ,"banana" , "cherry" , sep = "|",end = "<--- End of List\n")

# formatting message from user input

name = input("Enter your name:")
age = int(input("Enter your age:"))
hobby = input("Enter your favorite hobby:")

# f-string

print(f"Hello , {name}! At {age},enjoying {hobby}sounds fun!!!")
'''
# Declare variables of diffrent data types and show their types
'''
a = 10
b = 3.14
c = "python"
d = True

print(a,"type:", type(a))
print(b,"type:", type(b))
print(c,"type:", type(c))
print(d,"type:", type(d))
'''
# python program

subject1 = input("Enter 1st subject name:")
marks1 = int(input("Enter your marks:"))

subject2 = input("Enter 2nd subject name:")
marks2 = int(input("Enter your marks:"))

subject3 = input("Enter 3rd subject name:")
marks3 = int(input("Enter your marks:"))

#calculate total and average

total = marks1 + marks2 + marks3
average = total/3

#decide Grade

if average >= 90:
   grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "fail"

print("\n-----------result-----------")
print(f"{subject1}:{marks1}")
print(f"{subject2}:{marks2}")
print(f"{subject3}:{marks3}")
print(f"Total Marks:{total}")
print(f"Average Marks:{average}")
print(f"Grade:{grade}")









          

