### Overview

the ESCAPE(Experiments, Scenarios, Concept of Operations, and Prototype Engineering) dataset, collected at the Information Directorate's Stockbridge Site. 
The collection instruments include two SUAS (small unmanned flight system), four different observation towers, and two ground sensors. The researchers gathered 
data on four types of moving targets, a van, two gators(gas/diesel), a pickup truck, and a rack truck. The data includes information on P-RF(passive radiofrequency), 
radar, EO(electro-optical), IR (infrared), seismic and acoustic sensing. Having multimodal data provides many advantages, but the long term goal for this project is to 
create "signatures" for each of the targets. These "signatures" are formed by fusing the heterogeneous data types together to understand the unique behavior, "signature", 
for each target. To approach this pragmatically the researchers utilized a metal building in the center of the Stockbridge site, dubbed the "Butler Building". During each 
test run two or more targets would circle the site and then enter the Butler Building. Upon exiting the building the targets would leave at varying times, and some may not 
depart at all. If the researchers can successfully develop suitable signatures for each target based on the multi modal data, this allows the targets to be accurately 
identified as they exit.

![](/images/stockbrigesite.png)

### Expirement Summary 

Its important to note that in this experiment, there are two mobile forms of data collection. Data received from the ESCAPE payload attached the SUAS, and the data received from the emitters placed on the target. For each trial, the targets and the SUAS have a set path(scenario), then multiple runs with varying constants are collected for each scenario. Please refer to the test card to review the vehicle ![](general/ESCAPE%202018%20Vehicle%20Test%20Cards%2020190416.pptx) and SUAS ![](general/ESCAPE%202018%20SUAS%20Test%20Cards%2020191127.pptx) scenarios. For the SUAS scenarios the ESCAPE payload remains stationary on the ground while the drones act as the targets as they circle in the pattern specified in the scenario layout. For the vehicle scenarios, the vehicles are the targets and the drones carry the payload observing the infromation tramitted from the emitters places on the vehicles. There are five different types of vehicles utilized, John Deer - gas, John Deer - disel, Gator, Van, Pickup Truck, and a State rack truck. In most of the vehicle scenarios more than one vehicle is part of the run so be sure to refer to the vehicle test cards for the specific paths. When reading the test cards note the informations included on the runs, for the SUAS runs there whould be information detaliing the angle and directions of the drones. The vehicle run informations should include which vehicle are being observed, how each drone isn moveing and the type of emitter attached to the vehicle. The coloumns dedicated to each run is highlited based on the date of data collection, and those not highlighted were runs that were planned but never executed. 

|               | Example Scenario               | Example Run Card                 |
| ------------- | -------------------------------| ---------------------------------|
| SUAS          |![](/images/SuasScen4%20(2).png)|![](/images/SuasScen4Run.png)     |
| Vehicle       |![](/images/Scen1Veh.jpg)       |![](/images/Scen1VehRun%20(2).png)|


### File Structure and Naming Conventions
If intrested in the data set follow the instructions found in the data access read me ![](README_Data_Access.md). Each file follows a secific naming convention found, described in the sesnor and naming convention powerpoint ![](general/ESCAPE%20Sensor%20Layout%20Filename%20Conv%2020201220.pptx). Each file is formatted acording to d##s##r##yyyymmdd.*** standard, where the number following "d", "s", and "r" is the numerical value assocaited with the device(sensor), scenario. and run respectivley. The only exception are the .tiff files, these files dont follow a unique format and their device, sesnor, and run can be determined by the location on the file tree.  

### Sesnsors 
This expirement used a variety of sesnors of different capbilities to form the ESCAPE dataset. All of the sesnors where either mounted on one of the four towers, part of the ESCAPE paylod, or two of the group sesnors. The table below shows what sesnors are stored at each location.The escape payload contains and EO camera, IR camera, and P-RF reciever. 
|   Location     | Sensors           | 
| -------------  | ------------------| 
| ESCAPE payload | EO, IR, P-RF      |
| Tower 1        | EO, IR, P-RF      |
| Tower 2        | Radar             |      
| Tower 3        | P-RF              |
| Tower 4        | EO                |
| Groud          | aucostic & sesmic |

Each sesnor has a number associated with them, and their placement on the field varies with the different scenarios. A visual of sesnor location are provided in the sesnor and naming convention powerpoint ![](general/ESCAPE%20Sensor%20Layout%20Filename%20Conv%2020201220.pptx). 

![](/images/sensor1layout.png)

Some of the sesnors have several components to them resulting in collection of files for just one run. For example there are 16 wav files associated with the acoustic sesnor because there are 16 microphones. Likewise there were multipe camera for per EO sesnsor producing a variety of imagrey and video data. The sesnors collected seven main data types including, .tiff, .avi, .jpg, .bin, .yuv, .csv, .wav files.

|  Infromation | Datatype | 
| -------------| ---------| 
| EO           | TIFF     |
| IR           | JPG/AVI  |
| PRF          | binary   |      
| Radar        | binary   |
| EO           | YUV      |
| Sesmic       | CSV      |
| Acoustic     | WAV      | 

DataTypes 



