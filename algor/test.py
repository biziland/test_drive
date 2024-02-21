import math
import copy

#class package():
#      def __init__(self, x1, y1, x2, y2):
#         self.pointA = (x1,y1)
#         self.pointB = (x2,y2)
#        # self.price = price

# можно добавить скорость передвижения курьеров (пеший = 2 км/ч, машина = 40 км/ч)
"""class kur():
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1
"""
"""array_pack = []
# Открытие файла
line = []
filename = "example.txt"  # Имя файла, который нужно прочитать
with open(filename, "r") as file:
    # Чтение содержимого файла и запись в список
    for i in file:
        for j in i:
            if j != " ":
                line.append(j)                        
        ar = package(line[0],line[1],line[2],line[3])
        print(line)
        line = []
        array_pack.append(ar)"""

# распределение с учетом одинаковой скоростью доставщиков и в приоритете посылки по времени, не учитывается общее время доставок посылок
def firsttry():
    filename = "packages.txt"
    array_pack = []
    with open(filename, "r") as file:
        for i in file:
            line = []
            for j in i:
                if j != " " and j != "\n":
                    line.append(int(j))                        
            ar = (line[0],line[1])
            array_pack.append(ar)

    filename = "kur.txt"
    array_kur = []
    with open(filename, "r") as file:
        for i in file:
            line = []
            for j in i:
                if j != " " and j != "\n":
                    line.append(int(j))                        
            ar = (line[0],line[1])
            array_kur.append(ar)


    for i in array_pack:
        print(i)    
    
    # заполняем матрицу расстояний
    rows = len(array_pack)
    cols = len(array_kur)
    distan = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(math.dist(array_pack[i],array_kur[j]))
        distan.append(row)
    print(distan)

    # выбираем в каждой строчке минимальное значение и убираем его из последующих строчек матрицы Nan
    raspr = []
    count = 0
    for i in distan:
        min_value = min(i)
        max_value = max(i)
        min_index = i.index(min_value)
        raspr.append((count+1,min_index+1))
        for j in distan:
            j[min_index] = max_value
        count+=1
        print(min_index)
    for i in raspr:
        print("Посылку номер ",i[0]," посылку отнесёт курьер номер ", i[1])




# распределение с учетом разной скоростью доставщиков и в приоритете посылки по времени, не учитывается общее время доставок посылок
def secondtry():
    
    class package():
         def __init__(self, x1, y1, x2, y2, price):
            self.pointA = (x1,y1)
            self.pointB = (x2,y2)
            self.price = price

    class kur():
        def __init__(self,kor,v):
            self.kor = kor
            self.v = v

    array_pack = []
    filename = "packages.txt" 
    with open(filename, "r") as file:
        for i in file:
            i = i.split() 
            ar = package(int(i[0]),int(i[1]),int(i[2]),int(i[3]),i[4])
            array_pack.append(ar)
            #print(i)
    array_kur = []
    filename = "kur.txt" 
    with open(filename, "r") as file:
        for i in file:
            i = i.split() 
            for j in range(len(i)):
                 i[j] = int(i[j])               
            ar = kur((i[0],i[1]),i[2])
            array_kur.append(ar)


    rows = len(array_pack)
    cols = len(array_kur)
    t = []
    #array_pack_koord = [for i in range(len)]
    for i in range(rows):
        row = []
        for j in range(cols-1):
            row.append((math.dist(array_pack[i].pointA,array_kur[j].kor)+math.dist(array_pack[i].pointA,array_pack[i].pointB))/array_kur[j].v)
        t.append(row)
    print(t)

    # выбираем в каждой строчке минимальное значение и убираем его из последующих строчек матрицы Nan
    raspr = []
    count = 0
    sum = 0
    prev_min_index = 0
    for i in t:
        max_value = max(i)
        if count!=0:
            for j in t:
                j[prev_min_index] = max_value
        min_value = min(i)
        sum+= min_value
        min_index = i.index(min_value)
        raspr.append((count+1,min_index+1))
        prev_min_index = min_index
        count+=1
        #print(min_index)
    for i in raspr:
        print("Посылку номер ",i[0]," посылку отнесёт курьер номер ", i[1])
    print(sum)






def shift_matrix(matrix):
    rows = len(matrix)
    #cols = len(matrix[0])
    
    # Сохраняем нижнюю строку
    temp_row = matrix[rows - 1]
    
    # Сдвигаем строки вниз
    for i in range(rows - 1, 0, -1):
        matrix[i] = matrix[i - 1]
    
    # Перемещаем нижнюю строку наверх
    matrix[0] = temp_row
    
    return matrix


# распределение с учетом разной скоростью доставщиков и в приоритете, чтобы ВСЕ посылки были доставлены за минимальное время
def thirdtry():
    class package():
         def __init__(self, id, x1, y1, x2, y2, price):
            self.id = id
            self.pointA = (x1,y1)
            self.pointB = (x2,y2)
            self.price = price

    class kur():
        def __init__(self,kor,v):
            self.kor = kor
            self.v = v

    array_pack = []
    filename = "packages.txt" 
    with open(filename, "r") as file:
        for i in file:
            i = i.split() 
            ar = package(int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])
            array_pack.append(ar)
            
    array_kur = []
    filename = "kur.txt" 
    with open(filename, "r") as file:
        for i in file:
            i = i.split() 
            for j in range(len(i)):
                 i[j] = int(i[j])               
            ar = kur((i[0],i[1]),i[2])
            array_kur.append(ar)


    rows = len(array_pack)
    cols = len(array_kur)
    t = []
    #array_pack_koord = [for i in range(len)]
    for i in range(rows):
        row = []
        for j in range(cols-1):
            row.append((math.dist(array_pack[i].pointA,array_kur[j].kor)+math.dist(array_pack[i].pointA,array_pack[i].pointB))/array_kur[j].v)
        t.append(row)
    print(t)
    # выбираем в каждой строчке минимальное значение и убираем его из последующих строчек матрицы Nan
    array_of_var = []
    def jkl(t,array_of_id):
        array_of_max = []
        temp = copy.deepcopy(t)
        raspr = []
        count = 0
        prev_min_index = 0
        for i in temp:
            max_value = max(i)
            if count!=0:
                for j in temp:
                    j[prev_min_index] = max_value
            min_value = min(i)
            min_index = i.index(min_value)
            raspr.append((array_of_id[count],min_index+1))
            prev_min_index = min_index
            array_of_max.append(min_value)
            count+=1
        for i in raspr:
            print("Посылку номер ",i[0]," посылку отнесёт курьер номер ", i[1])

        print("Max time is",max(array_of_max))
        return raspr, max(array_of_max)
    
    array_of_id = []
    for i in array_pack:
        array_of_id.append(i.id)
    
    for i in range(len(array_pack)):
        array_of_var.append((jkl(t,array_of_id)))
        shift_matrix(t)
        shift_matrix(array_of_id)
        print(t)

    max_array = []
    for i in range(len(array_of_var)):
        max_array.append(array_of_var[i][1])

    right_one = array_of_var[max_array.index(min(max_array))][0]
    for i in right_one:
        print("Посылку номер ",i[0]," посылку отнесёт курьер номер ", i[1])
    

        

thirdtry()

