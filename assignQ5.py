# Write a program that takes a string input from the user and writes it to a 
# text file. 

user_input = input("Please enter a string: ")
filename = "output.txt"

with open(filename, "w") as file:
    file.write(user_input)

print(f"The string has been written to {filename}")

