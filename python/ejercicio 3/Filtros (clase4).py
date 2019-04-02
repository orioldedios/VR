import numpy as np
import  cv2

if __name__ == '__main__':

    img = cv2.imread('patata.png',cv2.IMREAD_ANYCOLOR)

    gauss_matrix = [[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]]

    gauss_matrix = np.array(gauss_matrix)
    gauss_matrix = gauss_matrix/gauss_matrix.sum()


    zeros_margin = np.int64(gauss_matrix.shape[0]/2)
    zeros_m = np.zeros((img.shape[0]+ zeros_margin *2 ,img.shape[1] + zeros_margin *2,3))

    print(zeros_m.shape)
    print(img.shape)
    zeros_m[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = img

    final_matrix = zeros_m

    for j in range(zeros_margin,final_matrix.shape[1]-zeros_margin):
        for i in range(zeros_margin,final_matrix.shape[0]-zeros_margin):

            local_mat = final_matrix[i-zeros_margin : i+zeros_margin +1,j-zeros_margin:j+zeros_margin +1]

            img[i -zeros_margin,j -zeros_margin] = (local_mat * gauss_matrix[:,:,np.newaxis]).sum(axis=(0,1))

    cv2.imshow('patata', np.uint8(img))
    cv2.waitKey(0)

