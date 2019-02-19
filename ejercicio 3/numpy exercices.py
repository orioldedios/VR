import numpy as np

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

    matrix8 = np.random.random((5,5)) #15 CONTINUARA....
