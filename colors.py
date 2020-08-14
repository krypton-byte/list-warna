import requests
from bs4 import BeautifulSoup as m
x=requests.get('https://www.rapidtables.com/web/color/RGB_Color.html')
o=m(x.text, 'html.parser')
v=o.find_all('table',class_='dtable')[2]
data=[]
warna_json={}
for i in enumerate(v.find_all('tr')[1:]):
    print('warna : %s'%i[1].find_all('td')[1].text)
    print('RGB   : %s'%i[1].find_all('td')[3].text)
    tup=i[1].find_all('td')[3].text.replace('(','').replace(')','').split(',')
    data.append({
        'warna':[i[1].find_all('td')[1].text,(int(tup[0]),int(tup[1]),int(tup[2])), i[1].find_all('td')[2].text]
    })
open('warna.json','w').write(str(data))
print(str(data))