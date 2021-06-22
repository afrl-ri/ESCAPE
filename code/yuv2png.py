# imports
import cv2
import numpy as np
import sys

# yuv file name
filename = "d01s05r0520181018_15_56_00.yuv"

# define method using yuv parameters
def yuv2bgr(filename, height, width, startfrm):
    """
    :param filename: the name of the YUV video to be processed
         :param height: the height of the image in the YUV video
         :param width: the width of the image in the YUV video
         :param startfrm: start frame
    :return: None
    """
    # open file
    fp = open(filename, 'rb')
    
    # calculcate framsize based on height and width 
    framesize = height * width * 3 // 2  # The number of pixels in a frame of image
    h_h = height // 2
    h_w = width // 2

    fp.seek(0, 2)  # Set the file pointer to the end of the file stream
    ps = fp.tell()  # Current file pointer position
    numfrm = ps // framesize  # Calculate the number of output frames
    fp.seek(framesize * startfrm, 0)

    for i in range(numfrm - startfrm):
        Yt = np.zeros(shape=(height, width), dtype='uint8', order='C')
        Ut = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')
        Vt = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')

        for m in range(height):
            for n in range(width):
                Yt[m, n] = ord(fp.read(1))
        for m in range(h_h):
            for n in range(h_w):
                Ut[m, n] = ord(fp.read(1))
        for m in range(h_h):
            for n in range(h_w):
                Vt[m, n] = ord(fp.read(1))

        img = np.concatenate((Yt.reshape(-1), Ut.reshape(-1), Vt.reshape(-1)))
        img = img.reshape((height * 3 // 2, width)).astype('uint8')  # YUV storage format is: NV12 (YYYY UV)

        # Since opencv cannot directly read YUV format files, it is necessary to convert the format
        bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # Pay attention to the storage format of YUV
        cv2.imwrite('yuv2bgr/%d.png' %i, bgr_img) #'./yuv_images/yuv2bgr/%d.png'
        if not cv2.imwrite('yuv2bgr/%d.png' %i, bgr_img):
             raise Exception("Could not write image")
        #print("\r Extract frame %d " % (i + 1))
        sys.stdout.write("\rExtract frame %d " % (i + 1))
        sys.stdout.flush()

    fp.close()
    print("job done!")
    return None


if __name__ == '__main__':
    _ = yuv2bgr(filename, height=3296, width=2472, startfrm=0)
