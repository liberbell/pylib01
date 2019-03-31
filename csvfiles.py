import csv

print(csv.list_dialects())

def readerSample():
    with open("StockQuotes.csv") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)

def useSniffer():
    with open("StockQuotes.csv") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        hashedder = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        print("Headers found: " + str(hashedder))
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)

def writeSample():
    with open("SampleData.csv", mode="w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Department", "Location"])
        csvwriter.writerow(["Jhon Doe", "Accounting", "San Francisco"])
        csvwriter.writerow(["Jhan Dae", "Engineering", "Seattle"])
        csvwriter.writerow(["Jim Due", "Human Resources", "New York"])

# readerSample()
# useSniffer()
writeSample
