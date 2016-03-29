def quick_sort(d, s, e):
    start = s
    end = e
    if s < e:
        pIndex = positioning(d, start, end)
        quick_sort(d, start, pIndex-1)
        quick_sort(d, pIndex+1,  end)

def positioning (d, s, e):
    start = s
    end = e
    pivot = d[end]
    pIndex = start


    for i in range(start, end):# important to have as end -1 or else it ll loop as infinite
        if d[i] <= pivot:
            d[i], d[pIndex] = d[pIndex], d[i]
            pIndex += 1

    d[pIndex], d[end] = d[end], d[pIndex]

    return pIndex

d= [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(d, 0, len(d)-1)
print d

