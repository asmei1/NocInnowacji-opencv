import argparse # statndard library import, used to take program arguments
import cv2      # opencv import

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])

cv2.imshow("image", image)

cv2.waitKey(0)