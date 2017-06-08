import random
import copy
import time
import datetime

#Подсчет времени выполнения сортировки или поиска
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
    def __exit__(self, type, value, traceback):
        print("Время: %.3f" % format(time.time() - self._startTime))

#Быстрая сортировка Хоара
def QuickSort(A, left, right):
    global Cq, Mq
    indexLow  = left + 1 # Нижний и текущий индексы                        
    indexHigh = right - 1    
    pivotPoint = left # Верхний индекс
    pivotVal = A[left]
    i = left + 1
    while i <= right: # Пока есть область не просмотренных элементов.
        #Cq += 1
        if A[i] < pivotVal:
            pivotPoint += 1 # Если элемент меньше оси
            if i > pivotPoint: # убирает перестановки эл-та с самим собой
                #Mq += 1
                A[i], A[pivotPoint] = A[pivotPoint],A[i]# гоним его в начало интервала
                indexLow = indexLow + 1 # сужаем область слева
        i += 1
        #print(A, left, pivotPoint)
    A[left],  A[pivotPoint] = A[pivotPoint], A[left]
    #1Mq += 1
    return pivotPoint


#Сортировка пузырьком
def BubbleSort(arr):
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

#Сортировка вставками
def InsertionSort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

#Сортировка бинарным деревом
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
        #global x, y
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                #x += 1
                if current.left == None:
                    #y += 1
                    current.left = Node(val, None, None)
                    break
                current = current.left
            elif val > current.key:
                #x += 1
                if current.right == None:
                    #y += 1
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
        print('\n')

    def inorder(self):
        self.inorder_()

#Поиск по бинарному дереву
    def find_(self, val):
        #global z
        if self.root == None:
            self.root = Node(val, None, None)
            return
        current = self.root
        while current:
            if val <= current.key:
                #z += 1
                if  current.key == val:
                    print("Искомое значение найдено")
                    break
                elif (current.left == None) and (current.key != val):
                    print("Искомое значение не найдено")
                current = current.left
            elif val > current.key:
                #z += 1
                if current.key == val:
                    print("Искомое значение найдено")
                    break
                elif (current.right == None) and (current.key != val):
                    print("Искомое значение не найдено")
                current = current.right

    def find(self, val):
        self.find_(val)

def SortTree(array):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert(i)

def FTree(array, val):
    if __name__ == "__main__":
        t = Tree()
        for i in array:
            if i == "0":
                break
            t.insert((i))
        t.find(val)

#Поиск минимального и максимального значений линейным поиском
def arrayMinMax(array):
    #while k < (len(array) - 1): 
    Min = 0
    Max = 0
    i = 1
    o = 1
    for i in range(len(array)):
        if array[i] < array[Min]:
            Min = i
        i += 1
    for o in range(len(array)):
        if array[o] > array[Max]:
            Max = o
        o += 1
    print ("Минимальное значение: ", array[Min])
    print ("Максимальное значение: ", array[Max])
    print ("Колличество операций сравнения: ", i+o)

#Бинарный поиск
def BinSearch(array, x):
    i = 0
    j = len(array)-1
    m = int(j/2)
    while array[m] != x and i < j:
        if x > array[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
        #y +=1
    if i > j:
        print ("Искомое значение не найдено")
    else:
        print ("Искомое значение стоит под номером: ", m)
    #print ("Колличество операций сравнения: ")


u=int(input("Введите, как вы собираетесь вводить массив(1=РАНДОМНО, 2=ВРУЧНУЮ, 3=ЧТЕНИЕ ИЗ ФАЙЛА): "))

if (u==1):
    h = int(input("Введите размер массива(10000, 30000, 50000, 70000, 90000): "))
    array=([random.randint(0, 10000000000) for x in range(h)])
    print("Элементы массива:")
    print(array)

elif (u==2):
    n = int(input("Введите размер массива: "))
    print("Введите элементы массива:")
    array = [int(input()) for x in range(n)]
    print("Элементы массива:")
    print(array)

elif (u==3):
    f = open('test.scv', 'r')
    lines = f.readlines() 
    f.close()
    array = [int(line) for line in lines]
    n = len(array)
    print("Элементы массива:")
    print(array)

else:
    print("Вы допустили ошибку!")

array1 = copy.copy(array)
array2 = copy.copy(array)
array3 = copy.copy(array)
array4 = copy.copy(array)
array5 = copy.copy(array)

# Быстрая сортировка и подсчет времени
print("Быстрая сортировка Хоара и подсчет времени")
with Profiler() as p:
    array1 = QuickSort(array1, 0, len(array1) - 1)
#print('Число операций сравнения = ' + str(Cq))
#print('Число операций перемещения = ' + str(Mq))

# Сортировка пузырьком
print("Сортировка пузырьком и  подсчет времени")
with Profiler() as p:
    BubbleSort(array2)
#print('Число операций сравнения = ' + str(Cb))
#print('Число операций перемещения = ' + str(Mb))

# Сортировка вставками
print("Сортировка вставками и подсчет времени")
with Profiler() as p:
    InsertionSort(array3)
#print('Число операций сравнения = ' + str(Ci))
#print('Число операций перемещения = ' + str(Mi))

# Сортировка деревом
print("Сортировка деревом и подсчет времени")
with Profiler() as p:
    array4 = SortTree(array4)
#print('Число операций сравнения = ' + str(Ct))
#print('Число операций перемещения = ' + str(Mt))

# Линейный поиск минимума и максимума
print("Линейный поиск минимума и максимума")
with Profiler() as p:
    arrayMinMax(array5)

# Бинарный поиск значения
print("Бинарный поиск")
k = int(input())
with Profiler() as p:
    BinSearch(array3, k)

# Поиск бинарным деревом
print("Поиск бинарным деревом")
key = random.randint(0, 100)
print(key)
Time = time.time()
p = FTree(array5, key)
Time = time.time() - Time
print("Время: %.3f" % format(Time), " sec")
#print('Число операций сравнения = ' + str(Mf))
    
