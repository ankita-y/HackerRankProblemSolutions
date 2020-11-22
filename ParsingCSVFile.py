import csv
def parse(filename):
    table = []
    with open(filename,"r") as csvfile:
        csvreader = csv.reader(csvfile)
        for i in csvreader:
            table.append(i)
    return table

def print_table(table):
    for row in table:
        # Header column left justified
        print("{:<15}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = parse("hightemp.csv")
print_table(table)
