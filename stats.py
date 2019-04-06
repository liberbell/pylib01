import statistics
import csv
import array

sample_data1 = [1, 3, 5, 7]
sample_data2 = [2, 3, 5, 4, 3, 5, 3, 2, 5, 6, 4, 3]

# print(statistics.mean(sample_data1))

# print(statistics.median(sample_data1))
# print(statistics.median_low(sample_data1))
# print(statistics.median_high(sample_data1))

print(statistics.mode(sample_data2))


def readData():
    with open("StockQuotes.csv") as dataFile:
        data = array.array('f', [])

        reader = csv.reader(dataFile)
