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


c2=bank1('samo',11)
c2.withdrow(100)
c2.azshe(1000)
c2.datail( )

        
