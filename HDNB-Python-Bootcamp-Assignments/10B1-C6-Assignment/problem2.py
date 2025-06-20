# Problem 2: Extract headers only from CSV files and write to a new folder


import csv
import os

inputFolder = 'removeCsvHeaders'
outputFolder = 'headerOnly'

os.makedirs(outputFolder, exist_ok=True)

for filename in os.listdir(inputFolder):
    if not filename.endswith('.csv'):
        continue

    inputPath = os.path.join(inputFolder, filename)
    outputPath = os.path.join(outputFolder, filename)

    with open(inputPath, newline='') as infile, \
         open(outputPath, 'w', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            writer.writerow(row)  # just write the first line
            break  # exit after header
