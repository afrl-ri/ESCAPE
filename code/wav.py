# file path for .wav data 
wavZer = 'd31s05r0520181018_0.wav'
# Imports
import numpy as np
import matplotlib.pyplot as plt
import wave as wv
from scipy.io.wavfile import read
# Read in Data using the wave library
datZer = wv.open(wavZer,'r')
# get and print wav info
datZerParam = datZer.getparams()
# initialize list of usefule information 
print("Data Set 1: ", datZerParam, "\n")
# read audio samples
graphZer = read(wavZer)
audio = graphZer[1]
# plot the first 1024 samples
plt.plot(audio[0:datZer.getnframes()])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wave, Sensor %s%s" %(wavZer[1], wavZer[2]))
# display the plot
plt.show()
