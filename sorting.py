#!C:\Python27\python.exe
# _*_ coding=utf-8 _*_

import random

def main():
    max_num = 1000
    cur_num = 100
    arr = random.sample(range(1,max_num),cur_num)
    print arr
    #insert_sort(arr, cur_num)
    print merge_sort(arr)
    #bubble_sort(arr)
    pass



def insert_sort(arr, length):
    """This is the basic insert sort alg.
    :param arr: The unsorted sequence(list)
    :param length: The length of the unsorted sequence
    :return:the sorted sequence
    """

    for i in range(1,length):
        j = i - 1
        key = arr[i]
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1
    return arr


def merge_sort(arr):
    """
    This is the basic merge sort alg.
    :param arr:The unsorted sequence(list)
    :return:The sorted sequence
    """
    if len(arr) > 1:
        m = int(len(arr)/2)
        larr = arr[:m]
        rarr = arr[m:]
        l = merge_sort(larr)
        r = merge_sort(rarr)
        return merge(l, r)
    else:
        return arr

def merge(larr, rarr):
    """
    merge the two sub-arr to one arr
    :param larr:The left arr to be merged
    :param rarr:The right arr to be merged
    :return:The merged arr
    """
    marr = list()
    while larr and rarr:
        if larr[0] < rarr[0]:
            marr.append(larr.pop(0))
        else:
            marr.append(rarr.pop(0))
    if larr:
        marr += larr
    if rarr:
        marr += rarr
    return marr

def bubble_sort(arr):
    """
    This is the basic bubble sort.
    :param arr:The unsorted sequence(list)
    :return:The sorted sequence
    """
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j + 1]:
                key = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = key
    return arr

def quick_sort(arr):
    """
    This is the basic quick sort alg.
    :param arr:The unsorted sequence
    :return:The sorted sequence
    """
    pass
if __name__ == '__main__':
    main()
