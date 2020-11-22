import csv

def read_csv_file(file_name):
    csv_table = []
    with open(file_name, "r",newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for i in csvreader:
            csv_table.append(i)
    return csv_table

def write_csv_file(csv_table, file_name, quoting_value):
    with open(file_name,"w",newline='') as csvwrite:
        csvwrite = csv.writer(csvwrite,delimiter=",", quoting=quoting_value)
        for row in csv_table:
            csvwrite.writerow(row)


filename = "cancer_riskdata.csv"
csv_table = read_csv_file("cancer_risk05_v4_county.csv")
write_csv_file(csv_table,filename,csv.QUOTE_MINIMAL)