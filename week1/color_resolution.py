import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
    Write  a computer program capable of reducing the number of intensity levels  in an image from 256 to 2, in integer
    powers of 2. The desired number of  intensity levels needs to be a variable input to your program.
'''


def intensity_levels(image: np.ndarray , n_levels: int) :
    assert np.log2(n_levels).is_integer() , '`n_levels` must be power of 2'
    
    # Converting image color to n_levels precision considering max as uint8 (256 possible values)
    color_step = 256 // n_levels
    image = np.divide(image , color_step).astype(int) * color_step
    
    return image


def main() :
    # Reading image
    image = cv2.imread('chest.jpg')
    plt.imshow(image[: , : , : :-1])  # from BGR to RGB
    
    # Applying intensity level change
    newimage = intensity_levels(image , 2)
    plt.imshow(newimage[: , : , : :-1])  # from BGR to RGB


if __name__ == '_main__' :
    main()
