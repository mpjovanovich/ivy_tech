from easyocr import Reader
import argparse
import cv2
import os

# Example usage: python3 python_easyocr.py --image_directory '/mnt/c/Users/mpjov/Downloads/TestOcr' 
    # --target_string 'smart solutions' --confidence .25 --use_gpu 1

parser = argparse.ArgumentParser()
parser.add_argument('--image_directory', type=str, required=True, 
    help='path to directory with images to search')
parser.add_argument('--target_string', type=str, required=True, 
    help='string(s) to search for, separated by spaces')
parser.add_argument('--confidence', type=float, required=True, 
    help='threshold for positive result; set float between 0 and 1')
parser.add_argument('--use_gpu', type=int, required=True, 
    help='set to 1 to use GPU; otherwise use 0')
args = vars(parser.parse_args())

search_directory = args['image_directory']
target_strings = args['target_string'].split(' ')
prob_threshold = args['confidence']
use_gpu = args['use_gpu'] > 0

# print(search_directory,target_strings,prob_threshold,use_gpu)

# for file in os.path.abspath(search_directory):
for root, dirs, files in os.walk(os.path.abspath(search_directory)):
    for file in files:
        # image = cv2.imread('/mnt/c/Users/mpjov/Downloads/test_ocr.jpg')
        image = cv2.imread(os.path.join(root, file))
        reader = Reader(['en'], gpu=True)
        results = reader.readtext(image)

        for (bbox, text, prob) in results:
            # Adjust probability threshold if desired
            if prob >= prob_threshold and any(target == text.casefold() 
                for target in target_strings):

                # Print what we found and bail on the loop
                print(f'File: {file}; Text found: {text}; Confidence: {prob:.4f}')
                break