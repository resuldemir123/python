import json

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class Userrepostiry:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}
        
        # load users from .json file
        self.loadUser()
        
    def loadUser(self):
        if os.path.exists(('users.json')):
            with open('users.json','r',encoding='utf-8')as file:
                users=json.load(file)
                   for user in users:
                       user=json.loads(user)
                       newUser=User(username = user['username'],password = user['password'],email=user['email'])

        
    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print('Kullanıcı Oluşturuldu')
    def login(self):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn=True
                self.currentUser=user
                print('login yapıldı.')
                break 
            
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print('Çıkış yapıldı.') 
    
    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('girş yapılmadı')    
        
                
            
    def saveToFile(self):
        list=[]
        
        for users in self.users:
            list.append(json.dumps(user.__dict__))
        
        
        with open('users.json','w') as file:
            json.dump(self.users,file)
    
repostiry=Userrepostiry() 
 
    
while True:
    print('Menü'.center(50,'*') )
    secim=input('1- Register\n2-Login\n3-Logout\n4-identity\n5-Exit\n seçiminiz:  ')   
    if secim == '5':
        break
    else:
        if secim =='1':
            username = input('username:')
            password = input('password:')
            email = input('email:')
               
            user=User(username=username,password=password,email=email)
            repostiry.register(user)
            
            print(repostiry.users)
        elif secim =='2':
            username=input('username:')
            password=input('password:')
        
            repostiry.login(username,password)
        elif secim =='3':
            repostiry.logout()
        elif secim =='4':
            repostiry.identity()
        else :
            print('yanlış seçim')