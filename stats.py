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
        curLine = 0
        for row in reader:
            if curLine == 0:
                pass
            else:
                item = float(row[4])
                data.append(item)
            curLine += 1

        print(f"Read {curLine+1} row of data.")
        return data

def calcStats():
    data = readData()

    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    data_std = round(statistics.stdev(data), 2)
    data_var = round(statistics.variance(data), 2)

    print("Mean: ", data_mean)
    print("Med: ", data_med)
    print("Std Div: ", data_std)
    print("Variance: ", data_var)

calcStats()
