import datetime


#from datetime import datetime

result= datetime.now()
simdi=datetime.now()
result=simdi.year

result=datetime.ctime(simdi)
result=datetime.strftime(simdi,'%Y')

t='23 April 2024'
gun,ay,yil=t.split()
print(gun)
print(ay)
print(yil) #bunu yapmak eyrine şunu yapabiliriz

t='15 April 2019 hour 10:12:30'
dt=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
dt=dt.year
print(dt)

birthday=datetime(2004,2,11,12,30,10)

result=datetime.timestamp(birthday)#saniye
result=datetime.fromtimestamp(result)

result=simdi-birthday #timedelta
#result=simdi + timedelta(days=730,minutes=10)

print(result)

