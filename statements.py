# control flow in python

# statements in python
'''
1.if statement
2.if...else statement
3.if...elif...else statement
4.match statement
5.continue statements
6.break statement
'''
# The is statement ececutes a block o code only if the specified condition is True.if the condition is false , the code inside the if bloc

'''
if condition:
     #code
'''

age = 20

if age >= 18:
    print("you are eligible to vote.")
        
# The if....else statement is used when there are two possible outcomes:
# if the condition is True, the if block executes.
# if the condition is False , the else block executes.
'''

if condition:
    #code(True)
else:
    #code(false)
'''

number = -5

if number >= 0:
    print("positive Number")
else:
    print("Negative Number")

# if....elif....else statement

# if...elif..else statement is used when multiple condition need to be checked.
'''
if condition1:
     #code
elif condition2:
    #code
elif condition3:
    #code
else :
    #code
'''

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("fail")

# match-case statement

num1 = 10
num2 = 5

operator = "+"

match operator:

  case "+":

     print("Addition:",num1+num2)

  case "-":

     print("Substraction:",num1-num2)

  case "/":

     print("Division:",num1/num2)

  case "*":

      print("Multiplication:",num1*num2)

  case _:

      print("Invalid operator!!")

# Multiple values in one case use

char = "a"

match char :

    case "a"|"e"|"i"|"o"|"u" :
        print("vowel")
        
    case _:
         
         print("consonents")







    
