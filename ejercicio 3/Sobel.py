import numpy as np
import cv2


def CompareModule(a, b, c):
    if b > a or b > c:
        res = b
    else:
        res = 0

    return res


def IsSurePediaSure(param, param1, param2, param3, param4, param5, param6, param7):

    res = 0

    if param == 1 or \
            param1 == 1 or \
            param2 == 1 or \
            param3 == 1 or \
            param4 == 1 or \
            param5 == 1 or \
            param6 == 1 or \
            param7 == 1:
        res = 1

    return res


if __name__ == '__main__':

    img = cv2.imread('valve.PNG', cv2.IMREAD_GRAYSCALE)

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

    final_matrix[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = img

    # print(angles_matrix)
    # print(final_matrix)
    # print(img)


    for j in range(0,angles_matrix.shape[1]):
        for i in range(0,angles_matrix.shape[0]):
            angle = angles_matrix[i, j]
            a = b = c = 0
            if angle < 22.5 or angle >= 157.5:
                b = final_matrix[i + zeros_margin, j + zeros_margin]
                a = final_matrix[i + zeros_margin - 1, j + zeros_margin]
                c = final_matrix[i + zeros_margin + 1, j + zeros_margin]
            elif angle < 67.5 or angle >= 22.5:
                b = final_matrix[i + zeros_margin, j + zeros_margin]
                a = final_matrix[i + zeros_margin - 1, j + zeros_margin - 1]
                c = final_matrix[i + zeros_margin + 1, j + zeros_margin + 1]
            elif angle < 112.5 or angle >= 67.5:
                b = final_matrix[i + zeros_margin, j + zeros_margin]
                a = final_matrix[i + zeros_margin, j + zeros_margin + 1]
                c = final_matrix[i + zeros_margin, j + zeros_margin - 1]
            elif angle < 157.5 or angle >= 112.5:
                b = final_matrix[i + zeros_margin, j + zeros_margin]
                a = final_matrix[i + zeros_margin - 1, j + zeros_margin + 1]
                c = final_matrix[i + zeros_margin + 1, j + zeros_margin - 1]

            img[i,j] = CompareModule(a,b,c)

    ##THRESHOLD--------------------------------------------------------------------------

    final_matrix[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = img

    sure_mat = np.zeros((img.shape[0], img.shape[1]))

    th_min = 30
    th_max = 50

    for j in range(0, img.shape[1]):
        for i in range(0, img.shape[0]):
            pixel = img[i, j]
            if pixel < th_min:
                pixel = 0.0
                sure_mat[i, j] = 0
            elif pixel >= th_max:
                pixel = 255.0
                sure_mat[i, j] = 1
            else:
                sure_mat[i, j] = 666
            img[i, j] = pixel

    ##U SURE ?-------------------------------------------------------

    final_matrix[zeros_margin:-zeros_margin,zeros_margin:-zeros_margin] = sure_mat

    for j in range(zeros_margin, img.shape[1] - zeros_margin):
        for i in range(zeros_margin, img.shape[0] - zeros_margin):
            if sure_mat[i - zeros_margin, j - zeros_margin] != 0 and sure_mat[i - zeros_margin, j - zeros_margin] != 1:
                local_sure_mat = final_matrix[i - zeros_margin:i + zeros_margin + 1, j - zeros_margin:j + zeros_margin + 1]
                img[i - zeros_margin, j - zeros_margin] = IsSurePediaSure(local_sure_mat[0, 0], local_sure_mat[1, 0], local_sure_mat[2, 0],
                                                                          local_sure_mat[0, 1], local_sure_mat[2, 1],
                                                                          local_sure_mat[0, 2], local_sure_mat[1, 2], local_sure_mat[2, 2])

    # for j in range(0, img.shape[1]):
    #     for i in range(0, img.shape[0]):
    #         if img[i, j] == 255:
    #             img[i, j] = 0
    #         else:
    #             img[i, j] = 255


    cv2.imshow('valve', np.uint8(img))
    cv2.waitKey(0)
