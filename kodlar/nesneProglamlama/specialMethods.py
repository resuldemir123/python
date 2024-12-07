myList=[1,2,3]
myString='my string'

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))


 
 
class movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('m objesi oluşturuldu')
    def __str__(self):
        return f"{self.title} by {self.director}"
     
    def __del__(self):
       print('film silindi')  
        
m=movie('ZindanAdası','MartinScorses','filmin süresi')

print(str(m)) 

del m 

print(str(m))    