import numpy as np
import cv2

if __name__ == '__main__':

    img = cv2.imread('valve.png',cv2.IMREAD_GRAYSCALE)

    ##GAUSSSS ------------------------------------------------------------------
    gauss_matrix = [[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]]

    gauss_matrix = np.array(gauss_matrix)
    gauss_matrix = gauss_matrix/gauss_matrix.sum()


    zeros_margin = np.int64(gauss_matrix.shape[0]/2)
    zeros_m = np.zeros((img.shape[0]+ zeros_margin *2 ,img.shape[1] + zeros_margin *2))

    zeros_m[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = img

    final_matrix = zeros_m

    for j in range(zeros_margin,final_matrix.shape[1]-zeros_margin):
        for i in range(zeros_margin,final_matrix.shape[0]-zeros_margin):

            local_mat = final_matrix[i-zeros_margin : i+zeros_margin +1,j-zeros_margin:j+zeros_margin +1]

            img[i -zeros_margin,j -zeros_margin] = (local_mat * gauss_matrix[:,:]).sum(axis=(0,1))

    ##SOBEL----------------------------------------------------------------------------

    Gx_mat = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Gx_mat = np.array(Gx_mat)

    Gy_mat = [[-1,-2,-1],[0,0,0],[1,2,1]]
    Gy_mat = np.array(Gy_mat)

    zeros_margin = np.int64(Gx_mat.shape[0]/2)
    zeros_m = np.zeros((img.shape[0]+ zeros_margin *2 ,img.shape[1] + zeros_margin *2))
    zeros_m[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = img
    final_matrix = zeros_m

    angles_matrix = np.zeros((img.shape[0],img.shape[1]))

    for j in range(zeros_margin,final_matrix.shape[1]-zeros_margin):
        for i in range(zeros_margin,final_matrix.shape[0]-zeros_margin):

            local_mat = final_matrix[i-zeros_margin : i+zeros_margin +1,j-zeros_margin:j+zeros_margin +1]

            Gx = (local_mat * Gx_mat[:,:]).sum(axis=(0,1));
            Gy = (local_mat * Gy_mat[:,:]).sum(axis=(0,1));

            img[i -zeros_margin,j -zeros_margin] = np.sqrt(Gx**2 + Gy**2)

            angles_matrix[i -zeros_margin,j -zeros_margin] = np.int32(np.rad2deg(np.arctan2(Gy,Gx)))

            if (angles_matrix[i -zeros_margin, j -zeros_margin] < 0.0):
                angles_matrix[i - zeros_margin, j - zeros_margin] += 180

    ##ANGLES------------------------------------------------------------------------

    print(angles_matrix)

    


    cv2.imshow('valve', np.uint8(img))
    cv2.waitKey(0)