class Dompitomca:

    def __init__(self, name = None, balance = None):
        self.name = name
        self.balance = balance
        self.db = []

    def getDb(self): # метод вывода БД
        for cl in self.db:
            return 'Your database:' + str(self.db)

    def addClient(self,name, balance): # метод для добавления клиента в БД
        self.name = name
        if balance.isdigit():
            self.balance = balance
            cli = {}
            cli['name'] = self.name
            cli['balance'] = self.balance
            self.db.append(cli)
            print('you added client: %s , balance: %s' % (self.name, self.balance))
        else:
            print('balance must be a number')


    def findClient(self, name): # метод поиска клиента
        print( 'serching' , name)
        for cli, value in enumerate(self.db):
            if name == value['name']:
                return value['balance']


users_db = Dompitomca() # cоздаем объект класса

while True:
    print('to add a client in the base press 1')
    print('to find a client in the base press 2')
    vibor = str(input()) # переменая для заоминания выбора пользователя

    if vibor == '1': # пункт меню 1
        name = str(input('\ninput name'))
        bal = input('input balance')
        users_db.addClient(name, bal)   # вызываем метод добпвлеия клиента в базу
        print(users_db.getDb() + '\n') # выводим созданную запись

    elif vibor == '2': # пункт меню 2
        nametofind = str(input('input name to search')) # переменая для имени введеного пользователем
        if users_db.findClient(nametofind): # вызов метода для поиска клиента
            finded_bal = users_db.findClient(nametofind)
            print('client: %s , balance: %s' % (nametofind, finded_bal))
        else:
            print('no client found')



