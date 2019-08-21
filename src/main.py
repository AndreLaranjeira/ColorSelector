# Program to highlight the color of a pixel selected in an image or video.

# Libraries:
import argparse
import cv2 as cv
import numpy as np

# User modules:

# Argument parser:
parser = argparse.ArgumentParser(description='Color selector in image and video.')
parser.add_argument('-i', type=str, dest='image',
                    help="path to a jpg image file.")
parser.add_argument('-v', type=str, dest='video',
                    help="path to an avi video file.")
parser.add_argument('-w', dest='webcam', action='store_true', default=False,
                    help="use webcam input as video source.")
args = parser.parse_args()

# Main function:

## Image:
if(args.image is not None and args.video is None and args.webcam == False):
    print("Placeholder for image.")


## Video:
elif(args.image is None and args.video is not None and args.webcam == False):
    print("Placeholder for video.")

## Webcam:
elif(args.image is None and args.video is None and args.webcam == True):
    print("Placeholder for webcam.")

## Invalid arguments:
else:
    print("Invalid program usage! Please use only one argument at a time!")
