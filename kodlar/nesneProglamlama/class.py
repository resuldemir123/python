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
     print("init methodu çalıştı")
    #methods
    
    

#object



p1 = person("resul",2024)
p2=person("bedo",2021)

#updating
p1.name='rondon'
p2.name='b.ç'

print(f'name: {p1.name} year: {p1.year} adress: {p1.adress}')
print(f'name: {p2.name} year: {p2.year}')

print(type(p1))
print(type(p2))
print(p1)