import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate(array: np.ndarray , degree: float , option: str = 'crop') :
    # Convert from degre to radian
    rad = (np.pi / 180) * degree
    
    # Creating array of zeros
    rot = np.zeros(array.shape , dtype=np.uint8)
    
    # Finding middle point
    shape = np.array(rot.shape)[:2]
    middle = np.divide(shape , 2).astype(int)
    
    # Defining rotation matrix
    rmatrix = np.array([[np.cos(rad) , -np.sin(rad)] ,
                        [np.sin(rad) , np.cos(rad)]])
    
    # Rotating array
    for i in range(shape[0]) :
        for j in range(shape[1]) :
            # Converting point to array
            point = np.array([i , j])
            
            # Getting rotated point
            rpoint = np.dot(point.reshape(1 , -1) - middle , rmatrix)
            
            # Rounding rpoint values to the closest integer and adding middle again
            rpoint = np.round(rpoint).astype(int) + middle
            rpoint = rpoint.reshape(-1)
            
            if (shape > rpoint).all() and (rpoint >= 0).all() :
                rot[point[0] , point[1] , :] = array[rpoint[0] , rpoint[1] , :]
    
    return rot


def main() :
    path = os.path.join('week1' , 'seu-madruga.jpg')
    array = cv2.imread(path)
    
    degree = 45
    rot = rotate(array , degree=degree)
    
    fig , axis = plt.subplots(2 , 1)
    axis[0].imshow(array[: , : , : :-1])
    axis[0].set_title('original')
    axis[1].imshow(rot[: , : , : :-1])
    axis[1].set_title(f'rotated {degree} degreed')


if __name__ == '__main__' :
    main()
