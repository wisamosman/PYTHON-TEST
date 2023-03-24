class bank:
    def __init__(self,name, age):
        print(f'welcom {name}')
        self.balance = 0
        self.name=name
        self.age=age
    


    def withdrow(self,amount):
        self.balance -=amount
        print(f'your balance is {self.balance}')

    def mama(self,amount):
       self.balance +=amount
       print(f'your balance is :{self.balance}')


    def detailes(self):
       print(f'name : {self.name}')
       print(f'age : {self.age}')

    def  Balance(self):
        print(f'your balance is : {self.balance}')

c1=bank( 'wesam', 23)
c1.withdrow(200)
c1.detailes( )
c1.mama(500)
c1.Balance( )























class bank1:
    def __init__(self,name,age):
        print(f'welcom {name}')
        self.balance=0
        self.name=name
        self.age=age
        

    def withdrow(self,accounter):
       self.balance -=accounter
       print(f'your balance is : {self.balance}')
       

    def azshe(self,accounter):
        self.balance +=accounter
        print(f'your balance is : {self.balance}')

    def datail(self):
        print(f'your name is : {self.name}')
        print(f'you rage is : {self.age}')

    def nalance(self):
        print(f'your balance is : {self.balance}')


c2=bank1('samo',11)
c2.withdrow(100)
c2.azshe(1000)
c2.datail( )
c2.nalance( )









class ser:
    def __init__(self,name,age):
        print(f'welcom {name}')
        self.balance = 0
        self.name=name
        self.age=age
        
        
    def withdrow(self,accounto):
        self.balance -=accounto
        print(f'your balance is : {self.balance}')
       
    def einzahlen(self,account):
        self.balance +=account
        print(f'your balance is :{self.balance}')
       
    def datuil(self):
        print(f'your name is :{self.name}')
        print(f'your age is :{self.age}')


    def balanci(self):
        print(f'your balance is :{self.balance}')

c3=ser('omer',44)
c3.withdrow(300)
c3.einzahlen(800)
c3.datuil( )
c3.balanci( )








class aha:
    def __init__(self,name,age):
        print(f'welcom {name}')
        self.balance =0
        self.name=name
        self.age =age
        

    def acountero(self,account):
        self.balance -=account
        print(f'{self.balance}')

    def ein(self,einzahlen):
        self.balance +=einzahlen
        print(f'{self.balance}')

    def anta(self):
        print(f'{self.name}')
        print(f'{self.age}')

    def antai(self):
        print(f'your balance is : {self.balance}')

        
c4=aha('nesro',19)
c4.acountero(100)
c4.ein(400)
c4.anta( )
c4.antai( )


for x in range (1,19):
    if x==10:
        break
    print(x)

    
for y in range (20,30):
    if y==25:
        continue
    print(y)
q=0
while q<10:
    print(q)
    q +=1
    if q==3:
        break
    
