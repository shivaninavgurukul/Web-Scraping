import json
from textwrap import indent
from task5 import d2
def analyse_movies_language1(movie_list):
    li1=[]
    lang_list={}
    for i in movie_list:
        if i["Director:"] not in li1:
            li1.append(i["Director:"])
    for i in li1:
            key=i
            # print(key)
            count=0
            for j in movie_list:
                lang=j["Director:"]
                if str(i)==str(lang):
                    count=count+1
            lang_list.update(({key:count}))
    with open("task_7.json","w") as f:
        json.dump(lang_list,f,indent=6)
    # return lang_list
    # print(lang_list)

            # print(list1)
# analyse_movies_language1(d2)
    with open("task_7.json","r") as d:
        z=json.load(lang_list,d,indent=4)
        print(z)
analyse_movies_language1(d2)    