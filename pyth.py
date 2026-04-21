'''num = int(input("Enter a number to find its factorial: "))
i = 1

factorial = 1 

while i <=num:
    factorial *= i
    i+=1


    print(f"the factorial of {num} is {factorial}")


# Q1 : Print 1 - 10 using while loop and for loop .
i = 1
while i <= 10 :
    print(i)
    i+=1 

for i in range(1,11,1):
    print(i)

# Q2 : Print 10 - 1 using  both while loop and for loop . 
i = 10 
while i >= 1 :
    print(i)
    i-=1
for i in range(10,0,-1) :
    print(i)
# Q3 : Print even numbers from 1 - 50 using both while loop and dor loop .

i = 1
while i<=50:
    if i%2 == 0 : 
        print(i)
        i+=1
for i in range(1,51):
    if i%2 == 0 :
        print(i)

# Q4 : Print odd numbers from 1 - 50 using both while loop and for loop .

i = 1 

while i <= 50 :
    if i%2 != 0 :
        print(i)
    i+=1
# Q5 : Find the sum of all n numbers from 1 to n using both while loop and for loop .

n = int(input("enter a number n to find the sumof all numbers from 1 - n :"))
sum = 0 
i = 1 
while i <= n :
    sum +=i
    i+=1
    print(f"the sum of all numbers from 1 - {n} is {sum}")

n = int(input("enter a number n to find the sumof all numbers from 1 - n :"))
sum = 0 
for i in range(1,n+1):
    sum +=i 
    print(f"the sum of {n} is {sum}")
# Q6 : Print the multiplication table of a given number n using both while loop and for loop .

n = int(input("enter a number n to find its multiplication table :"))
i = 1 
while i <= 10 :
    print(f"{n} * {i} = {n*i}")
    i+=1

n = int(input("enetr the number n to find its multipplication table :"))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")
# Q7 : Count how many numbers between 1 - 100 are divisible by 3 , use loop to solve . 

i = 1 
count = 0 
while i <= 100 :
    if i%3 == 0 :
        count +=1 
    i+=1
print(f"the count of numbers between 1 - 100 that are divisible by 3 is {count}")

# Q8 : Find the factorial of a number n using loops . 
n = int(input("enter a number n to find its factorial :"))
factorial = 1 
i = 1 
while i <=n :
    factorial *=i
    print(f"the factorial of {n} is {factorial}")
    i+=1 

n = int(input("enter a number n to find its factorial :"))   

factorial = 1 

for i in range(1,n+1):
    factorial *=i
    print(f"the factorial of {n} ia {factorial}")

# Q9 : Reverse a number using loops . 

n = int(input("enter a n number n to reverse it :"))
i = 1 
reverse = 0 
while n > 0 : 
    digit = n%10
    reverse = reverse * 10 + digit 
    n = n//10 
    print(f"the reverse {n} is {reverse}")
    i+=1 '''
n = int(input("enter a number n to reverse it well : "))

reverse = 0 
for i in range(len(str(n))):
    digit = n%10 
    reverse = reverse * 10 + digit 
    n = n//10
    print(f"the reverse of {n} is {reverse}")











    






