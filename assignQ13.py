# Write a program that asks the user for their birth year and calculates their 
# age. 
from datetime import date
yearofbirth=int(input("Enter your birth year: "))
current_year= date.today().strftime("%Y")
print(type(current_year))
print("Your age is :  " ,int(current_year)-yearofbirth)