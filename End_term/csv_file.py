
import csv

file_path = 'End_term/data.csv'

# Create a CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', '25', 'New York'])
    writer.writerow(['Jane', '30', 'Los Angeles'])
    writer.writerow(['Bob', '35', 'Chicago'])
    writer.writerow(['Alice', '20', 'San Francisco'])

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# other method to open
filePath = "End_term/daata.csv"
f = open(filePath,mode='w',newline='')
writer = csv.writer(f)
writer.writerow(['name','age'])
writer.writerow(['ak',56])
f.close()

f = open(filePath,mode='r')
reader = csv.reader(f)
for row in reader:
    print(row) 
