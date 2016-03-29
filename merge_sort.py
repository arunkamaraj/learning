__author__ = 'akamara'

def sort_merge(merge_list):
    print("Splitting ", merge_list)
    length = len(merge_list)
    if length > 1:
        mid = len(merge_list)/2
        left = merge_list[:mid]
        right = merge_list[mid:]
        # print left, right
        sort_merge(left)
        sort_merge(right)
        merge(left, right, merge_list)


def merge(left, right, merge_list):

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_list[k] = left[i]
            i = i+1
        elif left[i] > right[j]:
            merge_list[k] = right[j]
            j=j+1
        k=k+1

    while i < len(left):
        merge_list[k] = left[i]
        i=i+1
        k=k+1

    while j < len(right):
        merge_list[k] = right[j]
        j=j+1
        k=k+1
    print "merged list", merge_list


# d = [9, 8, 7, 6, 5, 4, 3, 2, 1]
d = [54,26,93,17,77,31,44,55,20]

d = [5]
sort_merge(d)
print d