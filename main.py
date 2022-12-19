import numpy as np
import cv2 as cv
import os
import json

print("PySanj : A Python Based Test Correction Tool")
print("Made In Codishellish")
print("Type Your Commands Here : ")
print("> 1 : New Test : To Make New Tests")
print("> 2 : Tests : A List Of Your Tests")
print("> 3 : Correction : Check Testpages")

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

def c():
    x = input("> ")
    while x == "":
        print("- Please Enter A True Command !!")
        x = input("> ")
    if x == "1":
        print("- Welcome To New Test Wizard :")
        print("- Please Type Your New Test Name :")
        y = input("> ")
        while y == "":
            print("- Please Enter Your Test Name !!")
            y = input("> ")
        print("- Now Please Type Your Test Questions File Path !")
        u = input("> ")
        while u == "" or os.path.exists(u) == False or u.endswith('.jpg') == False:
            if u == "":
                print("- File Path Must Be Filled !")
            elif os.path.exists(u) == False:
                print("- File Doesn't Exists !")
            elif u.endswith('.jpg') == False:
                print("- File Format Is Not True !!")
            else :
                print("- Unknown Error Occurred !!")
            print("- Try Another Path :")
            u = input("> ")
        print("- Now You Can Upload Answers By Two Options :")
        def j():
            print("> 1 : Upload By Json File")
            print("> 2 : Upload By Defualt Filling Exam File")
            w = input("> ")
            while w == "" or int(w) < 1 or int(w) > 2:
                if w == "":
                    print("- Input Must Be Filled !")
                elif w < 1 or w > 2:
                    print("- Function Is Not True !")
                else:
                    print("- Unknown Error Occurred !!")
                print("- Please Try With Another Option !")
                w = input("> ")
            if w == 1:
                k = "JSON"
                g = "json"
            else:
                k = "Test"
                g = "jpg"
            print("- Please Type A Path For " + k + " File")
            n = input("> ")
            while n == "" or os.path.exists(n) == False or u.endswith('.' + g) == False:
                if n == "":
                    print("- File Path Must Be Filled !")
                elif os.path.exists(n) == False:
                    print("- File Doesn't Exists !")
                elif n.endswith('.' + g) == False:
                    print("- File Format Is Not True !!")
                else:
                    print("- Unknown Error Occurred !!")
                print("- Try Another Path :")
                n = input("> ")
            print("- Answer File Preview :")
            tr = 0
            bu = ""
            for i in range (len(a(n))):
                z = 0
                b = 0
                for jsd in range(4):
                    if a(n)[i][jsd] == 1 and tr == 0:
                        z = jsd + 1
                        b += 1
                    if b > 1:
                        tr+=1
                    if tr != 0:
                        tr = i
                        print("- Unknown Error Occurred In Line " + str(tr + 1))
                        print("- Please Try Another File")
                        j()
                        break

                if tr != 0:
                    break      
                else:
                    bu += str(i + 1) + "." + str(z) + ","
                    print(str(i + 1) + "." + str(z))
            print("- Is It True ?")
            print("> 1 : True")
            print("> 2 : False")
            p = input("> ")
            while p != "1" and p != "2":
                print("- Invalid Input !")
                p = input("> ")
            
            if p == "1":
                if not os.path.exists("tfs/"):
                    os.mkdir("tfs")
                f = open("tfs/"+y+".tf","w")
                f.write(bu[:-1])

            elif p == "2":
                print("- Try Another Option !")
                j()
        j()
c()
