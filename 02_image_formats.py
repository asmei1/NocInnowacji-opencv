import argparse # standard library import, used to take program arguments
import cv2      # opencv import

import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])

# show image using the matplotlib. Looks strange, right?
plt.imshow(image)
plt.show()

# Because OpenCV reads image with BRG format to RGB format 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.imshow(image)
plt.show()
