import glob
import os
import argparse
import cv2 as cv
from image_functions import *

path = os.getcwd()
images = glob.glob("input/*")

parser = argparse.ArgumentParser(
    description="Photo converter with multiple modes (grayscale, sepia, mirror, and reflect"
)

parser.add_argument("mode", help="Select a photo processing mode.")

args = parser.parse_args()

# Create new directory for output
while True:
    if os.path.exists("./output") is True:
        break
    else:
        os.mkdir("./output")

for image in images:
    img = cv.imread(image)
    img_name = image[len("input/") :]
    h = img.shape[0]
    w = img.shape[1]

    if args.mode == "grayscale":
        new_name = f"g_{img_name}"
        cv.imwrite(os.path.join(f"{path}/output", new_name), grayscale(img, h, w))
    if args.mode == "sepia":
        new_name = f"s_{img_name}"
        cv.imwrite(os.path.join(f"{path}/output", new_name), sepia(img, h, w))
    if args.mode == "mirror":
        new_name = f"m_{img_name}"
        cv.imwrite(os.path.join(f"{path}/output", new_name), mirror(img, h, w))
    if args.mode == "reflect":
        new_name = f"r_{img_name}"
        cv.imwrite(os.path.join(f"{path}/output", new_name), reflect(img, h, w))
    if args.mode == "scale":
        new_name = f"sc_{img_name}"
        cv.imwrite(os.path.join(f"{path}/output", new_name), scale(img, h, w))
