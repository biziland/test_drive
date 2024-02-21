import math
import copy
class package():
    def __init__(self, id, x1, y1, x2, y2, price):
        self.id = id
        self.pointA = (x1,y1)
        self.pointB = (x2,y2)
        self.price = price

class kur():
    def __init__(self,id,kor,v):
        self.id = id
        self.kor = kor
        self.v = v
def shift_matrix(matrix):
    rows = len(matrix)
    temp_row = matrix[rows - 1]
    for i in range(rows - 1, 0, -1):
        matrix[i] = matrix[i - 1]
    matrix[0] = temp_row
    return matrix

def thirdtry(lk,lp):

    array_kur = []
    for row in lk:
        ar = kur(row['id'],(row['x1'],row['y1']),row['v'])
        array_kur.append(ar)

    array_pack = []  
    for row in lp:
        ar = package(int(row['id']),row['x1'],row['y1'],row['x2'],row['y2'],row['price'])
        array_pack.append(ar)

    
    rows = len(array_pack)
    cols = len(array_kur)
    t = []
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
            raspr.append((array_of_id[count],min_index))
            prev_min_index = min_index
            array_of_max.append(min_value)
            count+=1

        return raspr, max(array_of_max)
    
    array_of_id = []
    for i in range(len(array_pack)):
        array_of_id.append(i)
    
    for i in range(len(array_pack)):
        array_of_var.append((jkl(t,array_of_id)))
        shift_matrix(t)
        shift_matrix(array_of_id)
        print(t)

    max_array = []
    for i in range(len(array_of_var)):
        max_array.append(array_of_var[i][1])

    right_one = array_of_var[max_array.index(min(max_array))][0]
    mas = []
    for i in right_one:
        mas.append((array_pack[i[0]].id,array_kur[i[1]].id))

    for i in right_one:
        print("Посылку номер ",array_pack[i[0]].id," посылку отнесёт курьер номер ", array_kur[i[1]].v, " за ", array_pack[i[0]].price)
    
    return mas

