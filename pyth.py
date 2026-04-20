num = int(input("Enter the number for which you want to check factorial :"))

i = 1

factorial = 1 

while i <=num:
    factorial *= i
    i+=1


    print(f"the factorial of {num} is {factorial}")
