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
    i+=1 
n = int(input("enter a number n to reverse it well : "))

reverse = 0 
for i in range(len(str(n))):
    digit = n%10 
    reverse = reverse * 10 + digit 
    n = n//10
    print(f"the reverse of {n} is {reverse}")


#Q10 : Print the Pallindrome number . 

n = int(input("Enter a number to check if it is a palindrome: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print(f"The number {original} is a palindrome")
else:
    print(f"The number {original} is not a palindrome")

# Q11 : Print Sum of digits of a number n using loops . 

n = int(input("enter a number n to find the sum of its digits : "))
sum = 0 
while n > 0 : 
    digit = n % 10 
    sum += digit 
    n = n // 10 
    print(f"the sum of the digits is {sum}")


n = int(input("enter a number n to find the sum of its digits : "))
sum = 0 
for i in range(len(str(n))):
    digit = n % 10 
    sum += digit 
    n = n // 10 
    print(f"the sum of the digits is {sum}")

# Q12 : Count the number of digits in a number.

n = int(input("enter the number "))

count = 0 
while n > 0 :
    n = n // 10 
    count +=1 
    print(f'the count of digits in the number is {count}')'''

# Q13 : Print the Fibonacci series up to n terms using loops .

n = int(input("enter the number of terms n to print the Fibonacci series :"))
a = 0 
b = 1 

for i in range(n):
    print(a, end=" ")
    c = a + b 
    a = b 
    b = c 

# Q14 : Print the Pattern of Stars using loops .
n = int(input("enter the number of rows n to print the pattern of stars :"))
while n > 0 : 
    print("*" * n)
    n -=1

n = int(input("enter the number of rows n to print the pattern of stars :"))

for i in range(n , 0 , -1):
    print("*"*i)

# Q15 : Print the Pattern of stars in aescending order using loops . 

n = int(input("enter the number of rows n to print the pattern of stars in aescending order :"))
i = 1 
while i <= n : 
    print("*" * i , end = "\n")
    i+=1

# Q16 : Print the Patttern of numbers in aescending order using loops . 

n = int(input("Enter number of rows: "))

i = 1
while i <= n:
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    i += 1



 

    
















    






