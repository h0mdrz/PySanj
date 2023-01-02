import os
import numpy as np
import cv2 as cv
import re

iouh = 0
def ct(p, u):
    e = 0
    global iouh
    iouh = 0
    for i in range(len(p)):
        f = 0
        for j in range(4):
            if p[i][j] == 1:
                if f != 0 and f != "error":
                    if u != 0:
                        f = "f"
                    else:
                        f = "error"
                    e += 1
                else:
                    f = str(j + 1)
            elif j == 3 and f == 0:
                if u != 0:
                    f = "0"
                else:
                    f = "error"
                e += 1
        if u != 0:
            rtge = 0
            if f == "0":
                rtge = "-"
            else:
                if u[i] == f:
                    iouh+=1
                    rtge = "✓"
                else:
                    iouh-=.25
                    rtge = "✕"
            print("+ " + str(i + 1) + " ( " + f + " ?= " + u[i] + " ) => ( " + rtge + " )")
        else:
            print("+ " + str(i + 1) + " ( " + f + " )")


def a(v):
    img = cv.imread(v)
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


def lc(cs):
    for i in range(len(cs)):
        print("+ " + str(i + 1) + " " + cs[i])


def cc():
    global c
    global cs
    if int(c) >= len(cs) or int(c) < 0 or not re.compile("[0-9]+").fullmatch(str(c)):
        print("- Invalid command!")
        print("- Retry with another value:")
        c = int(input("> ")) - 1
        cc()


def nt():
    print("- Please type a name for your new test:")
    t = input("> ")
    if not os.path.exists('psnj/'):
        os.mkdir('psnj')
    while t == "" or not re.compile("[0-9a-zA-Z]+").fullmatch(t) or os.path.exists('psnj/'+t):
        if os.path.exists('psnj/'+t):
            print("- Test with this name already exits:")
        else:
            print("- Invalid test name!")
        print("- Retry with another value:")
        t = input("> ")
    os.mkdir('psnj/'+t)
    print("- Please choose how to import test keys")
    global c
    global cs
    cs = ["Upload by file", "Upload manually"]
    lc(cs)
    c = int(input("> ")) - 1
    cc()
    if c == 0:
        print("- Okay! Please type path of test key file without extension name (only jpg allowed):")
        y = input("> ")
        while y == "" or not re.compile("[0-9a-zA-Z]+").fullmatch(y) or not os.path.exists(y + ".jpg"):
            print("- Invalid File")
            print("- Retry with another value:")
            y = input("> ")
        open('psnj/'+t+'/tsky', 'w')
        print("- " + y + ".jpg File detected!")
        print("- Preview:")
        ct(a(y + ".jpg"), 0)


print("> PySanj v0.2")
print("- Easy way to correct short and 4-option tests")
print("- Enter the command code to perform each command:")
cs = ["Correction", "Create test", "Test Editor"]
lc(cs)


def lt():
    global cs
    cs = []
    file = os.listdir('psnj/')
    for i in range(len(file)):
        if os.path.isdir('psnj/' + file[i]):
            cs.append(file[i])


def ccf(f):
    global c
    t = 1
    for i in range(len(f)):
        if c.endswith("." + f[i]):
            t = 0
    if c == "" or not os.path.exists(c) or t:
        if t:
            print("- File format is not true")
        else:
            print("- Invalid file or path!")
        print("- Retry with another path or file:")
        c = input("> ")
        ccf(f)


c = int(input("> ")) - 1
cc()
print("- Welcome to " + cs[int(c)].lower() + " wizard")
if c == 0:
    print("- Please specify how you want the correction to be done:")
    cs = ["Single Correction", "Collective Correction"]
    lc(cs)
    c = (int(input("> ")) - 1)
    cc()
    print("- Please type path of that image file ( only jpg allowed ):")
    c = input("> ")
    ccf(["jpg"])
    print("- Please choose the test key:")
    oi = c
    cs = ["From saved tests", "Build new test"]
    lc(cs)
    c = (int(input("> ")) - 1)
    cc()
    if c == 0:
        print("- List tests :")
        lt()
        lc(cs)
        print("- Select By Number :")
        c = int(input("> ")) - 1
        cc()
        ry = (open("psnj/"+cs[c]+"/.tsky", "r").read()).replace('refG(','').replace(')','').split(",")
    elif c == 1:
        nt()
        print("- Continue Correction ...")
    print("- Preview:")
    ct(a(oi), ry)
    print("- Test Result : ( " + str(iouh) + " / 8 )")
    input
elif c == 1:
    nt()
