import cv2
import argparse
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200])
#    ([86, 31, 4], [220, 88, 50]),
#    ([25, 146, 190], [62, 174, 250]),
#    ([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    #ret,thresh = cv2.threshold(output,127,255,0)
    cv2.imshow("im", output)
    cv2.waitKey(0)
    
    ret,thresh = cv2.threshold(output,128,255,0)

    thresh = (255-thresh)
    thresh = cv2.cvtColor(thresh, cv2.COLOR_RGB2GRAY)
    cv2.imshow("i", thresh)

    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cv
    #cnt = contours[0]
 
    #x,y,w,h = cv2.boundingRect(cnt)
    #print x,y,w,h
    #img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("iasd", image)

    # show the images
    #cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

