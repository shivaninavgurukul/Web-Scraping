import pprint
import requests
import json
from bs4  import BeautifulSoup
n=[]
def get_movie_list_details(n):
    with open("task_1.json","r")as f:
        data=json.load(f)
    for i in range(0,100):
        url=requests.get(data[i]['url'])
        b={}
            # print(url)
        data1=url.content
            # print(data)
        soup=BeautifulSoup(data1,'html.parser')
            # pprint.pprint(soup)
        title1=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column") 
        # print(title1)
        til=title1.find('div',class_="thumbnail-scoreboard-wrap")
        h1=til.find('h1',class_="scoreboard__title").get_text()
        b["title"]=h1
        movie_bio=soup.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()   
        b["bio"]=movie_bio 
        ul=soup.find('ul',class_="content-meta info")
            # print(ul)   
        li=ul.find_all('li',class_="meta-row clearfix")
        for i in li:
            b[i.find("div",class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())   
        n.append(b)
    # pprint.pprint(n)
    with open("5task.json","w") as f4:
        json.dump(n,f4,indent=4)
        # pprint.pprint(d3)   
d=get_movie_list_details([])  
with open("5task.json","r") as red:
        d2=json.load(red)   
                