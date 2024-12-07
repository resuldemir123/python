import re #arama kriterlerini seçmemizi sağlar

result=dir(re)

#regular expression
result=re.findall("[abc]",str)
result=re.findall("[sat]",str)
result=re.findall("[a-e]",str)
result=re.findall("[^abc]",str) #abc dışındaki tüm karakterleri arar

result=re.findall("...",str)

"""
  ^ - belirtilen karakterle başlıyor mu?
  ^ => a: 1 match
       abc: 1 match
       bac: no match
"""
result=re.findall("^P",str)

"""
  $ - belirtilen karakterle bitiyor mu?
  a$ => lamba : 1 match
        Ptyhon: no match
"""
result=re.findall("$t",str)

"""
 * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder
  ma*n => man : 1 match
          main: no match(a'nın arkasına n gelmiyor)
"""
result=re.findall("sa*t",str)

"""
   + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder
  ma+n => man : 1 match
          main: no match(a'nın arkasına n gelmiyor)
"""
result=re.findall("sa+t",str)

"""
   ? - Bir karakterin bir ya da bir kez olmasını kontrol eder
  ma?n => man : 1 match
          main: no match(a'nın arkasına n gelmiyor)
"""
result=re.findall("sa?t",str)

"""
  {} - Karakter sayısını kontrol eder
     al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlanmalı
     [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
  
"""
result=re.findall("a{2,3}",str)

"""
  | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
   a|b => a ya da b
      cde => no match
      acdbea => 3 match
"""
result=re.findall("a|b",str)

"""
   () - gruplamak için kullanılır
      (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir
"""
result=re.findall("(a|b|c)xz",str)

"""
   \ - Özel karakterleri aramamızı sağlar
      \$a =>$ karakterinin arkasına a karakterini arar
   
   \A - Belirtilen karakter stringin sonunda mı?
      \Athe => the stringin başında mı?
   \Z - Belirtilen karakter stringin sonunda mı?
       the\Z => the stringin sonunda mı?   

"""

#re module
str="Python Kursu: Python Proglamlama Rehberiniz | 40 saat"

# result=re.findall("Python",str)


#result=re.split(" ",str)

# result=re.sub(" ","/",str)

#result=re.search("Python",str)
#result=re.span() #bize kelimenin nerede olduğunu verir
#result=re.group() #bize aradığımız şeyi getirir
#result=re.string() #bize hangi cümle içinde aradığımızı verir


print(result)