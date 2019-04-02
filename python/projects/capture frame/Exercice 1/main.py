import numpy
import cv2

if __name__ == '__main__':

    # img = cv2.imread('potatoe.jpg',cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('Potatoe',img)
    #
    # k = cv2.waitKey(0)
    #
    # if k == 27:
    #     cv2.destroyAllWindows()
    # elif k == ord('s'):
    #     cv2.imwrite('potatoe-grey.png',img)
    #     cv2.destroyAllWindows()

    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('test.avi')

    while(True):
        ret, frame = cap.read()

        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('VideoFrame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('urigrey.png', gray)
            break

    cap.release()
    cv2.destroyAllWindows()

