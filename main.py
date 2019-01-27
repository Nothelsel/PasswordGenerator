#coding:utf-8
#Software who generate some strong password
import os
from random import randrange


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Table 0
special_c = ["+", "$", "*", "ù", "%", "^", "!", "?", ";", ",", "#", "@", "ç", "-", "_", "=", "(", ")", "{", "}"]  # Table 1
ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",
         "Z"]  # Table 2
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]  # Table 3

password = ""

passwords = []

number_password = int(input("Choose numbers of passwords u want generate : "))

number_str = int(input("Choose length of password : "))


def rand_value(table):
    global password
    random_value = randrange(0, len(table))
    password = password + (table[random_value])



def generator(number_str):
    while number_str > 0:  # Tant que nombre demander par user n'a pas atteint 0
        number_str -= 1
        rand_table = randrange(0, 4)
        #print(rand_table)
        if rand_table == 0:
            table = numbers
            rand_value(table)
        elif rand_table == 1:
            table = special_c
            rand_value(table)
        elif rand_table == 2:
            table = ALPHA
            rand_value(table)
        elif rand_table == 3:
            table = alpha
            rand_value(table)


while number_password != 0:
    number_password -= 1
    generator(number_str)
    passwords.append(password)
    password = ""

print("Your passwords : ", (passwords))
