import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
    Using  any programming language you feel comfortable with (it is though  recommended to use the provided free
    Matlab), load an image and then  perform a simple spatial 3x3 average of image pixels. In other words,  replace the
     value of every pixel by the average of the values in its 3x3  neighborhood. If the pixel is located at (0,0), this
     means averaging  the values of the pixels at the positions (-1,1), (0,1), (1,1), (-1,0),  (0,0), (1,0), (-1,-1),
     (0,-1), and (1,-1). Be careful with pixels at the  image boundaries. Repeat the process for a 10x10 neighborhood
     and again  for a 20x20 neighborhood. Observe what happens to the image (we will  discuss this in more details in
     the very near future, about week 3).
'''


def average_filter(image: np.ndarray , fsize: tuple = (3 , 3) , padding: str = 'valid') :
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
    
    for i in range(filtered.shape[0]) :
        for j in range(filtered.shape[1]) :
            uconv = np.multiply(image[i : i + fsize[0] , j : j + fsize[1]] , f)
            filtered[i , j , :] = np.mean(uconv , axis=(0 , 1) , keepdims=True)  # converts to "filtered" type
    
    return filtered


def main() :
    # Reading image
    image = cv2.imread('chest.jpg')
    plt.imshow(image[: , : , : :-1])  # from BGR to RGB
    
    # Applying spatial filter
    filtered = average_filter(image , fsize=(11 , 11 , 3) , padding='same')
    plt.imshow(filtered[: , : , : :-1])  # from BGR to RGB


if __name__ == '__main__' :
    main()
