import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

print("""Welcome TO PySanj 0.1
A Great Tool For Grading the tests
ــــــــــــــــــــــــــــــــ
Creators:
1.Hamidreza Ahmadi
2.AmirHosein Alimardani
3.AmirMasoud Abedi
4.Radin Mosavi""")

class PasokhBarg():
    StudentName = "Felan Felani"
    StudentClass = 0
    Choices = []
    def __init__(self,StudentClass,StudentName,Choices:list):
        self.StudentClass = StudentClass
        self.StudentName = StudentName
        self.Choices = Choices

class Quiz():
    name = ""
    Corrects = []
    def __init__(self,name,Corrects:list):
        self.name = name
        self.Corrects = Corrects

def ChoiceRegisterer(imgpath:str):
    img = cv.imread(f'{imgpath}')
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
    print(o)
    return o


def tashih():
    pass

def addQuiz():
    Name = input("Quiz Name: ")
    try:
        file = open(f"Quizes\\{Name}.txt","x")
        Qcount:int = int(input("How Many Questions Your Quiz Is: "))
        for i in range(Qcount):
            option = int(input(f"Correct option for question number {i+1}: "))
            if option <= 4 and i+1 != Qcount:
                file.write(str(option))
                file.write("\n")
            elif option <= 4 and i+1 == Qcount:
                file.write(str(option))
            elif option > 4:
                print("option is greater than 4")
                removeQuiz(Name)
                file.close()
                break
    except FileExistsError:
        print("A Quiz With This Name Already Exists (Use \"remove\" command to delete it)")
    file.close()

def removeQuiz(Name):
    os.remove(f"Quizes\\{Name}.txt")

def listQuiz():
    for i in os.listdir("Quizes"):
        with open(f"Quizes\\{i}", 'r') as fp:
            x = len(fp.readlines())
            print(f"Quiz {i[0:-4]} : {x} questions")

def HandleCommand(Command:str):
    if Command == "add":
        addQuiz()
    elif Command == "remove":
        name = input("Quiz Name: ")
        removeQuiz(name)
    elif Command == "list":
        listQuiz()
    elif Command == "tashih":
        tashih()
    else:
        print("Command Is Not Registered")

while True:
    Command = input()
    HandleCommand(Command)