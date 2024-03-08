import time
import cv2
from cv2  import dnn_superres
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

image_path=r'./images'
output_path=r'./outputs'


MODEL_LIST = [
    {"name": "EDSR", "path":"./models/x2/EDSR_x2.pb", "scale":2},
    {"name": "ESPCN", "path":"./models/x2/ESPCN_x2.pb", "scale":2},
    {"name": "FSRCNN", "path":"./models/x2/FSRCNN_x2.pb", "scale":2},
    {"name": "LAPSRN", "path":"./models/x2/LapSRN_x2.pb", "scale":2},
    {"name": "interpolation", "path":"./models/x2/interpolation", "scale":2},
    
    {"name": "EDSR", "path":"./models/x3/EDSR_x3.pb", "scale":3},
    {"name": "ESPCN", "path":"./models/x3/ESPCN_x3.pb", "scale":3},
    {"name": "FSRCNN", "path":"./models/x3/FSRCNN_x3.pb", "scale":3},
    {"name": "interpolation", "path":"./models/x3/interpolation", "scale":3},
    
    {"name": "EDSR", "path":"./models/x4/EDSR_x4.pb", "scale":4},
    {"name": "ESPCN", "path":"./models/x4/ESPCN_x4.pb", "scale":4},
    {"name": "FSRCNN", "path":"./models/x4/FSRCNN_x4.pb", "scale":4},
    {"name": "LAPSRN", "path":"./models/x4/LapSRN_x4.pb", "scale":4},
    {"name": "interpolation", "path":"./models/x4/interpolation", "scale":4},
    
    {"name": "LAPSRN", "path":"./models/x8/LapSRN_x8.pb", "scale":8},
    {"name": "interpolation", "path":"./models/x8/interpolation", "scale":8},
    ]

def calculate_psnr(original,new):
    
    return cv2.PSNR(original,new)

def calculate_mse(original,new):
    return (np.square(original - new)).mean(axis=None)

def calculate_ssim(original,new):
    return ssim(original, new, channel_axis=2)

def save_image(path, result):
    cv2.imwrite(path,result)

def model_run(enable_write):
    for model in MODEL_LIST:
        name = model['name']
        path = model['path']
        scale = model['scale']
        if name!='interpolation':
            sr=dnn_superres.DnnSuperResImpl_create()
            sr.readModel(path)
            sr.setModel(name.lower(),scale)
        for i in os.listdir(image_path):
            input_image=cv2.imread(os.path.join(image_path,i))
            input_image = cv2.resize(input_image, (int(input_image.shape[1]/scale),int(input_image.shape[0]/scale)))
            processed_image = cv2.resize(input_image, (int(input_image.shape[1]*scale),int(input_image.shape[0]*scale)))
            
            if name=='interpolation':
                path=os.path.join(output_path,f'x{scale}',f'{name}',i)
                if enable_write==True:
                    save_image(path,processed_image)
                continue

            path=os.path.join(output_path,f'x{scale}')
            path=os.path.join(path,f'{name}_x{scale}.pb')
            path=os.path.join(path,i)
            
            
            begin=time.time()
            result_image=sr.upsample(input_image)
            interval=time.time()-begin
            print(scale)
            print(name)
            print(f'Time is : {interval}')
            print(f'PSNR is : {calculate_psnr(processed_image, result_image)}')
            print(f'MSE is : {calculate_mse(processed_image, result_image)}')
            print(f'SSIM is : {calculate_ssim(processed_image, result_image)}')
            
            print('')
            if enable_write==True:
                save_image(path,result_image)
                
                  

model_run(True)




        



