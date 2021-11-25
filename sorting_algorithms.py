"""Formal definition of sorting algorithms in Python

Author: Tony Abou Zeidan
Date: 11/24/2021
"""

def selectionSort(lst: list):
    """Formal definition of the selection sort algorithm in Python.
    
    Steps:
    Traverse the list.
    At each index look for the smallest element in the remaining portion of the list.
    Swap this element with the current index.

    Simpler Steps:
    1) Find the smallest element in the lstay and swap it with the first element.
    2) Find the second smallest element and swap it with the second element in the lstay.
    3) Find the third smallest element and swap it with the third element in the lstay.
    4) Repeat the process of finding the next smallest element and swapping it into the
    correct position until the entire lstay is sorted.

    :param lst: The list to be sorted
    :type lst: list
    """

    # Traverse through all lstay elements
    for i in range(len(lst)):

        min_idx = i
        # Find the minimum element in the remaining unsorted list
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


def bubbleSort(lst: list):
    """Formal definition of the bubble sort algorithm in Python.

    Steps:
    Iterate over the list multiple times.
    In each iteration compare elements in pairs and keep swapping them such
    that the larger element is moved towards the end of the list.

    Advantage:
    it is one of the easiest sorting algorithms to understand and code from
    scratch. It is useful for sorting small-sized lstays.

    Disadvantage:
    with a worst-case time complexity is high, bubble sort is very slow
    compared to other sorting algorithms like quicksort.

    :param lst: The list to be sorted
    :type lst: list
    """

    n = len(lst)

    # Traverse through all lstay elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the lstay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def insertionSort(lst: list):
    """Formal defintion of the insertion sort algorithm in Python.

    Steps:
    1) Iterate from lst[1] to lst[n] over the lstay
    2) Compare current element to its predecessor (compare lst[i] to lst[i-1])
    3) If the current element is smaller than its predecessor, compare it to the elements before
    4) Move the greater elements one position up and make space for the swapped element

    :param lst: The list to be sorted
    :type lst: list
    """

    # Traverse through 1 to len(lst) (skip first index)
    for i in range(1, len(lst)):

        current = lst[i]

        # Move elements of lst[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and current < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current


def mergeSort(lst: list):
    """Formal definition of the merge sort algorithm in Python.

    The divide and conquer tactic.
    
    Steps:
    1) Divide the array into two halves
    2) Sort the left half and the right half using the same recurring algorithm
    3) Merge the sorted halves

    What is recursion?
    The merge sort algorithm uses recursion.
    This means that the function calls itself over and over
    with a smaller and smaller input until the desired result
    is achieved.

    The picture helps to understand this algorithm.

    :param lst: The list to be sorted
    :type lst: list
    """

    if len(lst) > 1:
  
        # Finding the mid of the lst
        mid = len(lst)//2
  
        # Dividing the lst elements
        L = lst[:mid]
  
        # into 2 halves
        R = lst[mid:]
  
        # Sorting the first half (recursion here, see above)
        mergeSort(L)
  
        # Sorting the second half (recursion here, see above)
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp lst L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1    