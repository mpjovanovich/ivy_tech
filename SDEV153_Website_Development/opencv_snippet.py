import cv2
import imutils
import os
from selenium import webdriver
from skimage.metrics import structural_similarity as compare_ssim

# https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/

IMAGE_DIR = "/mnt/c/Users/mpjov/Desktop/images"

# # Initialize the WebDriver (e.g., Chrome, Firefox, Edge)
# driver = webdriver.Chrome()
# driver.get("https://example.com")

# driver.save_screenshot(os.path.join(IMAGE_DIR, "screenshot1.png"))
# driver.save_screenshot(os.path.join(IMAGE_DIR, "screenshot2.png"))

# driver.quit()

# Load the two images you want to compare
image1 = cv2.imread(os.path.join(IMAGE_DIR, "screenshot1.png"))
image2 = cv2.imread(os.path.join(IMAGE_DIR, "screenshot2.png"))

# Convert the images to grayscale
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(image1_gray, image2_gray, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(image1_gray, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(image2_gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
# cv2.imshow("Original", image1_gray)
# cv2.imshow("Modified", image2_gray)
# cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)

cv2.imwrite(os.path.join(IMAGE_DIR, "diff.png"), image2_gray)
cv2.waitKey(0)
