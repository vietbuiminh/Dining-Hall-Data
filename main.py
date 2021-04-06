import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup

url='https://www.augustana.net/csldining/public/view_student.php'

r = requests.get(url)
datahtml = BeautifulSoup(r.content, 'html5lib')
#print(datahtml.prettify())

data = []

todayData = datahtml.find('div', attrs = {'id':['today']})

# title and date
title = todayData.find('h2').get_text().strip()
title = title.split(" | ")
date = title[1].strip()
data.append({'date':date})

#print(date)

# Table section
table = todayData.find('table', attrs = {'id':['datatable']})
for line in table.findAll('tr'):
  tableData = {}
  print(line)

  #print(line.get_text())

df=pd.DataFrame(data)
print(df)
df.to_csv('./output.csv', index=False)