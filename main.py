import numpy
from statistics import mean
 
 
def find_min_in_pos_it(mass):
    find=101
    for i in range(len(mass)):
        if mass[i] < find and mass[i]>0:
            find = mass[i]
    if find == 101:
        print("Нет положительных")
    else:
        print("Минимальное положительное=", find)
 
def find_min_in_pos_fu(mass):
    pos=[]
    for elem in mass:
        if elem > 0:
            pos.append(elem)
    if len(pos) == 0:
        print("Нет положительных")
    else: 
        print("Минимальное положительное=", min(pos))
 
def task2_it(N, k, mass):
    sum=0
    num=0
    for dig in mass:
        if dig % k == 0:
            sum = sum + dig
            num = num + 1
    if num != 0:
        print('Cреднее арифметическое элементов массива, кратных числу k = ', sum/num)
    else:
        print('Нет чисел кратных k')
 
    max = mass[0]
    for i in range(len(mass)):
        if mass[i] > max:
            max = mass[i]
    firstmax = 0
    lastmax = 0
    i = 0
    while firstmax == 0 and i < len(mass):
        if mass[i] == max:
            firstmax = i
        i = i + 1
    for i in range(len(mass)):
        if mass[i] == max:
            lastmax = i
    if len(mass) < 3 or firstmax == lastmax:
        print('Массив состоит из менее чем 3 элементов или в массиве только 1 максимум')
    else:
        for i in range(firstmax + 1, lastmax):
            mass[i] = (-1) * mass[i]
        print('Изменились знаки некоторых элементов массива')
        print(mass)
 
    to_reverse_around = 0
    for i in range(len(mass)):
        if mass[i] < 0 and i % 2 == 0:
            to_reverse_around = i
            break
    print("Массив будет развернут вокруг:", to_reverse_around)
    mass1 = mass[0:to_reverse_around]
    mass2 = mass[to_reverse_around + 1:]
    to_reverse_around_dig = mass[to_reverse_around]
    new_mass = []
    for i in reversed(mass1):
        new_mass.append(i)
    new_mass.append(to_reverse_around_dig)
    for i in reversed(mass2):
        new_mass.append(i)
    print("Измененный массив:")
    print(new_mass)
    mass = new_mass
 
    mass[:] = [x for x in mass if x != 0]
    print("Из массива убраны удалены все нулевые элементы")
    print(mass)
 
    mass1 = mass[0:round(len(mass)/2)]
    for i in range(len(mass1)-1):
        for j in range(len(mass1)-i-1):
            if mass1[j] > mass1[j+1]:
                mass1[j], mass1[j+1] = mass1[j+1], mass1[j]
    mass1.extend(mass[round(len(mass)/2):])
    print("Измененный массив:")
    print(mass1)
 
 
def task2_fu(N, k, mass):
    mass1 = mass.copy()
    i = 0
    to_delete = []
    while i < len(mass1): 
        if mass1[i] % k != 0:
            to_delete.append(i)
        i = i + 1
    if len(mass1) == len(to_delete):
        print('Нет чисел кратных k')
    else:
        for i in reversed(to_delete):
            mass1.remove(i)
        print('Cреднее арифметическое элементов массива, кратных числу k = ', mean(mass1))   
    firstmax = mass.index(max(mass))
    lastmax = 0
    for i in range(len(mass)):
       if mass[i] == max(mass):
           lastmax = i
    #print(firstmax, lastmax)
    if len(mass) < 3 or firstmax == lastmax:
        print('Массив состоит из менее чем 3 элементов или в массиве только 1 максимум')
    else:
        for i in range(firstmax + 1, lastmax):
            mass[i] = (-1) * mass[i]
        print('Изменились знаки некоторых элементов массива')
        print(mass)
 
    to_reverse_around = 0
    for i in range(len(mass)):
        if mass[i] < 0 and i % 2 == 0:
            to_reverse_around = i
            break
    print("Массив будет развернут вокруг:", to_reverse_around)
    mass1 = mass[0:to_reverse_around]
    mass2 = mass[to_reverse_around + 1:]
    to_reverse_around_dig = mass[to_reverse_around]
    new_mass = []
    new_mass.extend(list(reversed(mass1)))
    new_mass.append(to_reverse_around_dig)
    new_mass.extend(list(reversed(mass2)))
    print("Измененный массив:")
    print(new_mass)
    mass = new_mass
 
    for i in range(len(mass)-1, -1, -1):
        if mass[i] == 0:
            mass.pop(i)
    print("Из массива убраны удалены все нулевые элементы")
    print(mass)
 
    mass1 = mass[0:round(len(mass)/2)]
    print(mass1)
    mass1.sort()
    mass1.extend(mass[round(len(mass)/2):])
    print("Измененный массив:")
    print(mass1)
 
def task1():
    task1= list(numpy.random.uniform(-100, 100, size=(3)))
    print('Массив для задания 1:')
    print(task1)
    find_min_in_pos_it(task1)
    find_min_in_pos_fu(task1)
 
def task2():
    print('Введите N')
    N=int(input())
    print('Введите k')
    k=int(input())
    s=0;
    task2 = []
    while s != N:
        d=input()
        try:
            int(d)
            task2.append(int(d))
            s = s + 1
        except ValueError:
            print("Не целое число")
    print('Массив для задания 2:')
    print(task2)
    #task2_it(N, k, task2)
    task2_fu(N, k, task2)
 
if __name__ == '__main__':
    #task1()
    task2()
