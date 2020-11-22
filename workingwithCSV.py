import csv
#Writing data on CSV file
#Row Header name in CSV file.
fields = ['Name','EmpNo','Designition']


rows = [['Ankita','135632','B1'],
        ['Dipali','135696','A5'],
        ['Robin','102563','C1'],
        ['Ram','136945','C2']]

#filename where data get stored. It cwill get create inside directory
filename = "employee.csv"


with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)