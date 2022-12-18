import cv2
import glob
import os
import argparse
import warnings
warnings.filterwarnings("ignore")

images=[]
value=[]


src = 'BreastCancer'
dest  = 'Output'



def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


def preprocessing():
    global images
    images=[cv2.imread(file) for file in glob.glob("BreastCancer/*.jpg")]

    for i in range(len(images)):
        global result
        gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)

        if fm >100:
            text="jelas"

        cv2.putText(images[i], "{:.2f}".format(fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        value.append(fm)

def sorting():
    for k in range(len(value)):
        for i in range(len(value)-1):
            if value[i]>value[i+1]:
                temp=images[i]
                images[i]=images[i+1]
                images[i+1]=temp
                temp1=value[i]
                value[i]=value[i+1]
                value[i+1]=temp1
def output():
    os.mkdir('Output')
    for index in range(len(images)):
        filename = f'img_{index}.jpg'
        img_des = os.path.join(dest, filename);
        cv2.imwrite(img_des ,images[index]);

preprocessing()
sorting()
output()