import pprint
import requests
import json
from bs4  import BeautifulSoup
def get_movie_list_details(n):
    with open("task_1.json","r")as f:
        data=json.load(f)
    for i in range(0,100):
        url=requests.get(data[i]['url'])
            # print(url)
        data1=url.content
            # print(data)
        soup=BeautifulSoup(data1,'html.parser')
            # pprint.pprint(soup)
        title_div=soup.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()    
        ul=soup.find('ul',class_="content-meta info")
            # print(ul)   
        li=ul.find_all('li',class_="meta-row clearfix")
        d={}
        h1=soup.find('h1',class_="scoreboard__title").get_text()
        d.update({'name':h1})
        d['bio']=title_div
        for i in li:
            k=i.find('div',class_="meta-label subtle").get_text().strip()
            v=i.find('div',class_="meta-value").get_text().strip()
            d.update({k:v})    
        n.append(d)
    pprint.pprint(n)
    with open("task_5.json","w") as f4:
        json.dump(n,f4,indent=4)
        # pprint.pprint(d3)   
d=get_movie_list_details([])  
with open("task_5.json","r") as red:
        d3=json.load(red)   
                