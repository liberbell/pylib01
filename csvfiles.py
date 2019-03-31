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
        hashedder = csv.Sniffer().has_header(csvfile)

def writeSample():
    pass

# readerSample()


# useSniffer()
