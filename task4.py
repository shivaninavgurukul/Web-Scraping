import requests
import pprint,json
from bs4  import BeautifulSoup
# url="https://www.rottentomatoes.com/m/black_panther_2018"
# par=requests.get(url)
# # print(par)
# soup=BeautifulSoup(par.text,'html.parser')
# # pprint.pprint(soup)
movie_details=[]
def scrape_movie_details(movie_url):
    d={}
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')

    # d['name']="Black panther"
    # "bio data realete to movie"
    title1=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column") 
        # print(title1)
    til=title1.find('div',class_="thumbnail-scoreboard-wrap")
    h1=til.find('h1',class_="scoreboard__title").get_text()
    d['name']=h1
    movie_bio=soup.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()   
    d["bio"]=movie_bio 
    ul=soup.find('ul',class_="content-meta info")
         # print(ul)   
    li=ul.find_all('li',class_="meta-row clearfix")
    for i in li:
        d[i.find("div",class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())   
        movie_details.append(d)
    # pprint.pprint(n)
    with open("4task.json","w") as f4:
        json.dump(movie_details[::14],f4,indent=4)
        # pprint.pprint(d3) 
    with open("4task.json","r") as f3:
        d=json.load(f3)  
        print(d[::14]) 
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018") 