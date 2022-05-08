import os
import socket
import time

import stdiomask
from prettytable import PrettyTable
class Person:

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('enter student name:')
        self.surname = input('enter student surname:')
        self.patronymic = input('enter patr:')
        self.number = input('enter number')

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_number(self):
        return self.number

l=[]
users={}

newtable=PrettyTable()
newtable.field_names = ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"]
mytable = PrettyTable()
mytable.field_names = ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"]
myytable = PrettyTable()
myytable.field_names = ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"]
import abc

models=['Идеал',"Конкурентка","Модель","Кокетка","Конфетка"]
mmodels=['Самец',"Мужчина","Коротконос","Лавли","Чуйка"]
cmodels=['Малыш',"Юла","Мишка","Поршак","Милка"]

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
class Shoes():
    def hi(self):
        pass
class Woman_Shoes(Shoes):
    def __init__(self):
        self.size=int(input('Введите размер: '))
        self.amount=int(input("Введите количество: "))
        self.model=wom_models()
        self.sex='жен'

    def get_size(self):
        return self.size

    def get_amount(self):
        return self.amount

    def get_model(self):
        return self.model

    def get_sex(self):
        return "жен"
class Man_Shoes(Shoes):
    def __init__(self):
        self.size = int(input('Введите размер: '))
        self.amount = int(input("Введите количество: "))
        self.model=man_models()
        #self.sex='муж'
    def get_size(self):
        return self.size

    def get_amount(self):
        return self.amount

    def get_model(self):
        return self.model

    def get_sex(self):
        return 'муж'
class Child_Shoes(Shoes):
    def __init__(self):
        self.size = int(input('Введите размер: '))
        self.amount = int(input("Введите количество: "))
        self.model=ch_models()
        self.sex='дет'

    def get_size(self):
        return self.size

    def get_amount(self):
        return self.amount

    def get_model(self):
        return self.model

    def get_sex(self):
        return 'дет'
class Person:

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('Введите имя заказчика:')
        self.surname = input('Введите фамилию заказчика:')
        self.patronymic = input('Введите фамилию заказчика:')
        self.number=inputnumber()

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_number(self):
        return self.number
def add():
    while True:

        choice=input('Какой тип обуви 1.муж 2 жен 3 детский 4 выход ')
        if choice=='1':
            person = Person()
            man = Man_Shoes()
            money = man.amount*10
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
            person.name, person.surname, person.patronymic, person.number, man.size, man.amount, man.model, 'man', money))
            file.close()
            break
        elif choice=='2':

            person = Person()
            wom = Woman_Shoes()
            money=wom.amount*8
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
            person.name, person.surname, person.patronymic, person.number, wom.size, wom.amount, wom.model, 'wom', money))
            file.close()
            break
        elif choice=='3':
            person = Person()
            ch = Child_Shoes()
            money = ch.amount*6
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
            person.name, person.surname, person.patronymic, person.number, ch.size, ch.amount, ch.model, 'chl', money))
            file.close()
            break
        elif choice=='4':
            break
        else:
            print('try again')
def inputnumber():
    while True:
        number=input("Введите номер телефона:+375 ")
        if len(number)==9:
            return number
        else:
            print("Попробуйте еще раз")
def clear(): os.system('cls')
def client_mode():
    person=Person()
    clear()
    print("Добрый день "+person.name)
    while True:
        print('1.Добавление заказа')
        print('2.Просмотр заказов')
        print('3.Редактирование заказов')
        print('4.Удаление заказов')
        print('5.Сортировка заказов')
        print('6.Поиск заказов')
        print('7.Расчет суммы заказов')
        print('8.Выход')
        choice=input('Ваш выбор>>:')
        if choice=='1':
            clear()
            add_client(person)
        elif choice=='2':
            clear()
            watch_client(person)
        elif choice=='3':
            clear()
            change_client(person)
        elif choice=='4':
            clear()
            delete_client(person)
        elif choice=='5':
            clear()
            sort_client(person)
        elif choice == '6':
            clear()
            find_client(person)
        elif choice=='7':
            clear()
            total(person)
        elif choice=='8':
            clear()
            break
        else:
            print("Попробуйте еще раз")
            clear()
