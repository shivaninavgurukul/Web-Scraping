import requests
import pprint,json
from bs4  import BeautifulSoup
with open("task_1.json","r") as re:
    scrapped=json.load(re)
def group_by_year(mov):
    years=[]
    for i in mov:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in mov:
        year=i['year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("task_2.json","w") as f:
        json.dump(movie_dict,f,indent=4)
dec_arg=group_by_year(scrapped)  
with open("task_2.json","r") as f1:
    sc=json.load(f1)
pprint.pprint(sc)          
