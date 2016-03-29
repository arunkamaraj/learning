def bubblesort(data):

    for i in range(len(data)-1, 0, -1): #clever part is here
        for j in range(i):
            if data[j] > data[j+1]:
            #     temp = data[j+1]
            #     data[j+1] = data[j]
            #     data[j] = temp
                data[j+1], data[j] = data[j], data[j+1]

    print data
d = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubblesort(d)

# print d