def sort_client(person):
    while True:
        mytable = PrettyTable(
            ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"])
        with open("tabl.txt", 'r') as file:
            for line in (line.rstrip() for line in file.readlines()):
                (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                if person.name == name and person.surname == surname and person.patronymic == patronymic:
                    mytable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

        file.close()
        choice=input('Сортировать по 1.Деньгам 2.Количеству 3.Размеру')
        if choice=='1':
            print(mytable.get_string(sortby='Деньги', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        elif choice=='2':
            print(mytable.get_string(sortby='Количество', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        elif choice=='3':
            print(mytable.get_string(sortby='Размер', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        else:
            print('try again')
def find_client(person):
    clear()
    while True:
        newtable = PrettyTable(
            ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"])
        choice = input('Поиск по 1.Полу 2.Модели 3.Размеру')
        if choice == '1':
            newsurname = input('Введите пол: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newsurname == sex and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            break
        elif choice == '2':
            newmodel = input('Введите модель: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newmodel == model and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            break
        elif choice == '3':
            newsize = input('Введите размер: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newsize == size and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            break
        else:
            print('Попробуйте еще раз ')
def see_models():
    print('Женские:')
    print(models)
    print("Мужские:")
    print(mmodels)
    print("Детские")
    print(cmodels)
def metod_ranga():
    #Исследованеи и подсчет стоимости всего товара
    #Расчет стоимости мы возьмем на соновании экспертного мнения 3 маркетологов и их оценок для подсчета стоимости
    #и 3 видов обувной продукции(муж жен и дет) то у нас получиться матрица 3 на 3 где каждый эксперт дает оценку
    Z = [[10, 14, 24],
         [16, 18, 24],
         [7, 12, 20]]
    z = []
    # посчитаем матрицу нормированных оценок
    z = [[i / 3 for i in row] for row in Z]
    print(z)
    # Находим веса целей
    w_1 = (z[0][0] + z[1][0] + z[2][0]) / 3
    print(w_1)
    w_2 = (z[0][1] + z[1][1] + z[2][1]) / 3
    print(w_2)
    w_3 = (z[0][2] + z[1][2] + z[2][2]) / 3
    print(w_3)
    print("best alternative-3")
    time.sleep(2)
    # Лучшая ставка+налог=8 ждя женщин
def total(person):
    watch_client(person)
    k=[]
    sum=0
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                k.append(money)
    array = [int(numeric_string) for numeric_string in k]
    for elem in array:
        sum+=elem

    print("|Итого:")
    print(sum)
def wom_models():
    while True:
        models=['Идеал',"Конкурентка","Модель","Кокетка","Конфетка"]
        ans=int(input("Женские модели:Идеал,Конкурентка,Модель,Кокетка,Конфетка"))
        if ans==1:
            return "Идеал"
        elif ans==2:
            return "Конкурентка"
        elif ans==3:
            return "Модель"
        elif ans==4:
            return "Кокетка"
        elif ans==5:
            return "Конкурентка"
        else:
            print('Попробуйте еще раз')
def man_models():
    while True:
        mmodels=['Самец',"Мужчина","Коротконос","Лавли","Чуйка"]
        ans=input("Женские модели:Самец,Мужчина,Коротконос,Лавли,Чуйка")
        if ans=='1':
            return "Самец"
        elif ans=='2':
            return "Мужчина"
        elif ans=='3':
            return "Коротконос"
        elif ans=='4':
            return "Лавли"
        elif ans=='5':
            return "Чуйка"
        else:
            print('Попробуйте еще раз')
def ch_models():
    while True:
        cmodels=['Малыш',"Юла","Мишка","Поршак","Милка"]
        ans=input("Женские модели:Малыш,Юла,Мишка,Поршак,Милка")
        if ans=='1':
            return "Малыш"
        elif ans=='2':
            return "Юла"
        elif ans=='3':
            return "Мишка"
        elif ans=='4':
            return "Поршак"
        elif ans=='5':
            return "Милка"
        else:
            print('Попробуйте еще раз')
def change_client(person):

    l = []
    d=[]
    l.clear()
    d.clear()
    print(l)

    watch_client(person)
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, size, amount, model, sex,money) = line.split(' ')
            if person.name!=name and person.surname!=surname and person.patronymic!=patronymic:
                myline = line.split(' ')
                d.append(myline)
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, size, amount, model, sex,money) = line.split(' ')
            if person.name==name and person.surname==surname and person.patronymic==patronymic:
                myline = line.split(' ')
                l.append(myline)
    print(l)
    index = int(input('Введите какой заказ изменить: '))
    del l[index - 1]
    f = open('tabl.txt', 'w')
    f.close()
    with open('tabl.txt', 'w') as x:
        for sub_list in l:
            for item in sub_list:

                x.write(item + ' ')
            x.write('\n')
    with open('tabl.txt', 'a') as x:
        for sub_list in d:
            for item in sub_list:

                x.write(item + ' ')
            x.write('\n')
    l.clear()
    d.clear()
    add_client(person)
def watch_client(person):
    myytable.clear_rows()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                myytable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

    file.close()
    print(myytable)
    myytable.clear_rows()
def delete_client(person):
    while True:
        watch_client(person)
        choice=input('1.Удалить все 2.Удалить одну запись')
        if choice=='1':
            l = []
            d=[]
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)

            with open('tabl.txt', 'w') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            break
        elif choice=="2":

            l = []
            l.clear()
            d = []
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if person.name == name and person.surname == surname and person.patronymic == patronymic:
                        myline = line.split(' ')
                        l.append(myline)
            index = int(input('Какой заказ удалить?: '))
            del l[index - 1]
            f = open('tabl.txt', 'w')
            f.close()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            with open('tabl.txt', 'a') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            watch_client(person)
            break
def add_client(person):
    while True:
        choice = input('Какой тип обуви 1.Мужской 2.Женский 3.Детский 4.Выход ')
        if choice == '1':
            man = Man_Shoes()
            money = man.amount * 10.0
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
                person.name, person.surname, person.patronymic, person.number, man.size, man.amount, man.model, 'Мужская',
                money))
            file.close()
            break
        elif choice == '2':
            wom = Woman_Shoes()
            money = wom.amount * 8.0
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
                person.name, person.surname, person.patronymic, person.number, wom.size, wom.amount, wom.model, 'Женская',
                money))
            file.close()
            break
        elif choice == '3':
            ch = Child_Shoes()
            money = ch.amount * 6.0
            file = open('tabl.txt', 'a')
            file.write('%s %s %s %s %d %d %s %s %d\n' % (
                person.name, person.surname, person.patronymic, person.number, ch.size, ch.amount, ch.model, 'Детская', money))
            file.close()
            break
        elif choice == '4':
            break
        else:
            print('Попробуйте еще раз')
def admin_mode():
    clear()
    while True:
        clear()
        print("1.Добавление записи\n")
        print("2.Просмотр записи\n")
        print("3.Редактирование записи\n")
        print("4.Удаление записи\n")
        print("5.Работа с пользователями\n")
        print("6.Поиск записи\n")
        print("7.Сортировка записи\n")
        print("8.Выход\n")
        choice_3=input("Выберите действие: ")
        if choice_3=='1':
            add()
        elif choice_3=='2':
            watch()
        elif choice_3=='3':
            change()
        elif choice_3=='4':
            delete()
        elif choice_3=='5':
            work()
        elif choice_3=='6':
            find()
        elif choice_3=='7':
            sort()
        elif choice_3=='8':
            break
        else:
            print('try again')
def find():
    clear()

    while True:
        newtable = PrettyTable(["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"])
        choice = input('Поиск по 1.Фамилии 2.Модели 3.Размеру')
        if choice == '1':
            newsurname=input('Введите фамилию: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newsurname==surname:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            newtable.clear_rows()
            time.sleep(3)
            clear()
            break
        elif choice == '2':
            newmodel = input('Введите модель: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newmodel == model:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            newtable.clear_rows()
            time.sleep(3)
            clear()
            break
        elif choice == '3':
            newsize = input('Введите размер: ')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                    if newsize == size:
                        newtable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

            file.close()
            print(newtable)
            newtable.clear_rows()
            time.sleep(3)
            clear()
            break
        else:
            print('try again')
def watch():
    clear()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
            myytable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

    file.close()
    print(myytable)
    time.sleep(3)
    myytable.clear_rows()
def delete():
    clear()
    while True:
        choice=input('1.delete all 2 one')
        if choice=='1':
            grid = 9
            l = []
            watch()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            l.clear()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')


            break
        elif choice=='2':
            grid = 9
            l = []
            watch()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)

            index=int(input('enter what column to delete: '))
            l.pop(index-1)
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')

            l.clear()
            watch()
            break
        else:
            print('try again')
def change():
    clear()
    while True:
        grid = 9
        l = []
        watch()
        with open("tabl.txt", 'r') as f:
            for line in (line.rstrip() for line in f.readlines()):
                myline = line.split(' ')
                l.append(myline)

        index = int(input('enter what column to change: '))
        l.pop(index - 1)
        with open('tabl.txt', 'w') as x:
            for sub_list in l:
                for item in sub_list:
                    x.write(item + ' ')
                x.write('\n')

        l.clear()
        add()
        watch()
        break
def sort():
    while True:
        mytable = PrettyTable(
            ["Имя", "Фамилия", "Отчество", "Номер", "Размер", "Количество", "Модель", "Пол", "Деньги"])
        with open("tabl.txt", 'r') as file:
            for line in (line.rstrip() for line in file.readlines()):
                (name, surname, patronymic, number, size, amount, model, sex, money) = line.split(' ')
                mytable.add_row([name, surname, patronymic, number, size, amount, model, sex, money])

        file.close()
        choice=input('Сортировать по 1.Деньгам 2.Количеству 3.Размеру')
        if choice=='1':
            print(mytable.get_string(sortby='Деньги', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        elif choice=='2':
            print(mytable.get_string(sortby='Количество', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        elif choice=='3':
            print(mytable.get_string(sortby='Размер', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            mytable.clear_rows()
            clear()
            break
        else:
            print('try again')
def authorization():
    while True:
        clear()
        login=input('Введите логин:')

        pas=stdiomask.getpass("Введите пароль: ")
        if login=='admin' and pas=="admin":
            admin_mode()
            break
        else:
            #users = {}
            with open("users.txt",'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (key, value) = line.split(' ')
                    if login==key and pas==value:
                        clear()
                        client_mode()
                        break

        if EOFError:
            break
def registration():
    clear()
    key = input('Введите логин ')
    value = stdiomask.getpass("Введите пароль ")
    users[key] = value
    while True:
       if len(key)>5 and len(value)>5:
            file = open("users.txt", "a")
            file.write('%s %s\n' % (key, value))
            file.close()
            break
       else:
           break
def enter():

    while True:
        clear()
        answer=input('1.Регистрация\n2.Вход\n3.Выход\n')
        if answer=='1':
            registration()
        elif answer=='2':
            authorization()
        elif answer=='3':
            break
        else:
            print("Неверно.Попробуйте еще раз: ")
def work():
    with open("users.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (key, value) = line.split(' ')

            users[key] = value
    while True:
        choice=input('1.Удаление 2.Добавление 3.Выход')
        if choice=='1':
            grid = 9
            l = []

            with open("users.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            print(l)
            index = int(input('Какого пользователя удалить? '))
            del l[index-1]
            file=open('users.txt', 'w')
            file.close()
            with open('users.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item)
                        x.write(" ")
                    x.write('\n')

            l.clear()

            break
        elif choice=='2':
            registration()
            break
        elif choice=='3':
            break
        else:
            print('Попробуйте еще раз')
def Main():
    while True:
        Input = input('Do you want to enter?yes or no ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        Response=Response.decode('utf-8')
        if Response=='im ready':
            enter()
            break
        else:
            print('bye')
            break


    ClientSocket.close()
if __name__ == '__main__':
    Main()


