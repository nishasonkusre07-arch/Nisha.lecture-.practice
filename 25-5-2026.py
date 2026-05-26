# print formatting using sep and end
'''
# using sep with end

print("Apple" , "Banana" , "Charry" , sep=" + " , end="<--- End of List\n")

# Fomatted Message for user input

name = input("Enter your name:")
age = input("Enter your age:")
hobby = input("Enter your favorite hobby:")

print(f"Hello , {name}! At{age}, enjoing {hobby} sounds fun1")


# Basic arithmetic operations

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("addition : " ,a + b )
print("subtraction: " , a - b)
print("Multiplication : " , a * b)
print("Divison : " , a / b)
print("floor Division : " , a // b)
print("modulus : " , a % b)
print("Expomtiations :", a ** b)
'''
# Decalre variables of diffrent data typs and show their typs

a = 10
b = 3.14
c = "CareerX"
d = False

print("a = " , a ,"type : " ,type(a))
print("b = " , b ,"type : " ,type(b))
print("c = " , c ,"type : " ,type(c))
print("d = " , d ,"type : " ,type(d))

# type() function and id() function

a = 10
b = 30

print(id(a))
print(id(b))
