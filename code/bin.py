# filepath
fp = "d12s05r0520181018_1539892560.bin"
# imports 
import numpy as np
import matplotlib.pyplot as plt
# Open binary file for reading
f = open(fp, 'rb')
# Get a string from binary file
d = f.read()
# intalize index
i = 0
# create array for indicies 
ilist = []
# create array for binary data
binData = []
# check every 1000000th index for binary data, save y index and data into respective arrays
while i < len(d):
    binData.append(d[i])
    ilist.append(i)
    i = i + 1000000
# declare x and y varibles
x = ilist
y = binData 

# plot the data indicies(x axis) and P-RF(y axis)
plt.xlabel("Byte Index")

if int(fp[1:3]) == 21:
        plt.ylabel("Radar")
else:
    plt.ylabel("Passive Radio Frequencey, Sensor %s%s" %(fp[1], fp[2]))
plt.plot(x, y)
plt.show()
# close the file
f.close()
