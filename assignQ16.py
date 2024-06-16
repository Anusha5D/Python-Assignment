# Write a program in python that counts the frequency of each character in 
# a string. 
ASCII_SIZE = 256
char_count = [0] * ASCII_SIZE
input_string = input("Enter a string: ")

for char in input_string:
    char_count[ord(char)] += 1

print("Character count:")
for i in range(ASCII_SIZE):
    if char_count[i] > 0:
        print(f"{chr(i)}: {char_count[i]}")
