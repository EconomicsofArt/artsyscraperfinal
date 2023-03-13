import csv , operator
import pandas as pd
import re
import numpy as np


def removetitle(list):
  pattern = '[0-9]|,|"|\s'
  list = [re.sub(pattern, '', i) for i in list]
  return list

def removedate(list):
  pattern = '[a-zA-Z]{3}\s[0-9]{0,2},|\s|[a-zA-Z]|•|\'|&'
  list = [re.sub(pattern, '', i) for i in list]
  return list

# print("date:", date) use regrex to remove everything that isn't a group of 4 digits
def removeprice(list):
  pattern = '^.*?(?=\$)|\d+k\s[a-zA-Z]+|\$\d+,*\d+.US\$\d+,\d+\s\(est\)'
  list = [re.sub(pattern, '', i) for i in list]
  return list

def removeprice2(list):
  pattern = '\$|,'
  list = [re.sub(pattern, '', i) for i in list]
  return list
def removedim(list):
  pattern = '[(.+).+]'
  list = [re.sub(pattern, '', i) for i in list]
  return list

def removesoup(list):
    pattern='\\b(?!(?:photo|photography|photograph|print|prints|lithograph|painting|paintings|canvas|paper|sculpture|sculptures)\\b)[a-zA-Z]+\\b' #[photoprint|prints|lithograph|oil|painting|paintings|canvas|acrylic|paper|sculpture|sculptures]
    patternn = '-*,*/*\'*\"*:*;*&*<*>*#*'
    patternnn = '[(.*)]'
    patternnnn='\s*'
    patternnnnn='\d*'
    list = [re.sub(pattern, '', i) for i in list]
    listt = [re.sub(patternn, '', i) for i in list]
    listtt = [re.sub(patternnn, '', i) for i in listt]
    listttt = [re.sub(patternnnn, '', i) for i in listtt]
    listtttt = [re.sub(patternnnnn, '', i) for i in listttt]
    return listtttt

#read csv and make it names array names = .....
names = []
with open("artist_names_repeated_sales.csv", 'r') as file:
    data = csv.reader(file, delimiter=',')
    names = sorted(data, key=operator.itemgetter(0))[0]

for name in names: #maketrycatch
  try:
    with open(name+".csv", 'r') as file:
      data = csv.reader(file, delimiter=',')
      #sort data on the basis of title
      sdata = sorted(data, key=operator.itemgetter(0))

      #print(sdata)
      #create empty lists to transform columns in
      title=[]
      date=[]
      price=[]
      year=[]
      soup = []
      dim = []



      #feed columns into arrays
      for col in sdata:
        title.append(col[0].lower()) #makes titles into an array
        date.append(col[3]) #makes dates into an array
        price.append(col[4]) #makes price into an array
        year.append(col[6])
        soup.append(col[1].lower())
        dim.append(col[2])

      #print("Title:", title) use regrex to remove everything that is not a letter

      title=removetitle(title)
      date=removedate(date)
      price=removeprice(price)
      price=removeprice2(price)
      dim = removedim(dim)
      soup = removesoup(soup)
      #print("price:", price) #use regrex to remove everything that isn't

      #turn arrays into a database
      newdata = pd.DataFrame(
        {'Titles': title,
         'Dates': date,
         'Prices': price,
         'Yearmade':year,
         'Dimension':dim,
         'Type':soup
         })
      #print(newdata)
    #replace any empty cells with na in python
    newdata['Titles'].replace('', np.nan, inplace=True)
    newdata['Dates'].replace('', np.nan, inplace=True)
    newdata['Prices'].replace('', np.nan, inplace=True)
    newdata['Yearmade'].replace('', np.nan, inplace=True)

    #drop all of the na
    df = newdata.dropna()
    #print(df['Titles'])
    #print(df['Titles'][0])


    #define variables


    #Make new empty arrays
    ntitle = []
    ndate = []
    nprice = []
    nyear = []
    ndim = []
    ntype = []


    i=int(0)
    j=int(1)
    #print(df['Titles'][1])
    #print(df['Titles'][0])
    #print(df['Titles'][i])
    #print(df.at[df.index[1],'Titles'])

    #filter through for
    while i+1 < int(len(df)):
      #print(df['Titles'][i])
      if df.at[df.index[i],'Titles']==df.at[df.index[i+1],'Titles'] and df.at[df.index[i],'Yearmade'] ==df.at[df.index[i+1],'Yearmade'] and df.at[df.index[i],'Dates'] !=df.at[df.index[i+1],'Dates']:
        ntitle.append(df.at[df.index[i],'Titles'])  # makes titles into an array
        ndate.append(df.at[df.index[i],'Dates'])  # makes dates into an array
        nprice.append(df.at[df.index[i],'Prices'])  # makes price into an array
        nyear.append(df.at[df.index[i],'Yearmade'])
        ndim.append(df.at[df.index[i], 'Dimension'])  # makes titles into an array
        ntype.append(df.at[df.index[i], 'Type'])  # makes dates into an array
        ntitle.append(df.at[df.index[i+1],'Titles'])  # makes titles into an array
        ndate.append(df.at[df.index[i+1],'Dates'] )  # makes dates into an array
        nprice.append(df.at[df.index[i+1],'Prices'] )  # makes price into an array
        nyear.append(df.at[df.index[i+1],'Yearmade'])
        ndim.append(df.at[df.index[i+1], 'Dimension'])  # makes titles into an array
        ntype.append(df.at[df.index[i+1], 'Type'])  #
        i=i+1
      else:
        i=i+1

    #print(finaldata)

    df2 = finaldata.sort_values(['Titles', 'Dates'])
    result_df = df2.drop_duplicates()
    print(result_df)
    result_df.to_csv('Repeatedsales.csv', mode='a', index=False, header=False)
  except:
    print(name+" has no csv")
