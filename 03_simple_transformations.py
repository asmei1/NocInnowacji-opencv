import argparse # standard library import, used to take program arguments
import cv2      # opencv import
import numpy as np
 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])

cv2.imshow("image", image)
cv2.waitKey(0)

# divide image on channels
zeros = np.zeros(image.shape[:2], dtype="uint8")
(blue_channel, red_channel, green_channel) = cv2.split(image)

# to display only one channel, we have to merge it with array with zeros.
# If we don't do that, opencv in imshow treat it as grayscale image.
cv2.imshow("blue", cv2.merge([blue_channel, zeros, zeros]))
cv2.imshow("red", cv2.merge([zeros, red_channel,zeros]))
cv2.imshow("green", cv2.merge([zeros, red_channel, green_channel]))

cv2.waitKey(0)