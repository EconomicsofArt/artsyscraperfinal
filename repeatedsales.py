import csv , operator
import pandas as pd
import re
import numpy as np

#read csv and make it names array names = .....
names = []
with open("artist_names.csv", 'r') as file:
    data = csv.reader(file, delimiter=',')
    names = sorted(data, key=operator.itemgetter(0))[0]

for name in names:
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
    #feed columns into arrays
    for col in sdata:
      title.append(col[0].lower()) #makes titles into an array
      date.append(col[3]) #makes dates into an array
      price.append(col[4]) #makes price into an array
      year.append(col[6])


    #print("Title:", title) use regrex to remove everything that is not a letter
    def removetitle(list):
      pattern = '[0-9]|,|"|\s'
      list = [re.sub(pattern, '', i) for i in list]
      return list
    title=removetitle(title)

    def removedate(list):
      pattern = '[a-zA-Z]{3}\s[0-9]{0,2},|\s|[a-zA-Z]|•|\'|&'
      list = [re.sub(pattern, '', i) for i in list]
      return list
    date=removedate(date)

    #print("date:", date) use regrex to remove everything that isn't a group of 4 digits
    def removeprice(list):
      pattern = '^.*?(?=\$)|\d+k\s[a-zA-Z]+|\$\d+,*\d+.US\$\d+,\d+\s\(est\)'
      list = [re.sub(pattern, '', i) for i in list]
      return list
    price=removeprice(price)
    def removeprice2(list):
      pattern = '\$|,'
      list = [re.sub(pattern, '', i) for i in list]
      return list
    price=removeprice2(price)
    #print("price:", price) #use regrex to remove everything that isn't

    #turn arrays into a database
    newdata = pd.DataFrame(
      {'Titles': title,
       'Dates': date,
       'Prices': price,
       'Yearmade':year
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
      ntitle.append(df.at[df.index[i+1],'Titles'])  # makes titles into an array
      ndate.append(df.at[df.index[i+1],'Dates'] )  # makes dates into an array
      nprice.append(df.at[df.index[i+1],'Prices'] )  # makes price into an array
      nyear.append(df.at[df.index[i+1],'Yearmade'])
      i=i+1
    else:
      i=i+1

  finaldata = pd.DataFrame(
      {'Titles': ntitle,
       'Dates': ndate,
       'Prices': nprice,
       'Yearmade':nyear
       })

  #print(finaldata)

  df2 = finaldata.sort_values(['Titles', 'Dates'])
  result_df = df2.drop_duplicates()
  print(result_df)
  result_df.to_csv('Repeatedsales.csv', mode='a', index=False, header=False)

