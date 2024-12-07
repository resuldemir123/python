liste=[1,2,3,4]

#for i in liste: # liste aslında bir iterable obje
#    print(i)
 
iterator=iter(liste)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#while True:
#    try:
#        element=next(iterator)
#        print(element)
#    except StopIteration:
#        break


class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        
list=MyNumbers(20,50)

myiter=iter(list)

print(next(myiter))        