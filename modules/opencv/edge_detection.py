import cv2
import matplotlib.pyplot as plt
import os

currect_dir = os.getcwd()
path = os.path.join(currect_dir, "opencv","mypic.jpg")
path = path.replace("\\", "/")
print(path)
img = cv2.imread(path)

# img = cv2.imread('C:/Users/korad/Desktop/python examples/modules/opencv/mypic.jpg')

half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
edge_image = cv2.Canny(image= half, threshold1=100, threshold2=400)

cv2.imshow("image", edge_image)

cv2.waitKey(0)
cv2.destroyAllWindows()