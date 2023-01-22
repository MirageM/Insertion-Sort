#Insertion Sort
#Best: O(n) time | O(1) spac
#Average: O(n^2) time | O(1) space
#Worst: O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(j - 1, j, array)
            j -= 1
    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]