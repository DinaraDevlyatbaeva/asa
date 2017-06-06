import random
import copy
import time
import datetime

#Заполнение массива
def Fillingin (n):
    A = [[0] * 2 for i in range(n)]

    for x in range(n):
        A[x][0] = int(time.mktime(time.strptime(str(random.randrange(1980, 2017)) + " 0" + str(random.randrange(1, 9)), '%Y %m')))
        A[x][1] = random.randrange(0, 100)
    print(A)
    return A

#Подсчет времени выполнения сортировки или поиска
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Время: {:.3f} sec".format(time.time() - self._startTime))

#Быстрая сортировка
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)
    
#Сортировка пузырьком
def buble_sort(mylist):
    for k in range(len(mylist) - 1):
        m = k
        i = k + 1
        while i < len(mylist):
            if mylist[i] < mylist[m]:
                m = i
            i += 1
        t = mylist[k]
        mylist[k] = mylist[m]
        mylist[m] = t

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
        # print('.')

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

#Поиск минимума и максимума линейным поиском
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

#Бинарный поиск значения
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

print('Введите как вы хотите работать с массивом: 1=вручную, 2=рандомно')
temp = int(input())

massive = []

if (temp == 1):
    n = int(input("Введите размер массива: "))
    print("Введите элементы массива:")
    massive = [float(input()) for x in range(n)]
    print("Элементы массива:")
    print(massive)

    array1 = copy.copy(massive)
    array2 = copy.copy(massive)
    array3 = copy.copy(massive)
    array4 = copy.copy(massive)

    print("Быстрая сортировка и подсчет времени")
    with Profiler() as p:
        array1 = QuickSort(array1)
    print(array1)

    print("Сортировка пузырьком и подсчет времени")
    with Profiler() as p:
        buble_sort(array2)
    print(array2)

    print("Сортировка вставками и подсчет времени")
    with Profiler() as p:
        insertion_sort(array3)
    print(array3)

    print("Сортировка бинарным деревом и подсчет времени")
    with Profiler() as p:
        array4 = SortTree(array4)

    print("Поиск минимума и максимумв в заданных случаях линейным поиском")
    ArrayMinAndMaxWrite = []
    with Profiler() as p:
        ArrayMinAndMaxWrite = min1(array3)
        
    print("Бинарный поиск значения")    
    number = int(input("Введите искомое вами значение: "))

    with Profiler() as p:
        interpolationSearch(array3, number)

    csvArr17 = [random.randint(0, 100) for i in range(10)]
    key = csvArr17[random.randint(0, 10)]
    print(key)
    tf = FTree(csvArr17, key)
    print('Время: ' + str(tf))

