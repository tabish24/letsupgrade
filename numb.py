# import  random

# def generate_random_number(num1,num2):
#     return random.randint(num1,num2)
# def give_random_range(range_var):
#     dt ={}
#     dt [min] = -random.randint(1,range_var)
#     dt [max] = random.randint(1,range_var)
#     return dt

# def show_on_screen(c_num,dt):
#     min_number = c_num - dt.get('min')
#     max_number =c_num + dt.get('max')
#     print('hey you guess the number which is in  between ',min_number, ' and ', max_number)
# def take_user_input():
#     num = int(input("Hey Enter yor guess"))
#     return num
# def check_if_same(c_num,u_num):
#     if c_num == u_num:
#         return 10
#     else:
#         return 0
import random

def generate_random_number(num1, num2):
    return random.randint(num1, num2)

def give_random_range(range_var):
    dt = {}
    dt['min'] = random.randint(1, range_var)
    dt['max'] = random.randint(1, range_var)
    return dt

def show_on_screen(c_num, dt):
    min_number = c_num - dt.get('min')
    max_number = c_num + dt.get('max')
    print('hey you guess the number which is in between ', min_number, ' and ', max_number)

def take_user_input():
    num = int(input("Hey Enter your guess - "))
    return num

def check_if_same(c_num, u_num):
    if c_num == u_num:
        print('yay you have got it right !!!')
        return 10
    else:
        print('Sorry, you have lost, the number was',c_num)
        return 0