import bs4 as bs
import datetime as ds
import requests as rq
import pandas_datareader.data as web
import pandas as pd


sauce = rq.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(sauce.text,'lxml')

table = soup.find('table')
ticker = []
j = 0
for i in table.find_all('tr')[1:]:
    j +=1
    element = i.find_all('td')[0].text
    ticker.append(element)

ticker[69] = 'BRK-B'
ticker[80] = 'BF-B'

def get_stock_data(array):
    start = ds.datetime(2017,1,1)
    end = ds.date.today()
    b = 0
    for i in array:
        b+=1
        print('%s -- %s' %(b,i))
        df = web.DataReader(i,'yahoo',start,end)
        df.to_csv('C:\Games\Stock_Data\%s.csv' % (i))
    return 0

#get_stock_data(ticker)
Main_df = pd.DataFrame

for i in ticker:
    df = pd.read_csv('C:\Games\Stock_Data\%s.csv' %(i))
    df.set_index('Date',inplace = True)
    df.drop(['Open','Close','Low','High','Volume'],1,inplace = True)
    df.rename(columns={'Adj Close':i},inplace = True)
    print (i)
    if Main_df.empty:
        Main_df = df
    else:

        Main_df = Main_df.join(df,how='outer')

Main_df.to_csv('C:\Games\Stock_Data\AAA\Main_df.csv')