elif (temp==2):
    r=int(input("Введите разме массива(10000, 30000, 50000, 70000, 90000): "))
    if (r==10000):
        massive = []
        massive = Fillingin(10000)

        array1 = copy.copy(massive)
        array2 = copy.copy(massive)
        array3 = copy.copy(massive)
        array4 = copy.copy(massive)

        print("Быстрая сортировка и подсчет времени")
        with Profiler() as p:
            array1 = QuickSort(array1)
        print(array1)

        print("Сортировка пузырьком и подсчет времени")
        with Profiler() as p:
            buble_sort(array2)
        print(array2)

        print("Сортировка вставками и подсчет времени")
        with Profiler() as p:
            insertion_sort(array3)
        print(array3)

        print("Сортировка бинарным деревом и подсчет времени")
        with Profiler() as p:
            array4 = SortTree(array4)

        print("Поиск минимума и максимумв в заданных случаях линейным поиском")
        ArrayMinAndMax = []
        with Profiler() as p:
            ArrayMinAndMax = min1(array3)

        print("Бинарный поиск значения")
        number = int(input("Введите искомое вами значение: "))

        with Profiler() as p:
            interpolationSearch(array3, number)

        csvArr = [random.randint(0, 100000000) for i in range(400000)]
        key =csvArr[random.randint(0, 10)]
        print(key)
        tf = FTree(csvArr, key)
        print('Время: ' + str(tf))

    elif (r==30000):
        massive = []
        massive = Fillingin(30000)

        array1 = copy.copy(massive)
        array2 = copy.copy(massive)
        array3 = copy.copy(massive)
        array4 = copy.copy(massive)

        print("Быстрая сортировка и подсчет времени")
        with Profiler() as p:
            array1 = QuickSort(array1)
        print(array1)

        print("Сортировка пузырьком и подсчет времени")
        with Profiler() as p:
            buble_sort(array2)
        print(array2)

        print("Сортировка вставками и подсчет времени")
        with Profiler() as p:
            insertion_sort(array3)
        print(array3)

        print("Сортировка бинарным деревом и подсчет времени")
        with Profiler() as p:
            array4 = SortTree(array4)
            
        print("Поиск минимума и максимумв в заданных случаях линейным поиском")
        ArrayMinAndMax2 = []
        with Profiler() as p:
            ArrayMinAndMax2 = min1(array3)

        print("Бинарный поиск значения")
        number = int(input("Введите искомое вами значение: "))

        with Profiler() as p:
            interpolationSearch(array3, number)

        csvArr1 = [random.randint(0, 100000000) for i in range(400000)]
        key = csvArr1[random.randint(0, 10)]
        print(key)
        tf = FTree(csvArr1, key)
        print('Время: ' + str(tf))
        
    elif(r==50000):
        massive = []
        massive = Fillingin(50000)

        array1 = copy.copy(massive)
        array2 = copy.copy(massive)
        array3 = copy.copy(massive)
        array4 = copy.copy(massive)

        print("Быстрая сортировка и подсчет времени")
        with Profiler() as p:
            array1 = QuickSort(array1)
        print(array1)

        print("Сортировка пузырьком и подсчет времени")
        with Profiler() as p:
            buble_sort(array2)
        print(array2)

        print("Сортировка вставками и подсчет времени")
        with Profiler() as p:
            insertion_sort(array3)
        print(array3)

        print("Сортировка бинарным деревом и подсчет времени")
        with Profiler() as p:
            array4 = SortTree(array4)

        print("Поиск минимума и максимумв в заданных случаях линейным поиском")
        ArrayMinAndMax3 = []
        with Profiler() as p:
            ArrayMinAndMax3 = min1(array3)

        print("Бинарный поиск значения")
        number = int(input("Введите искомое вами значение: "))

        with Profiler() as p:
            interpolationSearch(array3, number)

        csvArr12 = [random.randint(0, 100000000) for i in range(400000)]
        key = csvArr12[random.randint(0, 10)]
        print(key)
        tf = FTree(csvArr12, key)
        print('Время: ' + str(tf))


    elif(r==70000):
        massive = []
        massive = Fillingin(70000)

        array1 = copy.copy(massive)
        array2 = copy.copy(massive)
        array3 = copy.copy(massive)
        array4 = copy.copy(massive)

        print("Быстрая сортировка и подсчет времени")
        with Profiler() as p:
            array1 = QuickSort(array1)
        print(array1)

        print("Сортировка пузырьком и подсчет времени")
        with Profiler() as p:
            buble_sort(array2)
        print(array2)

        print("Сортировка вставками и подсчет времени")
        with Profiler() as p:
            insertion_sort(array3)
        print(array3)

        print("Сортировка бинарным деревом и подсчет времени")
        with Profiler() as p:
            array4 = SortTree(array4)

        print("Поиск минимума и максимумв в заданных случаях линейным поиском")
        ArrayMinAndMax5 = []
        with Profiler() as p:
            ArrayMinAndMax5 = min1(testarray70k3)

        print("Бинарный поиск значения")
        number = int(input("Введите искомое вами значение: "))

        with Profiler() as p:
            interpolationSearch(array3, number)

        csvArr13 = [random.randint(0, 100000000) for i in range(400000)]
        key = csvArr13[random.randint(0, 10)]
        print(key)
        tf = FTree(csvArr13, key)
        print('Время: ' + str(tf))

    elif(r==90000):
        massive = []
        massive = Fillingin(90000)

        array1 = copy.copy(massive)
        array2 = copy.copy(massive)
        array3 = copy.copy(massive)
        array4 = copy.copy(massive)

        print("Быстрая сортировка и подсчет времени")
        with Profiler() as p:
            array1 = QuickSort(array1)
        print(array1)

        print("Сортировка пузырьком и подсчет времени")
        with Profiler() as p:
            buble_sort(array2)
        print(array2)

        print("Сортировка вставками и подсчет времени")
        with Profiler() as p:
            insertion_sort(array3)
        print(array3)

        print("Сортировка бинарным деревом и подсчет времени")
        with Profiler() as p:
            array4 = SortTree(array4)

        print("Поиск минимума и максимумв в заданных случаях линейным поиском")
        ArrayMinAndMax6 = []
        with Profiler() as p:
            ArrayMinAndMax6 = min1(testarray90k3)

        print("Бинарный поиск значения")
        number = int(input("Введите искомое вами значение: "))

        with Profiler() as p:
            interpolationSearch(array3, number)

        csvArr14 = [random.randint(0, 100000000) for i in range(400000)]
        key = csvArr14[random.randint(0, 10)]
        print(key)
        tf = FTree(csvArr14, key)
        print('Время: ' + str(tf))
    else:
        print("Вы допустили ошибку")
else:
    print("Вы допустили ошибку")
