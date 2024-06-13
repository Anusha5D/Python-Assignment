#Write a python program that calculates the factorial of a given number
n=int(input("Enter a number:  "))
sum=1
for i in range(1,n+1):
    sum=sum*i

print("The factorial of" ,n, "is" ,sum)