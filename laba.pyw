import random
import copy
import time
import datetime
import numpy as np

while 1:
    try:
        u = input("Введите, как вы хотите ввести массив (вручную или рандомно): ")

        if (u=='вручную'):
            n = int(input("Введите размер массива: "))
            #Заполнение массива вручную и вывод элементов
            while 1:
                try:
                    print("Введите элементы массива:")
                    array = [float(input()) for x in range(n)]
                    print("Элементы массива:")
                    print(array)
                    break
        elif (u=='рандомно'):
            #Заполнение массива рандомно и вывод элементов
            while 1:
                try:
                    h = int(input("Введите размер массива(10000, 30000, 50000, 70000, 90000): "))
                    if (h==10000):
                            np.array([random.random() for x in range(10000)])
                            print("Элементы массива:")
                            print(array)
                            break
                    elif (h==30000):
                            np.array([random.random() for x in range(30000)])
                            print("Элементы массива:")
                            print(array)
                            break
                    elif (h==50000):
                            np.array([random.random() for x in range(50000)])
                            print("Элементы массива:")
                            print(array)
                            break
                    elif (h==70000):
                            np.array([random.random() for x in range(70000)])
                            print("Элементы массива:")
                            print(array)
                            break
                    elif (h==90000):
                            np.array([random.random() for x in range(90000)])
                            print("Элементы массива:")
                            print(array)
                            break
        else:
            print("Нет такой сортировки. Попробуйте снова.")
                        
    except ValueError:
        print("Вы ошиблись. Попробуйте ввести снова.")

#Подсчет времени выполнения 
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print "Время выполнения: {:.3f} sec".format(time.time() - self._startTime)

        
#Быстрая сортировка
def qsort(array):
    if array:
        return qsort([x for x in L if x<array[0]]) + [x for x in L if x==array[0]] + qsort([x for x in L if x>array[0]])
    return []

#Сортировка пузырьком
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
    return array

#Сортировка вставками
def insertion_sort(array):
        for i in range(1, len(array)):
            while i > 0 and array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                    i -= 1
#Сортировка деревом
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def set_value(self, val):
        self.key = val

class Tree:
    def __init__(self):
        self.root = None

    def add_key(self, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val < current.key:
                if current.left == None:
                    current.left = Node(val, None, None)
                    break
                current = current.left
            elif val > current.key:
                if current.right == None:
                    current.right = Node(val, None, None)
                    break
                current = current.right
            else:
                break

    def insert(self, val):
        self.add_key(val)

    def inorder_(self):
        if self.root == None:
            return None
    stack = []
    node = self.root
     while node or stack:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.key , end=" ")
            node = node.right

    def inorder(self):
        self.inorder_()

    def find_(self, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                if  current.key == val:
                    print(current.key)
                    break
                elif current.left == None and current.key != val:
                print("No Value")
                current = current.left
            elif val > current.key:
                if current.key == val:
                    print(current.key)
                    break
                elif current.right == None and current.key != val:
                    print("No Value")
                current = current.right

    def find(self, val):
            self.find_(val)

def SortTree(array):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
            break
        t.insert((i))
    t.inorder()

def FTree(array, val):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        tac = time.time()
        t.find((val))
        tic = time.time()
    return tic-tac

#Линейный поиск
def min1(array):
    sortArr = []
    for y in range(len(array)):
        if (int(array[y][0]) >= 832963409 and int(array[y][0]) <= 1180032209):
            sortArr.append(array[y][1])
    min2 = sortArr[0]
    for arg in sortArr[1:]:
        if arg < min2:
            min1 = arg
    print('Минимальное значение = ' + str(min2))

    max2 = []
    for arg in sortArr[1:]:
        if arg > min2:
            max2 = arg
    print('Максимальное значение = ' + str(max2))

#Бинарный поиск 
def interpolationSearch(a, key):
    print('Бинарный поиск')
    sortArr = []
    for y in range(len(a)):
        if (int(a[y][0]) >= 832963409 and int(a[y][0]) <= 1180032209):
            sortArr.append(a[y][1])


    left = 0  
    right = len(sortArr) - 1  

    while sortArr[left] < key and key < sortArr[right]:
        mid = left + (key - sortArr[left]) * (right - left) / (sortArr[right] - sortArr[left])
        mid = int(mid)
        if sortArr[mid] < key:
            left = mid + 1
        else:
            if sortArr[mid] > key:
                right = mid - 1
            else:
                print('Индекс = ' + str(mid))
                return mid
    if sortArr[left] == key:
        print('Индекс = ' + str(left))
        return left
    else:
        if sortArr[right] == key:
            print("Индекс = " + str(right))
            return right
        else:
            print('При бинарным поиске значение не найдено')
            return -1




while 1:
    try:
        u = input("Введите название сортировки (быстрая сортировка, сортировка пузырьком, сортировка вставками, сортировка деревом): ")

        #Быстрая сортировка и подсчет времени
        if (u=='быстрая сортировка'):
            with Profiler() as p:
                array = qsort(array)
            print(array)
            #Поиск минимума и максимума в заданных случаях линейным поиском
            arrayMinAndMax = []
            with Profiler() as p:
                arrayMinAndMax = min(array)

            break
        
        #Сортировка пузырьком и подсчет времени   
        elif (u=='сортировка пузырьком'):
           with Profiler() as p:
                bubble_sort(array)
            print(array)
            break

        #Сортировка вставками и подсчет времени
        elif (u=='сортировка вставками'):
            with Profiler() as p:
                insertion_sort(array)
            print(array)
            break

        #Сортировка деревом и подсчет времени
        elif (u=='сортировка деревом'):
            with Profiler() as p:
                array = SortTree(array)
            print(array)
                csvArr = [random.randint(0, 100000000) for i in range(400000)]
    key =csvArr[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr, key)
print('Time = ' + str(tf))
            break

        else:
            print("Нет такой сортировки. Попробуйте снова.")
    except ValueError:
        print("Нет такой сортировки. Попробуйте снова.")




