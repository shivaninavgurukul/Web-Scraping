import requests
import pprint,json
from bs4  import BeautifulSoup

url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,'html.parser')
pprint.pprint(soup)
def scape_top_list():
    main_div = soup.find('table',class_= "table")
    name=main_div.find_all("a",class_="unstyled articleLink")
    position = main_div.find_all('td',class_="bold")
    # review=main_div.find_all("td",class_="right hidden-xs")
    rating=main_div.find_all("span",class_="tMeterIcon tiny")
    topMovie=[]
    details={'position':"",'name':"",'year':"",'rating':"",'url':""}
    def Dividename(a):
        b=a.split("(")
        return b[0]

    for i in range(0,len(position)):
        n=name[i].get_text()
        a=name[i].get_text().strip()
        r=Dividename(a)
        details['position'] = i+1
        details["name"]=r
        details['year'] = n.split()[-1][1:5]
        details['rating'] = rating[i].get_text().strip()
        details['url'] = "https://www.rottentomatoes.com"+name[i]["href"]
        topMovie.append(details.copy())
        
    # return topMovie
        pprint.pprint(details)
    with open("task_1.json","w") as read:
        json.dump(topMovie,read,indent=4)
s=scape_top_list()
print(s)

