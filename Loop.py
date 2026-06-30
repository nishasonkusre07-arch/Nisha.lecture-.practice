#Loop in python
'''
1.while loop
2.for loop
'''

#while loop

#a while loop runs as long as the condition is true.
'''

while condition:
    #code block
'''

# print number 1 to 5
'''
i = 1

while i<= 5:
    print(i)
    i += 1
    
i = 5

while i>= 1:
    print(i)
    i=1
 '''   
# for loop

# print number 1 to 5
'''
print("=====for loop =====")

for i in range(1,7):
   print(i)


print("=====string loop ======")

name = "python"

for i in name:
    print(i)

print("=====list loop=====")

fruits = ["Apple","orange","banana","Mango"]

for iteam in fruits:
    print(iteam)

print("="*20)
'''
#range()function

#range(start,stop,stap)
'''
for i in range(5):
    print(i)

print("="*30)

for i in range(0,10,2):
    print(i)
    
print("="*20)

for i in range(10,0,-1):
     print(i)
'''
#nestad loops in python

# A Loop inside another loop.
'''
for i in range():
    for j in range():
        #block of code
'''

print("========")
'''
for i in range(1,5):
    for j in range(1,4):
        print(j,end="")
    print()
'''
print("=====break statement")

# stops the loop immediately.
'''
for i in range(1,7):
    if i==4:
        break
    print(i)
'''
print("=====continue statement")

# skips current iterations.
'''
for i in range(1,7):
    if i==5:
        continue
    print(i)
'''
print("=====pass statement======")

#skips current iterations.

for i in range(1,7):
    if i==5:
        pass
    print(i)


















































