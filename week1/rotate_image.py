import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate(array: np.ndarray , degree: float , option: str = 'same') :
    # Convert from degre to radian
    rad = (np.pi / 180) * degree
    
    # Finding middle point
    ishape = np.array(array.shape)[:2]  # input shape
    imid = np.divide(ishape , 2).astype(int)  # input middle point
    
    # Defining rotation matrix
    rmatrix = np.array([[np.cos(rad) , -np.sin(rad)] ,
                        [np.sin(rad) , np.cos(rad)]])
    
    # Verifying option and related
    if option == 'same' :
        oshape = ishape.copy()  # output shape
        omid = imid.copy()  # output middle point
    
    elif option == 'full' :
        # Getting output shape
        m = np.array([[np.cos(rad) , np.sin(rad)] ,
                      [np.sin(rad) , np.cos(rad)]])
        oshape = np.abs(np.dot(ishape , m).astype(int))
        
        # Getting center
        omid = np.divide(oshape , 2).astype(int)
    
    else :
        raise NotImplementedError(f'option={option} is invalid.')
    
    # Creating array of zeros
    rot = np.zeros((oshape[0] , oshape[1] , array.shape[-1]) , dtype=np.uint8)
    
    # Rotating array
    for i in range(oshape[0]) :
        for j in range(oshape[1]) :
            # Converting point to array
            point = np.array([i , j])
            
            # Getting rotated point
            rpoint = np.dot(point.reshape(1 , -1) - omid , rmatrix)
            
            # Rounding rpoint values to the closest integer and adding middle again
            rpoint = np.round(rpoint).astype(int) + imid
            rpoint = rpoint.reshape(-1)
            
            if (oshape > rpoint).all() and (rpoint >= 0).all() and (rpoint < ishape).all():
                rot[point[0] , point[1] , :] = array[rpoint[0] , rpoint[1] , :]
    
    return rot


def main() :
    path = os.path.join('week1' , 'seu-madruga.jpg')
    array = cv2.imread(path)
    
    degree = 45
    rot = rotate(array , degree=degree, option='same')
    
    fig , axis = plt.subplots(2 , 1)
    axis[0].imshow(array[: , : , : :-1])
    axis[0].set_title('original')
    axis[1].imshow(rot[: , : , : :-1])
    axis[1].set_title(f'rotated {degree} degreed')


if __name__ == '__main__' :
    main()
