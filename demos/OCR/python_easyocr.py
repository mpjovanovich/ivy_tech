from easyocr import Reader
import argparse
import cv2
import os

# Example usage (find anything):
# python python_easyocr.py --image_directory '/somepath/images'

# Example usage (find target):
# python python_easyocr.py --image_directory '/somepath/images' --target_string 'smart solutions' --confidence .25

# Note: it will print a nag message to stderr if you run with --use-gpu 0.
# You can choose to redirect only stdin to a file, append: 1> results.txt,
# or if on the console redired stderr to null, append: 2> /dev/null.

# There is little to no validation in this script. Make sure the image directory
# only contains images, or it will blow up with a vector error.

parser = argparse.ArgumentParser()
parser.add_argument(
    "--image_directory",
    type=str,
    required=True,
    help="path to directory with images to search",
)
parser.add_argument(
    "--target_string",
    type=str,
    required=False,
    default="",
    help="string(s) to search for, separated by spaces",
)
parser.add_argument(
    "--confidence",
    type=float,
    required=False,
    default=0.00,
    help="threshold for positive result; set float between 0 and 1",
)
parser.add_argument(
    "--use_gpu",
    type=int,
    required=False,
    default=True,
    help="set to 1 to use GPU; otherwise use 0",
)
args = vars(parser.parse_args())

search_directory = args["image_directory"]
target_strings = args["target_string"].split(" ")
prob_threshold = args["confidence"]
use_gpu = args["use_gpu"] > 0

# Debug statements:
# print(search_directory, target_strings, prob_threshold, use_gpu)

for root, dirs, files in os.walk(os.path.abspath(search_directory)):
    for file in files:
        image = cv2.imread(os.path.join(root, file))
        reader = Reader(["en"], gpu=True)
        results = reader.readtext(image)

        # Sort results by confidence, highest to lowest
        # Don't spend CPU on this if we're searching - only if we want a full list.
        if target_strings == [""]:
            results.sort(key=lambda x: x[2], reverse=True)

        for bbox, text, prob in results:
            if target_strings == [""]:
                # If no target string is provided, just print everything
                print(f"File: {file:<20} Text: {text:<20} Confidence: {prob:.4f}")
                continue

            # Otherwise search for the target string(s) and print if found
            # Adjust probability threshold if desired
            if prob >= prob_threshold and any(
                target in text.casefold() for target in target_strings
            ):
                # Print what we found and bail on the loop
                print(f"File: {file:<20} Text: {text:<20} Confidence: {prob:.4f}")
                break
