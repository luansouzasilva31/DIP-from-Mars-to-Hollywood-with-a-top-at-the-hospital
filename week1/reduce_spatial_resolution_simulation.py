import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
    For  every 3x3 block of the image (without overlapping), replace  all corresponding 9 pixels by their
    average. This operation simulates  reducing the image spatial resolution. Repeat this for 5x5  blocks
    and 7x7 blocks. If you are using Matlab, investigate  simple command lines to do this important operation.
'''


def reduce_spatial_res(image: np.ndarray , fsize: tuple = (3 , 3) , padding: str = 'valid') :
    hs = fsize[0] // 2
    vs = fsize[1] // 2
    
    # Creating mean filter
    f = np.ones(fsize)
    
    # Creating empty filtered array
    if padding == 'valid' :
        filtered = np.zeros(image.shape - np.array([2 * hs , 2 * vs , 0]) , dtype=np.uint8)
    elif padding == 'same' :
        filtered = np.zeros(image.shape , dtype=np.uint8)
        image = np.pad(image , [(hs , hs) , (vs , vs) , (0 , 0)] , mode='constant')
    else :
        raise NotImplementedError('Choose a valid option of padding.')
    
    for i in range(0 , filtered.shape[0] , fsize[0]) :
        for j in range(0 , filtered.shape[1] , fsize[1]) :
            # Analyse x-axis
            if i + fsize[0] <= filtered.shape[0] :
                xi = i
                xf = i + fsize[0]
            else :
                xi = filtered.shape[0] - fsize[0]
                xf = filtered.shape[0]
            
            # Analyse y-axis
            if j + fsize[1] <= filtered.shape[1] :
                yi = j
                yf = j + fsize[1]
            else :
                yi = filtered.shape[1] - fsize[1]
                yf = filtered.shape[1]
            
            uconv = np.multiply(image[xi : xf , yi : yf] , f)
            filtered[xi : xf , yi :yf , :] = np.mean(uconv , axis=(0 , 1) , keepdims=True)
    
    return filtered


def main() :
    # Reading image
    image = cv2.imread(os.path.join('week1' , 'seu-madruga.jpg'))
    plt.imshow(image[: , : , : :-1])  # from BGR to RGB
    
    # Applying spatial filter
    filtered = reduce_spatial_res(image , fsize=(25 , 25 , 3) , padding='same')
    plt.imshow(filtered[: , : , : :-1])  # from BGR to RGB


if __name__ == '__main__' :
    main()
