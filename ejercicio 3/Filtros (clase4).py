import numpy as np
import  cv2

if __name__ == '__main__':

    img = cv2.imread('patata.png',cv2.IMREAD_ANYCOLOR)

    gauss_matrix = cv2.getGaussianKernel((3,3),-1)

    zeros_m = np.zeros(img.shape[0]+1,img.shape[1]+1)

    zeros_m[1:img.shape[0],1:img.shape[1]] = img[:]

    final_matrix = zeros_m

    print(gauss_matrix)

    for j in range(1,img.shape[1] - 1):
        for i in range(1,img.shape[0] - 1):

            local_mat = final_matrix[i-1 : i+1,j-1:i+1]

            for x in range(0, local_mat.shape[1]):
                for y in range(local_mat.shape[0]):
                    local_mat[x,y] *= gauss_matrix[x,y]

            img[i,j] = np.mean(local_mat)

            #INACABADO
            # if i > 0 and j > 0:
            #     img[i, j] += img[i - 1, j - 1]
            # if i > 0:
            #     img[i, j] += img[i - 1,j]
            # if i < img.shape[0] - 1 and j < img.shape[1] - 1:
            #     img[i, j] += img[i -1,j +1]
            #
            # if j > 0:
            #     img[i, j] += img[i, j - 1]
            # img[i, j] += img[i, j]
            # if i > 0 and j > 0:
            #     img[i, j] += img[i, j + 1]
            #
            # if i > 0 and j > 0:
            #     img[i, j] += img[i + 1, j - 1]
            # if i > 0 and j > 0:
            #     img[i, j] += img[i + 1, j]
            # if i > 0 and j > 0:
            #     img[i, j] += img[i + 1, j + 1]
            #
            # img[i, j] / 9

    cv2.imshow('patata', img)
    cv2.waitKey(0)

