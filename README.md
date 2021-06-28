-   [Overview](#overview)
-   [Expirement Summary](#expirement-summary)
-   [File Structure and Naming Conventions](#file-structure-and-naming-conventions)
-   [Sensors](#sensors)
-   [Data Types](#data-types)
    -  [Video and Imagery](#video-and-imagery)
    -  [Radar and Passive Radio Frequency](#radar-and-passive-radio-frequency)
    -  [Acoustic](#acoustic)
    -  [Seismic](#seismic)
- [Additional Information](#additional-information)

### Overview
The ESCAPE(Experiments, Scenarios, Concept of Operations, and Prototype Engineering) dataset, collected at the Information Directorate's Stockbridge Site in 2018 is a multimodal dataset aimed to aide data fusion reserach. The collection instruments include two SUAS (small unmanned flight system), four different observation towers, and two ground sensors. The researchers gathered  data on four types of moving targets, a van, gators(gas/diesel), a pickup truck, and a rack truck. The data includes information on P-RF(passive radiofrequency), radar, EO(electro-optical), IR (infrared), seismic and acoustic sensing. Having multimodal data provides many advantages, but the long term goal for this project is to create "signatures" for each of the targets. These "signatures" are formed by fusing the heterogeneous data types together to understand the unique behavior, "signature", for each target. To approach this pragmatically the researchers utilized a metal building in the center of the Stockbridge site, dubbed the "Butler Building". During each test run two or more targets would circle the site and then enter the Butler Building. Upon exiting the building the targets would leave at varying times, and some may not depart at all. If the researchers can successfully develop suitable signatures for each target based on the multi modal data, this allows the targets to be accurately identified as they exit.

##### StockBridge Site
![](/images/siteLayout.jpg)


##### Vehicles 
| Disel Gator                | Disel John Deer              | Gas John Deer               |
|----------------------------|------------------------------|-----------------------------|
| ![](/images/GatorDisel.png)|![](/images/JohnDeerDisel.jpg)| ![](/images/JohnDeerGas.jpg)|

| State Rack Truck           | Van                          | Pickup                      |
|----------------------------|------------------------------|-----------------------------|
| ![](/images/rackTruck.jpg) |![](/images/van.jpg)          | ![](/images/pickup.jpg)     |

### Expirement Summary 
Its important to note that in this experiment, there are two mobile forms of data collection. Data received from the ESCAPE payload attached to the SUAS, and the data received from the emitters placed on the target. For each trial, the targets and the SUAS have a set path(a scenario), then multiple runs with varying constants are collected for each scenario. Please refer to the test card to review the vehicle [general/ESCAPE 2018 Vehicle Test Cards 20190416.pptx](general/ESCAPE%202018%20Vehicle%20Test%20Cards%2020190416.pptx) and the SUAS [general/ESCAPE 2018 SUAS Test Cards 20191127.pptx](general/ESCAPE%202018%20SUAS%20Test%20Cards%2020191127.pptx) scenario specifications. For the SUAS scenarios, the ESCAPE payload remains stationary on the ground while the drones act as the targets as they circle in the pattern described in the scenario layout. For the vehicle scenarios, the vehicles are the targets, and the drones carry the payload observing the information transmitted from the emitters places on the vehicles. There are five different types of vehicles utilized, John Deer - gas, John Deer - diesel, Gator, Van, Pickup Truck, and a State rack truck. More than one vehicle is part of the run in most vehicle scenarios, so be sure to refer to the vehicle test cards for the specific paths. When reading the test cards, note the information included on the runs. For the SUAS runs, there should be information detailing the angle and direction of the drones. The vehicle run information should include which vehicles are being observed, how each drone is moving, and the type of emitter attached to the vehicle. The columns dedicated to each run is highlighted based on the date of data collection, and those not highlighted are runs that were planned but never executed.

|               | Example Scenario               | Example Run Card                 |
| ------------- | -------------------------------| ---------------------------------|
| SUAS          |![](/images/SuasScen4%20(2).png)|![](/images/SuasScen4Run.png)     |
| Vehicle       |![](/images/Scen1Veh.jpg)       |![](/images/Scen1VehRun%20(2).png)|


### File Structure and Naming Conventions
If interested in the data set, follow the instructions found in the data access read me [README_Data_Access.md](README_Data_Access.md). Each file follows a specific naming convention found, described in the sensor, and naming convention powerpoint [general/ESCAPE Sensor Layout Filename Conv 20201220.pptx](general/ESCAPE%20Sensor%20Layout%20Filename%20Conv%2020201220.pptx). Each file is formatted according to d##s##r##yyyymmdd.*** standard, where the number following "d," "s," and "r" is the numerical value associated with the device(sensor), scenario. and run respectively. The only exception is the .tiff files. These files don't follow a unique format, and the location on the file tree can determine their device, sensor, and run.  



### Sensors 
This experiment used various sensors of different capabilities to form the ESCAPE dataset. The sensors were either mounted on a tower, included in the ESCAPE payload, or were a gound sensor. The table below shows what sensors are stored at each location.  
|   Location     | Sensors           | 
| -------------  | ------------------| 
| ESCAPE payload | EO, IR, P-RF      |
| Tower 1        | EO, IR, P-RF      |
| Tower 2        | Radar             |      
| Tower 3        | P-RF              |
| Tower 4        | EO                |
| Groud          | acoustic & sesmic |

Each sensor has a number associated with them, and its placement on the field varies with the different scenarios. A visual of sensor locations are provided in the sensor and naming convention powerpoint [general/ESCAPE Sensor Layout Filename Conv 20201220.pptx](general/ESCAPE%20Sensor%20Layout%20Filename%20Conv%2020201220.pptx).

![](/images/sampleSensor.png)

Some of the sensors have several components, resulting in collecting multiple files for just one run. For example, there are 16 wav files associated with the acoustic sensor because there are 16 microphones. Likewise, there were multiple cameras per EO sensor producing a variety of imagery and video data. The sensors collected seven main data types including, .tiff, .avi, .jpg, .bin, .yuv, .csv, .wav files.

|  Infromation | Datatype | 
| -------------| ---------| 
| EO           | TIFF     |
| IR           | JPG/AVI  |
| PRF          | binary   |      
| Radar        | binary   |
| EO           | YUV      |
| Seismic      | CSV      |
| Acoustic     | WAV      | 

### Data Types 
#### Video and Imagery
Extensive EO data was collected in the making of this dataset. There are three main file types associated with the EO data, .yuv. .avi, .tiff files. Both yuv and avi are video files, however avi are standard red, green, blue videos, and yuv are black and white. Unlike avi, [yuv](https://en.wikipedia.org/wiki/YUV) files contain chrominance and luminance infromation on each pixel instead a rgb value. Also included in the dataset are .tiff files which are simple, red green blue images. To make data analysis easier on the video files use the [code/yuv2png.py](code/yuv2png.py) and the [code/avi2png.py](code/avi2png.py) scripts which extract each frame, convert it to an rgb image if necessary, then save the frames as a png locally. In order to to be able to save an retrieve the frames, create folders named yuv2png, avi2png in your IDE. Using the [code/image.py](code/image.py) any two images, whether it be a tiff, png or any other image file can be imported, read, plotted, and determined if the two images are identical. 

#### Radar and Passive Radio Frequency
Radar and passive radio frequencey(P-RF) was collected using binary files. [Radar](https://en.wikipedia.org/wiki/Radar), detects radiowaves from the transmitters and [P-RF](https://en.wikipedia.org/wiki/Passive_radar), is a measurement of the time gap between the transmitter signal and the signal from object reflection. Each byte in the bin files have a numerical value associtaed with it which can be read and plotted using the [code/bin.py](code/bin.py). Note the binary files are quite large, <2GB, and will result in a memory error if attempted to read each individual byte. For computational efficancy purposes, the program is set to read each 1000000th byte on line 20, but certianly can be adjusted to a smaller value to porduce more accurate results. 

#### Acoustic
The [aucostic](https://en.wikipedia.org/wiki/Acoustical_measurements_and_instrumentation) data was collected as wav files using sixteen different microphones. The frequency of thse wav files can be easily analyzed using the wave python library. [code/wav.py](code/wave.py) program will read a wav file and plot the amplitude over time. 

#### Seismic
The [seismic](https://en.wikipedia.org/wiki/Reflection_seismology) data, a measurement of reflected seismic waves from earth's sublayer, is stored using a comma seperate file(csv). Each csv file contains two rows one with the numerical seismic values on one row and the other row dedicated to time. Note each time entry has a unique naming standard, for example on entry might be 2018-10-19T16:00:00.097999Z, in the [code/csv.py](code/csv.py) the hh:mm:ss.ssssss time is isolated, and used for plotting the seismic data.

### Additional Information
The researchers who conducted ESCAPE data collecction publised their work in the article [ESCAPE Data Collection for Multi-Modal Data Fusion
Research](https://www.researchgate.net/profile/Erik-Blasch/publication/333922294_ESCAPE_Data_Collection_for_Multi-Modal_Data_Fusion_Research/links/5f1b0634299bf1720d6050b6/ESCAPE-Data-Collection-for-Multi-Modal-Data-Fusion-Research.pdf). This extensivley covers the methodolgy, science, and future goals for the ESCAPE data. For a shorter and conciese overview of the porject refer to the [ESCAPE_overview 20190416.pptx](general/ESCAPE_overview%2020190416.pptx) powerpoint. 



