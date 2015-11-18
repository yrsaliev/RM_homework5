## -*- coding: utf-8 -*-
'''Переделать второе задание первого задания:
Создать класс для второго задания
Классу добавить атрибуты
Вынести все функции функциями классами
Создать конструктор который будет в соответствии с параметром атрибута выполнять функцию класса
'''

print "Society in XXI Century"

class Age_checker():

    age = None

    def __init__(self,x=None):
        self.age = x
        self.check_age()


    def check_age(self):

        if 0<self.age<7:
            print "You gotta go to children garden"

        elif self.age<18:
            print "High school"

        elif self.age<25:
            print "University"

        elif self.age<60:
            print "Work"

        elif self.age<121:
            print "Now you can live your life"

        else:
            for number in range (0,5):
                print "Error! This programm is for human only"


while True:
    try:
        x=int(raw_input("What's your age?: "))
        break
    except:
        print "It is not a number... Try again..."

my_age = Age_checker(x) #instance of class is feeded with input value