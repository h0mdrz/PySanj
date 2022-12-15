import numpy as np
import cv2 as cv
def a():
    img = cv.imread('exam.jpg')
    img = cv.resize(img, (800, 400))
    img = img[0:00 + 352, 215:215 + 560]
    def s(t, e):
        if t == 0:
            t = 25 * t + (t - 1) * 18 - 15
        else:
            t = 25 * t + (t - 1) * 18 - 9
        e = 18 * e + (e - 1) * 46 - 2
        pic = img[t:t + 18, e:e + 46]
        f = 0
        for y in range(18):
            for x in range(46):
                if pic[y, x][0] > 100:
                    f += 1
        if f > 414:
            return 0
        else:
            return 1
    o = np.zeros([8, 4], dtype=int)
    for i in range(8):
        for j in range(4):
            o[i, j] = s((i + 1), (j + 1))
    return o
