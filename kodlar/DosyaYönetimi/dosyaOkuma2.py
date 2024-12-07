with open("new file.txt","r",encoding="utf-8") as file:
    content=file.read(10)
    print(content)
    file.seek(0) #cursorı en başa gönderir
    print(file.tell()) #cursorun nerde olduğunu söyler nnerden okunmaya devam edeceğini söyler
    content2=file.read()
    print(content2)