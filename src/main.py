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
def highlightInImage(img, color):
    result = np.copy(img)

    # Create auxiliary variables to stop integer overflow in subtractions:
    aux_img = np.array(img, dtype=np.int32)
    aux_color = np.array(color, dtype=np.int32)

    # Calculate distance:
    distance = (aux_img - aux_color) ** 2

    # Greyscale logic for an image with 3 channels:
    if(is_img_greyscale and len(img.shape) == 3):
        mask = np.where((distance[:,:,0] < (13 ** 2)), True, False)
        result[(mask)] = [255]

    # Greyscale logic for an image with 2 channels:
    elif(is_img_greyscale and len(img.shape) == 2):
        mask = np.where((distance < (13 ** 2)), True, False)
        result[(mask)] = [255]

    # Color logic:
    else:
        mask = np.where(((distance[:,:,0] + distance[:,:,1] + distance[:,:,2]) < (13 ** 2)), True, False)
        result[(mask)] = [0, 0, 255]

    return result

def isImageGreyscale(img_shape):
    if(len(img_shape) == 3 and img_shape[2] != 1):
        return False
    else:
        return True

def mouseEventHandler(event, x, y, flags, params):
    if(event == cv.EVENT_LBUTTONDOWN):
        pixel_row = y
        pixel_col = x
        pixel_color = img[pixel_row, pixel_col]
        printPixelInfo(row=pixel_row, col=pixel_col, color=pixel_color)

        # Add pixel color to highlighted colors:
        highlighted_color.clear()
        highlighted_color.append(pixel_color)

def printPixelInfo(row, col, color):
    print("Pixel information:")
    print("Row: ", row)
    print("Column: ", col)

    if(is_img_greyscale):
        print("Greyscale value: ", color)

    else:
        B, G, R = color
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

        # Initiate the color variable:
        highlighted_color = []

        # Main event loop:
        while(1):

            # Highlight selected color in image:
            if(highlighted_color):
                new_img = highlightInImage(img, highlighted_color[0])
                cv.imshow("ColorSelector", new_img)
                highlighted_color.clear()

            # Read user input:
            key = cv.waitKey(100) & 0xFF

            # Exit application:
            if(key == 27):
                break

            # Clean image:
            elif(key == ord('c')):
                cv.imshow("ColorSelector", img)

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
