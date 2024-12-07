def cube():
    
    
    for i in range(5):
      yield i**3 # elemanlara sadece bir anlığına kulanıcaksak atarız

generator=cube()
iterator=iter(generator)

print(next(iterator))