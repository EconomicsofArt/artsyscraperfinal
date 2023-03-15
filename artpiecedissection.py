import csv , operator
import pandas as pd
import re
import numpy as np
import math

with open("paintingrepeatedsales.csv", 'r') as file:
    paintings = csv.reader(file, delimiter=',')
    paintingtitle = []
    paintingdate = []
    paintingprice = []
    paintingyear = []

    for col in paintings:
        paintingtitle.append(col[0])  # makes titles into an array
        paintingdate.append(col[1])  # makes dates into an array
        paintingprice.append(col[2])  # makes price into an array
        paintingyear.append(col[3])

with open("sculpturesrepeatedsales.csv", 'r') as file:
    sculptures = csv.reader(file, delimiter=',')
    sculpturetitle = []
    sculpturedate = []
    sculptureprice = []
    sculptureyear = []

    for col in sculptures:
        sculpturetitle.append(col[0])  # makes titles into an array
        sculpturedate.append(col[1])  # makes dates into an array
        sculptureprice.append(col[2])  # makes price into an array
        sculptureyear.append(col[3])
with open("printsrepeatedsales.csv", 'r') as file:
    prints = csv.reader(file, delimiter=',')
    printtitle = []
    printdate = []
    printprice = []
    printyear = []

    for col in prints:
        printtitle.append(col[0])  # makes titles into an array
        printdate.append(col[1])  # makes dates into an array
        printprice.append(col[2])  # makes price into an array
        printyear.append(col[3])

#goal is to plot each line of a piece and track over the number of years it is held
#does holding time matter for pieces return using returns of paintings and the holding time matrix
#does starting price affect the holding time and return? does the painting made date affect the price


#get the starting price from all of the above, you should have one array for each
paintingstartingprice=[paintingprice[0]]
sculpturestartingprice=[sculptureprice[0]]
printstartingprice=[printprice[0]]
i=0
while i + 1 < int(len(paintingprice)):
    if paintingtitle[i] != paintingtitle[i+1]:
        paintingstartingprice.append(paintingprice[i+1])
        i=i+1
    else:
        i=i+1
i=0
while i + 1 < int(len(sculptureprice)):
    if sculpturetitle[i] != sculpturetitle[i+1]:
        sculpturestartingprice.append(sculptureprice[i+1])
        i=i+1
    else:
        i=i+1
i=0
while i + 1 < int(len(printprice)):
    if printtitle[i] != printtitle[i+1]:
        printstartingprice.append(printprice[i+1])
        i=i+1
    else:
        i=i+1
#print(printstartingprice)

def holding_matrix(filename):
    with open(filename,'r') as file:
        holding_matrix = csv.reader(file, delimiter=',')
        output = []
        for col in holding_matrix:
            col = np.array(col).astype('int').tolist()
            #print(col)
            sum_ = np.sum(col)
            output.append(sum_)
            #print(sum_)
        #print(output)
        return output

def readcsv(filename):
    with open(filename,'r') as file:
        csv_ = csv.reader(file, delimiter=',')
        array_ = []
        for col in csv_:
            array__ = np.array(col).astype('str').tolist()
            #print(array__)
            array___ = []
            for ele in array__:
                yee = ele.replace('[', '')
                yeee = yee.replace(']', '')
                #print(yeee)
                array___.append(yeee)
            #print(array___)
            array_+=np.array(array___).astype('double').tolist()
        return array_

hold_painting = holding_matrix("holdtimematrixpaintings.csv")
hold_print = holding_matrix("holdtimematrixprints.csv")
hold_sculpture = holding_matrix("holdtimematrixsculpture.csv")
print(hold_painting)

#pull the return from everything above
paintingreturns = readcsv("returnspaintings.csv")
sculpturereturns = readcsv("returnsprints.csv")
printreturns = readcsv("returnssculpture.csv")

print(paintingreturns)


#if there is a correlation, then split things by starting price and holding time and compare with the other indexes