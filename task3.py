  
from task_1 import*
import json
with open("task_2.json","r") as f1:
    sc=json.load(f1)
def group_by_decade(movie):
    moviedic={}
    list1=[]
    for i in movie:
        mod=int(i)%10
        decade=int(i)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    # print(list1)
    for j in list1:
        moviedic[j]=[]
    for i in moviedic:
        dec10=int(i)+9
        for x in movie:
            if int(x)<=dec10 and int(x)>=i:
                for v in movie[x]:
                    moviedic[i].append(v)
    with open("task_3.json","w") as f1:
        json.dump(moviedic,f1,indent=4)                
    return(moviedic)                
print(group_by_decade(sc))                    
        