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
    print(i)'''
# Q3 : Print even numbers from 1 - 50 using both while loop and dor loop .

i = 1
while i<=50:
    if i%2 == 0 : 
        print(i)
        i+=1

