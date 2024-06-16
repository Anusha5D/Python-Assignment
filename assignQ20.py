# Write a python program that takes a list of numbers and returns their sum.
# Python program to find sum of elements in list
no_ofinputs=int(input("Enter the count of numbers you would take as input:"))
list1=[]
for i in range(no_ofinputs):
    num=int(input("Enter the numbers:  "))
    list1.append(num)
print("The list you entered:",list1)
total=0
for ele in range(0, len(list1)):
	total = total + list1[ele]


print("Sum of all elements in given list: ", total)
