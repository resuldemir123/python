#inheritance:miras alma


#person => name,lastname,age,eat(),run()
#student(person),teacher(person)



class person:
    
    def __init__(self,fname,lname):
       self.fname=fname
       self.lname=lname 
       print('person created') 
       
    def who_am_i(self):
        print('I am a person')   
       
    def eat(self):
          print('I am eating')
       
class student(person):
    def __init__(self,fname,lname,number):
        person.__init__(self,fname,lname)
        self.studentNumber=number
        print('student created')
        
    #overriding    
    def who_am_i(self):
        print('I am a student')
        
        
        
class teacher(person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname) 
        self.branch=branch       

p1=person('resul','demir')
s1=student('bedo','çakar',222)

print(p1.fname + '' + p1.lname)
print(s1.fname+ ' ' + s1.lname+ ' ' +str(s1.studentNumber))

p1.eat()
s1.who_am_i()