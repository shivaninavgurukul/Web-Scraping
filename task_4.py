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

    d['name']="Black panther"
    # "bio data realete to movie"
    title_div=soup.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()

    d['bio']=title_div
    title=soup.find_all('div',class_='meta-label subtle')

    sub_div=soup.find_all('div',class_='meta-value').get_text().strip()

    for i in range(len(title)):
        d[str(title[i].get_text().strip())] = sub_div[i].get_text().strip()
    movie_details.append(d)    
    # pprint.pprint(movie_details)
    with open("task_4.json","w") as f3:
        json.dump(movie_details,f3,indent=4)
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")    