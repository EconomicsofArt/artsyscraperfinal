import csv , operator
import pandas as pd
import re
import numpy as np
import math
import matplotlib.pyplot as plt
with open("paintingrepeatedsales.csv", 'r') as file:
    zdata = csv.reader(file, delimiter=',')

    title=[]
    date=[]
    price=[]
    year=[]

    for col in zdata:
        title.append(col[0])  # makes titles into an array
        date.append(col[1])  # makes dates into an array
        price.append(col[2])  # makes price into an array
        year.append(col[3])

#NEED TO CLEAN NEW COLUMN IN RETURN MATRIX FOR DIMENSION AND TYPE
    def removeweird(list):
        pattern = '.*\$.*|.*€.*|.*US.*|-|\(\)|\.|\+'
        list = [re.sub(pattern, '', i) for i in list]
        return list

    date = removeweird(date)
    price=removeweird(price)
    yifei = pd.DataFrame(
        {'Titles': title,
         'Dates': date,
         'Prices': price,
         'Yearmade': year
         })
    print(yifei)
    yifei['Dates'].replace('', np.nan, inplace=True)
    yifei['Prices'].replace('', np.nan, inplace=True)
    df = yifei.dropna()
   # print(df['Titles'])

    titles=df['Titles']
    dates=df['Dates']
    prices=df['Prices']
    yearmade=df['Yearmade']
    #print(prices)

    returns = []  # hold the returns and then push it to a new csv
    #holdtime = []  # holding matrix
    earliest = int(min(dates))
    latest = int(max(dates))
    index=latest-earliest
    #print(earliest)
    #print(latest)

   # testerdf=df.head(10)
   # print(testerdf)
    i = int(0)
    d=int(0)
    matrix = []
    while i + 1 < int(len(df)):
        if df.at[df.index[i],'Titles']==df.at[df.index[i+1],'Titles'] and df.at[df.index[i],'Yearmade'] ==df.at[df.index[i+1],'Yearmade']:
            returns.append(math.log((int(df.at[df.index[i+1],'Prices'])/int(df.at[df.index[i],'Prices']))))
            holdtime = list()
            smaller_date = float(df.at[df.index[i], 'Dates'])
            later_date = float(df.at[df.index[i+1], 'Dates'])

            for j in range(earliest, latest+1):
                if smaller_date <= j and j <= later_date:
                    holdtime.append(1)
                else:
                    holdtime.append(0)
            #print(holdtime)
            matrix.append(holdtime)

        i=i+1
    matrix_ = np.array(matrix)
    with open("holdtimematrixpaintings2.csv", "w", newline="") as f:
       writer = csv.writer(f)
       writer.writerows(matrix_) #this writest the matix into a csv
    with open('returnspaintings2.csv', 'w') as f:
       f.write(str(returns))

        #print(returns) this is a array of returns
    print(len(matrix_))
    print(len(returns))
#create a beta for entirety
#create separate betas
print(earliest)
print(latest)
