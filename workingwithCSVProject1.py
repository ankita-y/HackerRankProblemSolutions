import csv

def read_csv_fieldnames(filename,separator,quote):
    read_file = []
    with open(filename,"r",newline='') as csvfile:
        #csvreader = csv.reader(csvfile,delimiter=separator, quoting=quote)
        csvreader = csv.DictReader(csvfile,delimiter=separator, quoting=quote)
        print(csvreader)
        for i in csvreader:
            read_file.append(i)
    print(read_file)

#def read_csv_as_list_dict(filename):
read_csv_fieldnames("employee.csv",",",csv.QUOTE_MINIMAL)