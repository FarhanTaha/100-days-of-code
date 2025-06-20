# Problem 1: Extract even rows from CSV file and write to a new CSV.

import csv

with open('exampleWithHeader.csv', newline='') as inputFile, \
     open('output.csv', 'w', newline='') as outputFile:

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile)

    for index, row in enumerate(reader):
        # Always write the header (index 0), then skip even rows (index 2, 4, 6...)
        if index == 0 or index % 2 != 0:
            writer.writerow(row)



