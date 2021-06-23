# File Paths
imgZerFP = 'image_0001_25518416696154.tiff'
imgOneFP = 'image_0002_25521016659129.tiff'
# imports 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# open image one 
imgZer = mpimg.imread(imgZerFP)
print("Image One Size", np.shape(imgZer))
# open image 2
imgOne = mpimg.imread(imgOneFP)
print("Image Two Size", np.shape(imgOne))
# plot both images
imgplotZer = plt.imshow(imgZer)
plt.figure()
imgplotOne = plt.imshow(imgOne)
# check if images are identical
if (np.shape(imgZer) != np.shape(imgOne)):
    print("Images not the same size")
    system.exit(0)
else:
    if(np.any(imgZer) != np.any(imgOne)):
        print("Images are not identical")
        system.exit(0)
print("Images are identical")
                    
