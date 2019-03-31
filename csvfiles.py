import csv

def readerSample():
    with open("StockQuotes.csv") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)

def useSniffer():
    pass

def writeSample():
    pass

readerSample()
