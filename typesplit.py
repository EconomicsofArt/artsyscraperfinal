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
    print(df['Type'].value_counts().to_string())

#prints, paintings, paper, sculpture
    type_mapping = {'photography':'prints', 'paintings': 'paintings','paper': 'paintings', 'sculpture':'sculpture','prints' :'prints', 'lithographpaper': 'prints', 'lithograph': 'prints', 'canvas': 'paintings', 'print': 'prints', 'papercanvas': 'paintings', 'printpaper': 'prints', 'paperpaper': 'prints'}
    df=df.assign(Type=df.Type.map(type_mapping))
    #print(df.head(50))
    df.sort_values('Titles')
    print(df['Type'].value_counts().to_string())

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
    #print(current_index)

    for i in range(0, len(current_index)-1, 2):
        Type = ""
        for k in range(current_index[i], current_index[i+1]):
            if(df.at[df.index[k], 'Type'] == 'paintings' or df.at[df.index[k], 'Type'] == 'prints'or df.at[df.index[k], 'Type'] == 'sculpture'):
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
    df = newdata.drop_duplicates()
    df2 = df.replace(r'^\s*$', np.nan, regex=True)
    df3=df2.dropna()
    #print(df3.head(50)) #right now I can print one extra from set... but i need for it to be able to loop but honestly fuck it
    #make different arrays for paintings, sculptures, prints
#first let's get the dataframes for all of the types of art
    #arrays for paintings
    ptitle=[]
    pdate=[]
    pprice=[]
    pyear=[]
    ptype=[]
    #arrays for prints
    prtitle=[]
    prdate=[]
    prprice=[]
    pryear=[]
    prtype=[]
    #arrays for sculptures
    stitle=[]
    sdate=[]
    sprice=[]
    syear=[]
    stype=[]
    i = int(0)
        # filter through for
    while i + 1 < int(len(df3)):
        if df.at[df.index[i], 'Titles'] == df.at[df.index[i + 1], 'Titles'] and df.at[df.index[i], 'Yearmade'] == df.at[ df.index[i + 1], 'Yearmade'] and df.at[df.index[i], 'Dates'] != df.at[df.index[i + 1], 'Dates']:
            if df.at[df.index[i], 'Type'] == "paintings":
                ptitle.append(df.at[df.index[i], 'Titles'])  # makes titles into an array
                pdate.append(df.at[df.index[i], 'Dates'])  # makes dates into an array
                pprice.append(df.at[df.index[i], 'Prices'])  # makes price into an array
                pyear.append(df.at[df.index[i], 'Yearmade'])
                ptype.append(df.at[df.index[i], 'Type'])  # makes dates into an array
                ptitle.append(df.at[df.index[i + 1], 'Titles'])  # makes titles into an array
                pdate.append(df.at[df.index[i + 1], 'Dates'])  # makes dates into an array
                pprice.append(df.at[df.index[i + 1], 'Prices'])  # makes price into an array
                pyear.append(df.at[df.index[i + 1], 'Yearmade'])
                ptype.append(df.at[df.index[i + 1], 'Type'])  #
            elif df.at[df.index[i], 'Type'] == "prints":
                prtitle.append(df.at[df.index[i], 'Titles'])  # makes titles into an array
                prdate.append(df.at[df.index[i], 'Dates'])  # makes dates into an array
                prprice.append(df.at[df.index[i], 'Prices'])  # makes price into an array
                pryear.append(df.at[df.index[i], 'Yearmade'])
                prtype.append(df.at[df.index[i], 'Type'])  # makes dates into an array
                prtitle.append(df.at[df.index[i + 1], 'Titles'])  # makes titles into an array
                prdate.append(df.at[df.index[i + 1], 'Dates'])  # makes dates into an array
                prprice.append(df.at[df.index[i + 1], 'Prices'])  # makes price into an array
                pryear.append(df.at[df.index[i + 1], 'Yearmade'])
                prtype.append(df.at[df.index[i + 1], 'Type'])  #
            elif df.at[df.index[i], 'Type'] == "sculpture":
                stitle.append(df.at[df.index[i], 'Titles'])  # makes titles into an array
                sdate.append(df.at[df.index[i], 'Dates'])  # makes dates into an array
                sprice.append(df.at[df.index[i], 'Prices'])  # makes price into an array
                syear.append(df.at[df.index[i], 'Yearmade'])
                stype.append(df.at[df.index[i], 'Type'])  # makes dates into an array
                stitle.append(df.at[df.index[i + 1], 'Titles'])  # makes titles into an array
                sdate.append(df.at[df.index[i + 1], 'Dates'])  # makes dates into an array
                sprice.append(df.at[df.index[i + 1], 'Prices'])  # makes price into an array
                syear.append(df.at[df.index[i + 1], 'Yearmade'])
                stype.append(df.at[df.index[i + 1], 'Type'])  #
            i = i + 1
        else:
            i = i + 1
    #making the paintings dataframe
    paintings = pd.DataFrame(
        {'Titles': ptitle,
        'Dates': pdate,
        'Prices': pprice,
        'Yearmade': pyear,
        'Type':ptype
        })
    #making the prints dataframe

    prints = pd.DataFrame(
        {'Titles': prtitle,
        'Dates': prdate,
        'Prices': prprice,
        'Yearmade': pryear,
        'Type': prtype
        })
    #making the sculpture dataframe

    sculptures= pd.DataFrame(
        {'Titles': stitle,
        'Dates': sdate,
        'Prices': sprice,
        'Yearmade': syear,
        'Type': stype
        })
    paintings=paintings.drop_duplicates()
    prints=prints.drop_duplicates()
    sculptures=sculptures.drop_duplicates()


    #print(paintings.head())
    #print(prints.head())
    #print(sculptures.head())
    paintings.to_csv('paintingrepeatedsales.csv', mode='a', index=False, header=False)
    prints.to_csv('printsrepeatedsales.csv', mode='a', index=False, header=False)
    #sculptures.to_csv('sculpturesrepeatedsales.csv', mode='a', index=False, header=False)