__author__ = "byteme8bit"
import csv

with open('testDB5.csv') as file:
    reader = csv.reader(file, dialect='excel', delimiter=',')
    line_count = 0
    for row in file:
        print(row)
        line_count += 1
        # if line_count == 0:
        #     print(f'Column names are {", ".join(row)}')
        #     line_count += 1

        # else:
        # print(f'\t{row[0]} was born on {row[1]}. Entry created @ {row[2]} with UID: {row[3]}.')
    print(f'Processed {line_count} lines.')