def greet():
    print('hello')
greet()

def add(x,y):
    sum_value = x + y
    return sum_value
print(add(12, 97))

def add_sub(x, y):
    sum_value  = x+y
    dif = x-y
    return sum_value, dif

add_sub(12, 5)

def student(id, name):
    print('Student ID:  ' + str(id))
    print('Student name:    ' + name + '\n')

student(id = 148, name = 'Ahilya')