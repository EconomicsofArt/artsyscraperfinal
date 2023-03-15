import csv , operator
import pandas as pd
import re
import numpy as np
import math
import matplotlib.pyplot as plt
#1986 to 2022
with open("Treasury.csv", 'r') as file:
    treasury = csv.reader(file, delimiter=',')
    treasuryz = []

    for col in treasury:
        treasuryz.append(col[1])
    treasuryz.remove("DGS2")
    treasuryzz = []
    for i in treasuryz:
        treasuryzz.append(float(i)/100)
   # print(len(treasuryzz))

with open("Dow.csv", 'r') as file:
    dow = csv.reader(file, delimiter=',')
    close=[]
    date=[]
    for col in dow:
        date.append(col[0])
        close.append(col[4])

    #find different years
    year_ind = 0
    year_arr = [0]
    year_inds = []
    for dates in date:
        try:
            current_year = dates[6]+dates[7]
            if year_arr[len(year_arr)-1] != current_year:
                year_arr.append(current_year)
                year_inds.append(year_ind)

            year_ind = year_ind + 1
        except:
            year_ind = year_ind + 1
    #print(year_inds)
    close1=[]
    close2=[]
    date1=[]
    date2=[]
    for i in range(len(year_inds)):
        try:
            date1.append(date[year_inds[i]])
            close1.append(close[year_inds[i]])
            date2.append(date[year_inds[i+1]-1])
            close2.append(close[year_inds[i+1]-1])
        except:
            date2.append(date[year_inds[len(year_inds)-1]])
            close2.append(close[year_inds[len(year_inds)-1]])

   # print(date1)
   # print(close1)
   # print(date2)
   # print(close2)


    realreturndow=[]
    for h in range(0,(len(close1))):
        realreturndow.append(math.log((float(close1[h])/float(close2[h])))) #december over jan
   # print(realreturndow)#from 2022 to 1986
    realreturndow.pop(0)
    #print(realreturndow)
    res = realreturndow[::-1] #reverses it from 1986 to 2022
    realreturnsdow=[]
    for r in range(0,(len(res))):
        realreturnsdow.append(res[r]-treasuryzz[r])
    #print(realreturnsdow)

with open("SP500.csv", 'r') as file:
    sp = csv.reader(file, delimiter=',')

    closea = []
    datea = []
    for col in sp:
        datea.append(col[0])
        closea.append(col[4])

    # find different years
    year_inda = 0
    year_arra = [0]
    year_indsa = []
    for datesa in datea:
        try:
            current_yeara = datesa[6] + datesa[7]
            if year_arra[len(year_arra) - 1] != current_yeara:
                year_arra.append(current_yeara)
                year_indsa.append(year_inda)

            year_inda = year_inda + 1
        except:
            year_inda = year_inda + 1
    # print(year_inds)
    closeb = []
    closec = []
    dateb = []
    datec = []
    for i in range(len(year_indsa)):
        try:
            dateb.append(datea[year_indsa[i]])
            closeb.append(closea[year_indsa[i]])
            datec.append(datea[year_indsa[i + 1] - 1])
            closec.append(closea[year_indsa[i + 1] - 1])
        except:
            datec.append(datea[year_indsa[len(year_indsa) - 1]])
            closec.append(closea[year_indsa[len(year_indsa) - 1]])

    #print(dateb)
    # print(close1)
    #print(datec)
    # print(close2)

    realreturnsp = []
    for h in range(0, (len(closeb))):
        realreturnsp.append(math.log((float(closeb[h]) / float(closec[h]))))  # december over jan
    #print(realreturnsp)#from 2022 to 1986
    realreturnsp.pop(0)
   # print(realreturnsp)
    resa = realreturnsp[::-1]  # reverses it from 1986 to 2022t
    #print(resa)
    realreturnssp = []
    for r in range(0, (len(resa))):
        realreturnssp.append(resa[r] - treasuryzz[r])
    #print(realreturnssp)

with open("AllBeta.csv", 'r') as file:
    alltype = csv.reader(file, delimiter=',')
    alltypez = []
    realreturnart=[]
    for col in alltype:
        alltypez.append(float(col[0]))
    alltypez.pop()
    for y in range(0,(len(alltypez))):
        realreturnart.append(alltypez[y]-treasuryzz[y])
#for only paintings
with open("betapaintings.csv", 'r') as file:
    alltypep = csv.reader(file, delimiter=',')
    alltypezp = []
    realreturnpaint=[]
    for col in alltypep:
        alltypezp.append(float(col[0]))
    alltypezp.pop()
    for y in range(0,(len(alltypezp))):
        realreturnpaint.append(alltypezp[y]-treasuryzz[y])
#for only sculptures
with open("betasculptures.csv", 'r') as file:
    alltypes = csv.reader(file, delimiter=',')
    alltypezs = []
    realreturnsculpt=[]
    for col in alltypes:
        alltypezs.append(float(col[0]))
   #alltypezs.pop() do not need since already to 2022
    for y in range(0,(len(alltypezs))):
        realreturnsculpt.append(alltypezs[y]-treasuryzz[y])
#print(realreturnsculpt)
#print(len(realreturnsculpt))
with open("consumerindex.csv", 'r') as file:
    consumer = csv.reader(file, delimiter=',')
    consumers = []
    try:
        for row in consumer:
            print(row)
            consumers.append(float(row[2]))
    except:
        pass

print(consumers)






#the array for real returns of dow is realreturnsdow, the real returns of sp is realreturnssp, the real returns for art is realreturnart
#now we go ahead and make the summary statisticxs
compdata = pd.DataFrame(
        {'ALlArtType': realreturnart,
         'S&P500': realreturnssp,
         'DOW': realreturnsdow,
         'Paintings': realreturnpaint,
         'Sculptures': realreturnsculpt
         }) #this makes a new pandas dataframe for the charts I want
matdata = pd.DataFrame(
        {'ALlArtType': realreturnart,
         'S&P500': realreturnssp,
         'DOW': realreturnsdow,
         'Paintings': realreturnpaint,
         'Sculptures': realreturnsculpt,
         'ConsumerIndex':consumers
         })
print(compdata.mean())
print(compdata.std())
corr_matrix=matdata.corr()
print(corr_matrix)






