import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate(array: np.ndarray , degree: float , option: str = 'crop') :
    # Convert from degre to radian
    rad = (np.pi / 180) * degree
    
    # Creating array of zeros
    rot = np.zeros(array.shape , dtype=np.uint8)
    
    # Finding middle point
    shape = np.array(rot.shape)
    middle = np.divide(shape , 2)
    
    # Defining rotation matrix
    rmatrix = np.array([np.cos(rad) , -np.sin(rad) ,
                        np.sin(rad) , np.cos(rad)])
    
    # Rotating array
    for i in range(shape[0]) :
        for j in range(shape[1]) :
            # Converting point to array
            point = np.array([i , j])
            # Getting rotated point
            rpoint = np.multiply(point - middle , rmatrix)
            
            # Rounding rpoint values to the closest integer and adding middle again
            rpoint = np.round(rpoint) + middle
            
            assert (shape > rpoint >= 0).all , 'Check your rotation method.'
            rot[point] = array[rpoint]
    
    return rot


def main() :
    path = ''


if __name__ == '__main__' :
    main()
