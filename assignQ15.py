#  Write a program that reads data from a CSV file and prints it to the 
# console.
import csv


file_name = "data_input.csv"
with open(file_name,"r") as csvfile :
    reader = csv.reader(csvfile)
    data = list(reader)
    for d in data :
        print(d)



