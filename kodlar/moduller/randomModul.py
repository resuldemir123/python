import random

#result=dir(random)



result=random.random()
result=int(random.random()*100)
result=random.uniform(1,10)
result=random.randint(1,100)

greeting='hello there'
names=['resul','bedo','yusuf','miraç']
result=names[random.randint(0,len(names)-1)]

result=random.choice(greeting)


liste=list(range(10))
random.shuffle(liste)
result=liste

liste=range(100)
result=random.sample(liste,3)

print(result)