import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from IPython.display import clear_output

from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot

def show_img(img, bigger=False):
    if bigger:
        plt.figure(figsize=(10,10)) 
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()
    
def sharpen(img, sigma=200):    
    # sigma = 5、15、25
    blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
    usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
    
    return usm

# sharpen
def img_processing(img):
    # do something here
    img = sharpen(img)

    return img

# like sharpen
def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr

# restoring models
def edsr(origin_img):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()

    path = "EDSR_x4.pb"

    sr.readModel(path)

    sr.setModel("edsr",4)

    result = sr.upsample(origin_img)
    
    return result

def espcn(origin_img):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()

    path = "ESPCN_x4.pb"

    sr.readModel(path)

    sr.setModel("espcn",4)

    result = sr.upsample(origin_img)
    
    return result

def fsrcnn(origin_img):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()

    path = "FSRCNN_x4.pb"

    sr.readModel(path)

    sr.setModel("fsrcnn",4)

    result = sr.upsample(origin_img)
    
    return result

def lapsrn(origin_img):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()

    path = "LapSRN_x4.pb"

    sr.readModel(path)

    sr.setModel("lapsrn",4)

    result = sr.upsample(origin_img)
    
    return result

def uint_to_float(img, method='NTSC'):
    img = img.astype(np.float32) / 255
    b,g,r = cv2.split(img)
    
    if method == 'average':
        gray = (r + g + b) / 3
    elif method == 'NTSC':
        gray = 0.2989*r + 0.5870*g + 0.1140*b
        
    #gray = (gray*255).astype('uint8')
    
    return gray