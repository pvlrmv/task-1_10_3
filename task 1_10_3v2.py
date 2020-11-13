class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def getName(self):
        return self.name
    def getBalance(self):
        return self.balance
    def getClient(self):
        return 'client: ' + self.name + ', Balance: ' + self.balance


class Dompitomca(Client):

    def __init__(self, name = None, balance = None):
        self.name = name
        self.balance = balance
        self.db = []


    def getDb(self): # метод вывода всей БД
        print('Your database:')
        for cli in self.db:
            print('client: ' + cli.getName() + ', Balance: ' + cli.getBalance())

    def addClient(self,name, balance): # метод для добавления клиента в БД
        self.name = name
        if balance.isdigit():
            self.balance = balance
            cli = Client(name, balance)

            self.db.append(cli)
            print('you added client')

        else:
            print('balance must be a number')


    def findClient(self, name): # метод поиска клиента
        print( 'serching' , name)
        for cli in self.db:
            if name == cli.getName():
                return cli.getBalance()


users_db = Dompitomca() # cоздаем объект класса

while True:
    print('to add a client in the base press 1')
    print('to find a client in the base press 2')
    vibor = str(input()) # переменая для заоминания выбора пользователя

    if vibor == '1': # пункт меню 1
        name = str(input('\ninput name'))
        bal = input('input balance')
        users_db.addClient(name, bal)   # вызываем метод добпвлеия клиента в базу
        print(users_db.getClient() + '\n') # выводим созданную запись

        #users_db.getDb()

    elif vibor == '2': # пункт меню 2
        nametofind = str(input('input name to search')) # переменая для имени введеного пользователем
        if users_db.findClient(nametofind): # вызов метода для поиска клиента
            finded_bal = users_db.findClient(nametofind)
            print('client: %s , balance: %s' % (nametofind, finded_bal))
        else:
            print('no client found')



