#this is for photo, photography etc
import csv , operator
import pandas as pd
import re
import numpy as np
import math

with open("repeatedsales.csv", 'r') as file:
    zdata = csv.reader(file, delimiter=',')

    title = []
    date = []
    price = []
    year = []
    dim = []
    type = []

    for col in zdata:
        title.append(col[0])  # makes titles into an array
        date.append(col[1])  # makes dates into an array
        price.append(col[2])  # makes price into an array
        year.append(col[3])
        dim.append(col[4])
        type.append(col[5])

    df = pd.DataFrame(
        {'Titles': title,
         'Dates': date,
         'Prices': price,
         'Yearmade': year,
         'Dimension': dim,
         'Type': type
         })
    #print(df['Type'].value_counts().to_string())

#prints, paintings, paper, sculpture
    type_mapping = {'photography':'prints', 'paintings': ' paintings','paper': 'paintings', 'sculpture':'sculpture','prints' :'prints', 'lithographpaper': 'prints', 'lithograph': 'prints', 'canvas': 'paintings', 'print': 'prints', 'papercanvas': 'canvas', 'printpaper': 'prints', 'paperpaper': 'paper'}
    df=df.assign(Type=df.Type.map(type_mapping))
    #print(df.head(20))
    df.sort_values('Titles')

    #if the titles are the same chage NaN into the type above
    ntitle=[]
    ndate=[]
    nprice=[]
    nyear=[]
    ntype=[]
    i = int(0)
    j = int(1)

    current_index = []
    first = 1
    #loops through dataframe
    while i + 1 < int(len(df)):
        if df.at[df.index[i], 'Titles'] == df.at[df.index[i + 1], 'Titles'] and df.at[df.index[i], 'Yearmade'] == df.at[df.index[i + 1], 'Yearmade']:
            if first == 1:
                current_index.append(i)
                first = 0
        elif first == 0:
            current_index.append(i)
            first = 1
        i = i + 1
    print(current_index)

    for i in range(0, len(current_index)-1, 2):
        Type = ""
        for k in range(current_index[i], current_index[i+1]):
            if(df.at[df.index[k], 'Type'] == 'paintings' or df.at[df.index[k], 'Type'] == 'prints'or df.at[df.index[k], 'Type'] == 'sculptures'):
                Type = df.at[df.index[k], 'Type']
        for v in range(current_index[i], current_index[i + 1]):
            ntitle.append(df.at[df.index[v], 'Titles'])  # makes titles into an array
            ndate.append(df.at[df.index[v], 'Dates'])  # makes dates into an array
            nprice.append(df.at[df.index[v], 'Prices'])  # makes price into an array
            nyear.append(df.at[df.index[v], 'Yearmade'])
            ntype.append(Type)  # makes dates into an arrayntitle.append(df.at[df.index[v], 'Titles'])  # makes titles into an array
            try:
                ntitle.append(df.at[df.index[v+1], 'Titles'])  # makes titles into an array
                ndate.append(df.at[df.index[v+1], 'Dates'])  # makes dates into an array
                nprice.append(df.at[df.index[v+1], 'Prices'])  # makes price into an array
                nyear.append(df.at[df.index[v+1], 'Yearmade'])
                ntype.append(Type)  # makes dates into an array
            except:
                print("done!")

        # print(df['Titles'][i])


    newdata = pd.DataFrame(
        {'Titles': ntitle,
         'Dates': ndate,
         'Prices': nprice,
         'Yearmade': nyear,
         'Type': ntype
         })
    #print(newdata.head(20))
    df = newdata.drop_duplicates().dropna()
    print(df.head(50)) #right now I can print one extra from set... but i need for it to be able to loop but honestly fuck it