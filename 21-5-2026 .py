# Python Basic program
'''
# 1. Print your name using in built-in funstion input()

name = input("Enter your name : ")
print("My name is" , name)

# simple calculator

a = int(input("Enter first value :"))
b = int(input("Enter second value:"))

print("addition: " , a + b)
print("substraction: ", a - b)
print("Multiplication : " , a * b)
print("Division: " , a / b)              

# Silly Sandwich Maker

bread = input("choose your bread(white / brown) : ")
filling = input("choose your filling(cheese / jelly / banana) :")

print("Here's your silly sandwich.")
print("[" + bread + "bread +" +
filling + " + rainbow glittre]")
'''             
# Rock , paper, scissors 

import random

choice = ["rock" , "paper" ,"scissors"]
computer = random.choice(choices)

player = input("choos rock , paper or scissors : ")

print("omputer choice : " , computer)

if player == computer:
      print("It's a tie.")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("you are win")
else:
    print("computer win")
    
     
