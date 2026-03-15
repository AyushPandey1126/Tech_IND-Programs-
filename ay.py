"""print("console calculator")
num1 = float(input("Enter first number: "))
ope = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("enter second number:"))

if ope == "+":
	print("result:", num1 + num2)
elif ope == "-":
	print("result:", num1 - num2)
elif ope == "*":
	print("result:", num1 * num2)
elif ope == "/":
	print("result:", num1 / num2)
elif ope == "%":
	print("result:", num1 % num2)
else:
	print("invalid operator") 
for i in range(5,51,5):
	print(i)
 
j = "TECHIND RISHI"
print(len(j))

for i in range(len(j)):
	print(j[i])

n = int(input("eneter a number:"))
for i in range(n,n*10+1,n):
	print(i)
n = int(input("enter a number to find its factorial:"))
factorial = 1

for i in range(1, n+1):
    factorial*=i

print(f"the factorial is: {factorial}")

n = int(input("Enter a number: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f"The sum of even numbers is {even}")
print(f"The sum of odd numbers is {odd}")
n = int(input("enter a number:"))
sum = 0
for i in range(1,n):
	if n % i == 0:
		sum += i 

if sum == n:
	print(f"{n} is a perfect number")
else:
	print(f"{n} is not a perfect number")
n = int(input("Enter a number to check prime or not: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

a = " RISHI"

b = " "
for i in range(len(a)-1, -1, -1):
	b = b + a[i]
	print(b)
a = "naman"

b = ""
for i in range(len(a)-1, -1, -1):
	b = b + a[i]
	
if b == a:
	print(f"{a} is a palindrome")
else :
	print (f"{a} is not a palindrome")
a = "adjbd*&^%$#@!12345"
dig = 0 
char = 0  
spchr = 0
for i in a :
	if i.isdigit():
		dig = dig + 1 
	elif i.isalpha():
		char = char + 1 
	else :
		spchr = spchr + 1 

print(f"digits: {dig} \ncharacters: {char} \nspecial characters: {spchr}")

a = int(input("enter a number:"))
rev = 0 
while a > 0 :
	rev  = rev * 10 + a % 10
	a = a // 10 
print(f"reverse of the number is: {rev}")

a = int(input("enter a number:"))
copy = a 
rev = 0 
while a > 0 :
	rev  = rev * 10 + a % 10
	a = a // 10 

	if rev == copy :
		print(f"{copy} is a palindrome number ")
	else :
		print(f"{copy} is not a palindrome number ")
import random 

num = random.randint(1,10)
tries = 0
while True :
	guess = int(input("guess a number between 1 to 10:"))
	if num == guess :
		tries +=1
		print(f"congratulations! you guessed it right in {tries} tries.")
		break
	elif guess < num :
		print("too low! try again.")
		tries +=1
	elif guess > num :
		print("too high! try again.")
		tries +=1
	else :
		tries +=1
		print("try again , you are wrong .")
	ef palindrome(s):
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev = rev + s[i]

    if rev == s:
        print("palindrome")
    else:
        print("not a palindrome")


palindrome("naman")
def sum(a, b):
    print(f"The sum is: {a + b}")

sum(4, 7)

a = [1, 2, 3, 4, 5]
a.append(6)

print(a)

print(dir(list))
 
l = [1,3,4,5]
l.insert(1,2)

print(l)
a = [1,-2,3,-4,5,-6,7,-8,9]
print("positive elements are :")
for i in a :
	if i >= 0 :
		print(i)
print("negative elements are :")	
for i in a : 
	if i < 0 :
		print(i)

a = [12, 34, 56, 78, 90]	
sum = 0 
for i in a : 
	sum = sum + i 

print(sum/len(a))

a = [236, 567, 890, 123, 456]

largest = a[0]
index = 0

for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i

print(largest)
print(index)
a = [236, 567, 890, 123, 456,889]

largest = a[0]
second_largest = a[0]

for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print(f"the largest no is : {largest}")
print(f"the second largest no is : {second_largest}")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted")	

a = (1, 2, 3, 4, 5)

print(type(a))
a = (1, 2, 3, 4, 5)
index = a.index(3)
print(index)
a = (1, 2, 3,3, 4, 5)
count = a.count(3)
print(count)
a = {1, 2, 3, 4, 5}
a.add(6)
print(a)

a = {1, 2, 3, 4, 5, 6}
a.remove(3)
print(a)
a = {1, 2, 3, 4, 5, 6}
a.pop()
print(a)
a = {1, 2, 3, 4, 5}
a.clear()
print(a)
a = {1, 2, 3, 4, 5}
b = a.discard(6)
print(a)
#Union of two sets (| (union operator))
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a|b)

#Intersection of two sets (& (intersection operator))
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(b & a)

#Difference of two sets (- (difference operator))
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a - b)
print(b - a)

#Symmetric difference of two sets (^ (symmetric difference operator))
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a ^ b)

#CRUD operations on dictionary (create, read, update, delete)

a = { 10:100, 20:200, 30:300}
a.update({40:400}) #create
print(a)
print(a[20]) #read
a.update({30:350}) #update
print(a)
a.pop(10) #delete
print(a)

# Deep copy and shallow copy 
a = [1, 2, 3, 4, 5]
b = a #when .copy is'nt used then it is deep copy otherwise shallow copy
b[0] = 10
print(a)
print(b)

d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 50:500, 60:600}
print(d1|d2) 

# Merge two dictionaries
d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 50:500, 60:600}
for i in d2 :
	d1[i] = d2[i]
print(d1)

# Sum of all values in a dictionary
d1 = {10:100, 20:200, 30:300}

sum = 0 
for i in d1 :
	sum  = sum + d1[i]
	print(f"sum of the values in the dict. is : {sum}")

a = [ 1, 2, 2, 3, 4, 4, 5, 5, 5 ]	
print(a.count(5))

# Count frequency of each element in a list

a = [ 1, 2, 2, 3, 4, 4, 5, 5, 5 ]

dict = {}


for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

# Merge two dictionaries by adding values for common keys

d1 = {10:100, 20:200, 30:300, 40:400}
d2 = {40:100, 50:500, 60:600, 70:700}

for i in d2 :
	if i in d1.keys():
		d1[i]+=d2[i]
	else :
		d1[i]=d2[i]
		print(d1)

# Exception handling example
num = int(input("Enter a number: "))

try:
	print(10/num)
except Exception as err :
	print("You cannot divide by zero!")

print("division operation completed.")	

# File handling example
a = open("ay.py")
print(a.read())

p = open("ap.cpp")
print(p.read())

#write and append mode example
a = open("ayush.txt", "w")
a = open("ayush.txt", "a")
a.write("is learning python.")

#object oriented programming example 1 
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print(f"Name: {self.name}, Age: {self.age}")
p1 = Person("Ayush", 20)
p1.display()
p2 = Person("reece", 22)
p2.display()

class Animal: #Parent class
	def __init__(self, name): #constructor
		self.name = name #instance variable

	def speak(self):
		pass

class Pet(Animal): # Child class implementation
	def speak(self):
		print(f"{self.name} says hello!")
p1 = Pet("Buddy")
p1.speak()"""

a = [12, 34, 56, 78, 90]	
sum = 0 
for i in a : 
	sum = sum + i 

print(sum/len(a))













	
	







	


	
