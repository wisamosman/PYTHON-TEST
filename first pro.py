class bank:
    def __init__(self,name, age):
        print(f'welcom {name}')
        self.balance = 0
    


    def withdrow(self,amount):
        self.balance -=amount
        print(f'your balance is {self.balance}')

    def mama(self,amount):
       self.balance +=amount
       print(f'your balance is :{self.balance}')




c1=bank( 'wesam',23)
c1.withdrow(200)
c1.mama(500)
