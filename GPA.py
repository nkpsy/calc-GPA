import numpy as np


def GPA():
    fileName = input('Please enter a transcript belonging desktop:')
    fin = open('C:\\Users\\psy16\\Desktop\\' + fileName + '.csv','r')

    abcSum = 0
    dSum = 0
    eSum = 0

    abcCre = 0
    dCre = 0
    eCre = 0

    line = fin.readline()

    while line:
        data = line.rstrip().split(',')
        if (data[0] == 'A') or (data[0] == 'B') or (data[0] == 'C'):
            abcSum+=(np.float(data[1])) * (np.float(data[2]))
            abcCre+=(np.float(data[2]))
        elif data[0] == 'D':
            dSum+=(np.float(data[1])) * (np.float(data[2]))
            dCre+=(np.float(data[2]))
        elif data[0] == 'E':
            eSum+=(np.float(data[1])) * (np.float(data[2]))
            eCre+=(np.float(data[2]))
        line = fin.readline()

    fin.close()

    abcGPA = abcSum / abcCre
    abcdGPA = (abcSum + dSum) / (abcCre + dCre)
    abcdeGPA = (abcSum + dSum + eSum) / (abcCre + dCre + eCre)

    print(abcCre)
    print(abcCre + dCre)
    print(abcCre + dCre + eCre)
    print('abcGPA=' + str(abcGPA))
    print('abcdGPA=' + str(abcdGPA))
    print('abcdeGPA=' + str(abcdeGPA))