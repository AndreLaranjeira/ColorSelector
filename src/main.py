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

# Auxiliary functions:
def isImageGreyscale(img_shape):
    if(len(img_shape) == 3 and img_shape[2] != 1):
        return False
    else:
        return True

def mouseEventHandler(event, x, y, flags, params):
    if(event == cv.EVENT_LBUTTONDOWN):
        printPixelInfo(row=y, col=x)

def printPixelInfo(row, col):
    print("Pixel information:")
    print("Row: ", row)
    print("Column: ", col)

    pixel = img[row, col]

    if(is_img_greyscale):
        print("Greyscale value: ", pixel)

    else:
        B, G, R = pixel
        print("Blue value: ", B)
        print("Green value: ", G)
        print("Red value: ", R)

    print("")


# Main function:

## Image:
if(args.image is not None and args.video is None and args.webcam == False):

    # Load image:
    img = cv.imread(args.image)

    # Check if an image was loaded:
    if(img is None):
        print("Image not found!")

    else:
        # Determine if the image has color:
        is_img_greyscale = isImageGreyscale(img.shape)

        # Configure image window:
        cv.imshow("ColorSelector", img)
        cv.setMouseCallback("ColorSelector", mouseEventHandler)

        # Wait for ESC key to be pressed:
        while(1):
            key = cv.waitKey(100) & 0xFF
            if(key == 27):
                break

        # Clean up resources:
        cv.destroyAllWindows()

## Video:
elif(args.image is None and args.video is not None and args.webcam == False):
    print("Placeholder for video.")

## Webcam:
elif(args.image is None and args.video is None and args.webcam == True):
    print("Placeholder for webcam.")

## Invalid arguments:
else:
    print("Invalid program usage! Please use exactly one argument!")
