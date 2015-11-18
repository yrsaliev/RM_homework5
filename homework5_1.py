## -*- coding: utf-8 -*-
'''

Переделать первое домашнее задание:
Создать класс для первого задани
Классу добавить атрибуты
Вынести все функции функциями классами
Создать конструктор который будет в соответствии с параметром атрибута выполнять функцию класса

'''


class Number_checker():

    y=None

    def __init__(self,x=None):
        self.y=x
        self.check_input()

    def check_input(self):

        if 1<=self.y<4:
            self.btw_one_and_four()

        elif self.y<7:
            self.btw_four_and_seven()

        elif self.y<10:
            self.btw_seven_and_ten()
        else:
            print "Number is out of specified range... Quiting the programm..."

    def btw_one_and_four(self):
        s=raw_input("Enter a string: ")
        n=int(raw_input("Enter repetition times: "))
        for repetion in range(0,n,1):
            print s

    def btw_four_and_seven(self):
        m=int(raw_input("Enter Power degree: "))
        print x**m

    def btw_seven_and_ten(self):
        for repetition in range(x, x+10, 1):
            print repetition


while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."

number=Number_checker(x) # создает объект класса c переданным атрибутом
