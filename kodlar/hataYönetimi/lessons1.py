#error handling =>hata yönetimi

#try:
#    x=int(input('x:'))
#    y=int(input('y:'))
#    print(x/y)
    
#except ZeroDivisionError as e: #"e" neyden kaynaklandığını gösterir
#    print('y için 0 girilmez')
#    print(e)
#except ValueError as e:
#    print('x ve y için saysısal değer giriniz')
#    print(e)
    
while True:
    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)
    
    except Exception:
        print('yanlış bilgi girdiniz')
    else:
        break
    finally:
        print('try except sonlandı')

