import random
import sys
'''
Python 3.0
This file allow to show the different sort's functions
'''
sys.setrecursionlimit(5000)
'''
    sys.setrecursionlimit() change the default value of the recursion limit
'''


def RandomList(size):
    '''
    Function who give us a list with random value for being sorted after that
    The import of random class and the function randint() is neccessary
    '''
    list = [0]*size
    for i in range(size):
        list[i] = random.randint(0, size)
    return list


def BubbleSort(listBs):
    '''
        listBs: List has sorted
    '''
    '''
        This function give us a sort of the RandomList with the BubbleSort
        method. This method run the length of the list with the first element
        and inverse the element if is higher than other. Then, the program
        continue with the next value while the list isn't sorted
    '''
    for i in range(len(listBs), 0, -1):
        for j in range(0, i-1):
            if (listBs[j+1] < listBs[j]):
                listBs[j+1], listBs[j] = listBs[j], listBs[j+1]
    return listBs


def Partition(listQs, low, high):
    '''
        listQs: List has sorted
        low: smaller index of listQS, it's 0
        high: length of listQs
    '''
    '''
        This function is used for the QuickSort function and give the value
        of the pivot I take the last element and I sort him then I place the
        higher values at the right and the smaller values at the left
    '''
    i = low
    pivot = listQs[high]
    for j in range(low, high):
        if (listQs[j] < pivot):
            permuteOne = listQs[i]
            listQs[i] = listQs[j]
            listQs[j] = permuteOne
            i = 1 + i
    permuteTwo = listQs[i]
    listQs[i] = listQs[high]
    listQs[high] = permuteTwo
    return i


def QuickSort(listQs, low, high):
    '''
        listQs: List has sorted
        low: smaller index of listQS, it's 0
        high: length of listQs
    '''
    '''
        This Function allow us to sort a list with the quick sort
        Quick sort use a pivot a replace the value that lower and higer than
        him When it's done, the function use an other pivot while the list
        isn't sorted
    '''
    if low < high:
        partitionIndex = Partition(listQs, low, high)
        QuickSort(listQs, low, partitionIndex-1)
        QuickSort(listQs, partitionIndex+1, high)


def MergeSort(listMs):
    '''
        listMs: List has sorted
    '''
    '''
        This function show us to sort a list with the merge sort
        Merge sort allow us to divise the list in many little list
        It do list of 1, then 2, then 4 etc and sort and replace the higher and
        smaller value
    '''
    if len(listMs) > 1:
        mid = len(listMs)//2
        lefthalf = listMs[:mid]
        righthalf = listMs[mid:]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        '''
            Separation of the list in to 2 lists from the mid list with right
            part and left part
        '''

        i = j = k = 0
        '''
            Declaration of the index neccessary
        '''
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                listMs[k] = lefthalf[i]
                i = i + 1
            else:
                listMs[k] = righthalf[j]
                j = j + 1
            k = k + 1
            '''
                i is the index of the lefthalf list
                j is the index of the righthalf list
                k is the index of listMs the final list
            '''

        while i < len(lefthalf):
            listMs[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            listMs[k] = righthalf[j]
            j = j + 1
            k = k + 1
            '''
                Place the rest of lefthalf and righthalf list to build listMs
            '''
