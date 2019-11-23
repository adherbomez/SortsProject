from sortFunctions import RandomList
from sortFunctions import BubbleSort
from sortFunctions import QuickSort
from sortFunctions import MergeSort
from averageFunctions import SetAverage
import time
'''
    This is all my access to my different function from others files
'''

size = [10, 100, 1000, 10000, 100000]
openFile = False
fileBs = None
averageBs = []
averageQs = []
averageMs = []

numberOfSort = 1
'''
    Initialisation of differents averages
'''
'''
    numberOfSort = 1 for the BubbleSort
    numberOfSort = 2 for the QuickSort
    numberOfSort = 3 for the MergeSort
    numberOfSort is define for more flexibilities
'''


def main():

    for j in range(len(size)):
        '''
            Range the list with the differents hight of the list
        '''
        if(numberOfSort == 1):

            openFile = False

            for i in range(0, 100):
                '''
                    Do one undread times the operation to have many values
                '''
                list = RandomList(size[j])
                listBs = list.copy()
                '''
                    Set here all similars lists for the three differents sorts
                '''
                if(openFile is False):
                    path = "timeOfSort/timeBubbleSort/"
                    fileBs = open(path + str(size[j]) + ".py", "w")
                    openFile = True
                    '''
                        Open the file who add current time to it
                    '''
                startTime = time.time()
                BubbleSort(listBs)
                currentTime = (time.time() - startTime)

                fileBs.write(str(currentTime) + "\n")
                '''
                    currentTime is the current time after execution
                    fileBs.write add the current time to the selected file
                '''
                averageBs.append(currentTime)

                print("Time of BubbleSort: ", currentTime)

                if (i == 99):
                        SetAverage(size[j], averageBs, "averageOfSort/averageBubbleSort.py")

        elif(numberOfSort == 2):

            openFile = False

            for i in range(0, 100):
                list = RandomList(size[j])
                listQs = list.copy()
                '''
                    Set here all similars lists for the three differents sorts
                '''
                '''
                    Do one undread times the operation to have many values
                '''
                if(openFile is False):
                    path = "timeOfSort/timeQuickSort/"
                    fileQs = open(path + str(size[j]) + ".py", "w")
                    openFile = True
                    '''
                        Open the file who add current time to it
                    '''
                startTime = time.time()
                QuickSort(listQs, 0, len(listQs)-1)
                print(listQs)
                currentTime = (time.time() - startTime)

                fileQs.write(str(currentTime) + "\n")
                '''
                    currentTime is the current time after execution
                    fileBs.write add the current time to the selected file
                '''
                averageQs.append(currentTime)

                print("Time of QuickSort: ", currentTime)

                if (i == 99):
                        SetAverage(size[j], averageQs, "averageOfSort/averageQuickSort.py")

        elif(numberOfSort == 3):

            openFile = False

            for i in range(0, 100):
                '''
                    Do one undread times the operation to have many values
                '''
                list = RandomList(size[j])
                listMs = list.copy()
                '''
                    Set here all similars lists for the three differents sorts
                '''
                if(openFile is False):
                    path = "timeOfSort/timeMergeSort/"
                    fileMs = open(path + str(size[j]) + ".py", "w")
                    openFile = True
                    '''
                        Open the file who add current time to it
                    '''
                startTime = time.time()
                MergeSort(listMs)
                currentTime = (time.time() - startTime)

                fileMs.write(str(currentTime) + "\n")
                '''
                    currentTime is the current time after execution
                    fileBs.write add the current time to the selected file
                '''
                averageMs.append(currentTime)

                print("Time of MergeSort: ", currentTime)

                if (i == 99):
                        SetAverage(size[j], averageMs, "averageOfSort/averageMergeSort.py")

                startTime = time.time()


if __name__ == '__main__':
    main()
