# Write a python program that removes all punctuation from a given string.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 = input("Enter a string: ")
no_punct = ""
for ch in str1:
    if ch not in punctuations:
        no_punct = no_punct + ch

print(no_punct)