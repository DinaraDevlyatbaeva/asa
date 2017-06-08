import random
import copy
import time
import datetime

#Подсчет времени
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
    def __exit__(self, type, value, traceback):
        print("Время: %.3f" % format(time.time() - self._startTime))

#Быстрая сортировка Хоара
def QuickSort(A, left, right):
    global Cq, Mq
    indexLow  = left + 1                       
    indexHigh = right - 1    
    pivotPoint = left 
    pivotVal = A[left]
    i = left + 1
    while i <= right: 
        #Cq += 1
        if A[i] < pivotVal:
            pivotPoint += 1 
            if i > pivotPoint: 
                #Mq += 1
                A[i], A[pivotPoint] = A[pivotPoint],A[i]
                indexLow = indexLow + 1 
        i += 1
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
                #print(node.key , end=" ")
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
                    print("Èñêîìîå çíà÷åíèå íàéäåíî")
                    break
                elif (current.left == None) and (current.key != val):
                    print("Èñêîìîå çíà÷åíèå íå íàéäåíî")
                current = current.left
            elif val > current.key:
                #z += 1
                if current.key == val:
                    print("Èñêîìîå çíà÷åíèå íàéäåíî")
                    break
                elif (current.right == None) and (current.key != val):
                    print("Èñêîìîå çíà÷åíèå íå íàéäåíî")
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

#Поиск минимума и максимума линейным поиском
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
        print ("Искомое значение найдено под номером: ", m)
    #print ("Êîëëè÷åñòâî îïåðàöèé ñðàâíåíèÿ: ")


u=int(input("Введите как вы хотите ввести массив(1=рандомно, 2=вручную, 3=из файла): "))

if (u==1):
    h = int(input("Введите размер массива(10000, 30000, 50000, 70000, 90000): "))
    array=([random.randint(0, 10000000000) for x in range(h)])
    print("Элементы массива:")
    print(array)

elif (u==2):
    n = int(input("Введите размер массива: "))
    print("Введите элементы массива:")
    array = [int(input()) for x in range(n)]
    print("Эллементы массива:")
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
    print("Вы ошиблись!")

array1 = copy.copy(array)
array2 = copy.copy(array)
array3 = copy.copy(array)
array4 = copy.copy(array)
array5 = copy.copy(array)

#Быстрая сортировка Хоара
print("Быстрая сортировка Хоара")
with Profiler() as p:
    array1 = QuickSort(array1, 0, len(array1) - 1)
print (array)
#print('×èñëî îïåðàöèé ñðàâíåíèÿ = ' + str(Cq))
#print('×èñëî îïåðàöèé ïåðåìåùåíèÿ = ' + str(Mq))

#Сортировка пузырьком
print("Сортировка пузырьком")
with Profiler() as p:
    BubbleSort(array2)
print(array)
#print('×èñëî îïåðàöèé ñðàâíåíèÿ = ' + str(Cb))
#print('×èñëî îïåðàöèé ïåðåìåùåíèÿ = ' + str(Mb))

#Сортировка вставками
print("Сортировка вставками")
with Profiler() as p:
    InsertionSort(array3)
print (array)
#print('×èñëî îïåðàöèé ñðàâíåíèÿ = ' + str(Ci))
#print('×èñëî îïåðàöèé ïåðåìåùåíèÿ = ' + str(Mi))

#Сортировка бинарным деревом
print("Сортировка бинарным деревом")
with Profiler() as p:
    array4 = SortTree(array4)
print (array)
#print('×èñëî îïåðàöèé ñðàâíåíèÿ = ' + str(Ct))
#print('×èñëî îïåðàöèé ïåðåìåùåíèÿ = ' + str(Mt))

#Поиск минимума и максимума линейным поиском
print("Поиск минимума и максимума линейным поиском")
with Profiler() as p:
    arrayMinMax(array5)

#Бинарный поиск
print("Бинарный поиск")
k = int(input())
with Profiler() as p:
    BinSearch(array3, k)

#Поиск по бинарному дереву
print("Поиск по бинарному дереву")
key = random.randint(0, 100)
print(key)
Time = time.time()
p = FTree(array5, key)
Time = time.time() - Time
print("Âðåìÿ: %.3f" % format(Time), " sec")
#print('×èñëî îïåðàöèé ñðàâíåíèÿ = ' + str(Mf))
