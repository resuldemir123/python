def usalma(number):
    def inner(power):
        return number**power
    return inner


def yetkiSorgula(page):
    def inner(role):
        if role=='admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,format)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role,format)
    return inner
        
user1=yetkiSorgula("product edit")
print(user1("admin"))


def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpım=1
        for i in args:
            carpım*=i
        return carpım
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma
    
toplama=islem("toplama")
print(toplama (1,3,5,6))