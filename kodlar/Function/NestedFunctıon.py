#def greeting(name):
#    print('hello',name)
    
#sayHello=greeting

#print(greeting)
#print(sayHello)

#del sayHello
#print(sayHello)
 
 
#def outer(num1): 
 #   def inner_increment(num1):
#        return num1+1
#    num2=inner_increment(num1)
#    print(num1,num2)
 
#outer(10)


def factoriyel(number):
    if not isinstance(number,int):
        raise TypeError("number is not integer")
    if not number >=0:
        raise ValueError("number must be zero or positive")
    
    def inner_factoriyel(number):
        if number <=1:
            return 1
        return number*inner_factoriyel(number-1)
    return inner_factoriyel(number)

try:
    print(factoriyel(-2))
except Exception as ex:
    print(ex)    

def sum(num1,num2):
    
    def inner_sum(num1,num2):
        if num1>=num2:
            return num1 + num2
        if num1 <=num2:
            return num2-num1
    result = inner_sum(num1,num2)
    print(result)

sum(20,10)    