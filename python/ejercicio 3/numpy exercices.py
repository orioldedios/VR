import numpy as np
import cv2

if __name__ == '__main__':

    vector = np.zeros(shape=(10)) #1

    vector2 = np.zeros(shape=(10)) #2
    vector2[4] = 1

    min = 10
    max = 49
    vector3 = np.arange(min,max + 1) #3

    matrix1 = np.array(np.arange(1,10)).reshape(3,3) #4

    matrix2 = np.array(np.arange(1,10)).reshape(3,3) #5
    matrix2 = np.flip(matrix2,1)

    matrix2 = np.array(np.arange(1,10)).reshape(3,3) #6
    matrix2 = np.flip(matrix2,0)

    matrix3 = np.eye(3) #7

    matrix4 = np.random.random((3,3)) #8

    average = np.random.randint(0,10,10).mean() #9

    matrix5 = np.zeros((10,10))

    matrix6 = np.zeros((5,5))
    matrix6[:] = np.array(np.arange(1,6)) #11

    vector4 = np.float64(np.random.randint(0,100,9).reshape((3,3)))#12

    matrix7 = np.float64(np.random.randint(0,100,25).reshape((5,5))) #13
    average1 = matrix7.mean()
    matrix7[:] -= average1

    matrix7 = np.float64(np.random.randint(0,100,25).reshape((5,5))) #14
    average2 = np.mean(matrix7,1).reshape((5,1))
    matrix7 = np.subtract(matrix7,average2)

    matrix8 = np.random.randint(0,10,9).reshape((3,3)) #16
    res = (np.size(matrix8[matrix8 > 5]))

    size = 255
    realsize = 400
    foto = np.ones((size,size,3),np.uint8) *255

    # tufifi = np.ones((size,size),np.uint8) * 255
    # colour = np.flip(np.arange(0,256,256/size,np.uint8))
    #
    # foto[:,:,0] = tufifi
    # foto[:, :, 1] = colour
    # foto[:, :, 2] = colour
    #
    tufifiR = (np.random.random(size) * 255)
    tufifiG = (np.random.random(size) * 255)
    tufifiB = (np.random.random(size) * 255)

    foto[:,:,0] = tufifiB
    foto[:,:,1] = tufifiG
    foto[:,:,2] = tufifiR

    foto = cv2.resize(foto,(realsize,realsize)) #si quieres mas resolucion normaliza de 0 a 1 y multiplica y haz miierdas yokese pregunta ajony/profe
    cv2.imshow("foto",foto)
    cv2.waitKey()
