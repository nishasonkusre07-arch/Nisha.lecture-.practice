# sets,Dictionary,type conversion, list of Dictionary

print("=" * 40)
print("1. set oprations")
print("=" * 40)

numbers = {1,2,3,4,5}

print(type(numbers))

numbers.add(6)

numbers.remove(3)

print(numbers)

print("In 2 present?", 2 in numbers)

print(numbers)

print("=" * 40)
print("2. Union , Intersection and Difference")
print("=" * 40)

set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(set_a)
print(set_b)

print(set_a|set_b)
print(set_a&set_b)
print(set_a - set_b)
print(set_b - set_a)

print("=" * 40)
print("3. Dictionary Operations")
print("=" * 40)

student = {
    "name":"nisha",
    "age":20,
    "grade":"A"
    }
for key in student.keys():
    print(f"{key}:{student[key]}")

for values in student.values():
    print(values)

print(student["name"])

student["city"] = "Delhi"

student["age"] = 21

print(student)

del student["grade"]

print(student)

print("=" * 40)
print("4. Dictionary from Lists")
print("=" * 40)

keys = ['id','name','email']
values = [101,'rajan','example@gmail.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

print(user)

print("=" * 40)
print("5. Type Conversion")
print("=" * 40)

num = '123'

print(type(num))

nums = int(num)

print(type(nums))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)

pairs = [(1 , "A") , (2 , "B")]

print(dict(pairs))































