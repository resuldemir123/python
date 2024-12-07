#class

class person:
    #pass
    #class attributes
    
    adress='no information'
    
    #constructor
    def __init__(self,name,year) :#self otomatik olarak objeleri temsil eder
        
        
    #object attributes
     self.name=name
     self.year=year
     
    #instance methods
    def intro(self): #methodslar objectlere hizmet edeceği için delf bağlantısı kurulur
        print('hello world.I am ' + self.name)
    
    def calculateAge(self):
        return 2024 - self.year

#object



p1 = person("resul",2004)
p2=person("bedo",2002)

p1.intro()
print(f'adım: {p2.name} ve yaşım:{p2.calculateAge()}')



class Circle:
    pi = 3.14
    
    def __init__(self,yaricap=1):
       self.yaricap=yaricap
       
    def cevreHesapla(self):
         return 2 * self.pi * self.yaricap
    
    
#object
c1=Circle(5)
print(f'c1 : Çevre={c1.cevreHesapla}')