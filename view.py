import model
def input_class():
    return input('Какой класс? ').upper()

def input_class1():
    print('Нет такого класса')
    return input('Какой класс? ').upper()

def input_subject():
    sub = input('Какой предмет? ').lower()
    return sub

def input_subject1():
    print('Нет такого предмета')
    sub = input('Какой предмет? ').lower()
    return sub

def who_answer():
    search = input('Кто будет отвечать? ')
    return search

def who_answer1():
    print('Нет такого ученика')
    search = input('Кто будет отвечать? ')
    return search


def what_mark():
    markis = int(input('На какую оценку ответил? '))
    while True:
        if 1<=markis<=5:
            break
        else:
            print('Нет такой оценки')
            markis = int(input('На какую оценку ответил? '))
    return markis

def list_of_child(journal:dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

