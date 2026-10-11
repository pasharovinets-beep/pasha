from random import *
flag='да'
def randomizer(a,b):
    return randint(a,b)
def is_valid(ip):
    return ip in s
def check(ip):
    if ip<num:
        print(f'ваше число {ip} меньше загаданного, попробуйте еще раз= ')
        return False
    elif ip>num:
        print(f'ваше число {ip} больше загаданного, попробуйте еще раз = ')
        return False
    else:
        print(f'поздравляю вы отгадали число {ip}, ваше количество попыток: {c}')
        return True
def cont(flag):
    flag=input('вы хотите сыграть? введите да или нет')
    return flag
while cont(flag) in 'да':
    c=0
    print('добро пожаловать в числовую угадайку', 'введите промежуток')
    a=int(input('левая граница='))
    b=int(input('правая граница='))
    num=randomizer(a,b)
    s=[i for i in range(a,b+1)]
    ip = int(input('попробуйте угадать число, введя его: '))
    while is_valid(ip)==False:
        ip=int(input(f'вы написали число вне промежутка, попробуйте еще раз(промежуток: от{a} до {b})= '))
        is_valid(ip)
    while check(ip)==False:
        c+=1
        ip=int(input())
