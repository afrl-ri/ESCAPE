#imports
import cv2
import sys

# filepath
fp = 'd01s05r02B20181018_15_28_00.avi'

#open video 
vid = cv2.VideoCapture(fp)
i=0
while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == False:
        break
    cv2.imwrite('avi2png/%d.png' %i, frame)
    # check if can write into directory
    if not cv2.imwrite('avi2png/%d.png' %i, frame):
             raise Exception("Could not write image")
    sys.stdout.write("\rExtract frame %d " % (i + 1))
    sys.stdout.flush()
    i+=1
 
vid.release()
cv2.destroyAllWindows()
