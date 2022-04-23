import json
from task5 import d2
def analyse_movies_language (movie_list):
    list1=[]
    lang_list={}
    for i in movie_list:
        if i["Original Language:"] not in list1:
            list1.append(i["Original Language:"])
    for i in list1:
            key=i
            # print(key)
            count=0
            for j in movie_list:
                lang=j["Original Language:"]
                if str(i)==str(lang):
                    count=count+1
            lang_list.update(({key:count}))
    with open("task_6.json","w") as f:
        json.dump(lang_list,f,indent=6)
    return lang_list

            # print(list1)
analyse_movies_language(d2)