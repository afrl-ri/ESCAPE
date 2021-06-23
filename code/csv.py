# filepath
fp = "d41_R23AC_S01_R12_20181019.csv"
# imports 
import numpy as np
import matplotlib.pyplot as plt
import csv
# input all of the csv data into an array
data = []
with open(fp, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
# isolate the value and time data from array
values = []
time = []
for i in range(0, len(data[0][:])):
    values.append(int(data[0][i]))
    time.append(data[1][i])
# extract raw time data
timeRaw = []
indexLen = len(time)
for i in range(0, indexLen):
    index = time[i]
    timeRaw.append(index[11:25])
plt.plot(timeRaw, values)
plt.ylabel("Sesmic Value, Sensor %s" %fp[1:3])
plt.xlabel("Time")
