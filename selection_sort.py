__author__ = 'akamara'

def selection_sort(data):
    for i in range(len(data)):
        min = i

        for j in range(i, len(data)):
            if data[j] < data[min]:
                min = j

        data[i], data[min] = data[min], data[i]

    print data


data = [2,9,6,5,3,1]
selection_sort(data)