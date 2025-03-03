import pytest
from src.sorting_algorythms.insertion_sort import insertion_sort
from src.sorting_algorythms.merge_sort import merge_sort
from src.sorting_algorythms.quick_sort import quick_sort
from src.sorting_algorythms.selection_sort import selection_sort


# Test the insertion_sort function
def test_insertion_sort():
    # Test case with unsorted integers
    input_list = [5, 2, 9, 1, 5, 6]
    insertion_sort(input_list)
    assert input_list == [1, 2, 5, 5, 6, 9]

    # Test case with an already sorted list
    input_list = [1, 2, 3, 4, 5]
    insertion_sort(input_list)
    assert input_list == [1, 2, 3, 4, 5]

    # Test case with an empty list
    input_list = []
    insertion_sort(input_list)
    assert input_list == []

    # Test case with one element
    input_list = [3]
    insertion_sort(input_list)
    assert input_list == [3]

    # Test case with negative numbers
    input_list = [-3, -1, -2, 0, -5]
    insertion_sort(input_list)
    assert input_list == [-5, -3, -2, -1, 0]


# Test the merge_sort function
def test_merge_sort():
    # Test case with unsorted integers
    unsorted_list = [5, 2, 9, 1, 5, 6]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 5, 5, 6, 9]

    # Test case with an already sorted list
    unsorted_list = [1, 2, 3, 4, 5]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 3, 4, 5]

    # Test case with an empty list
    unsorted_list = []
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == []

    # Test case with one element
    unsorted_list = [3]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [3]

    # Test case with negative numbers
    unsorted_list = [-3, -1, -2, 0, -5]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [-5, -3, -2, -1, 0]


# Test the quick_sort function
def test_quick_sort():
    # Test case with unsorted integers
    arr = [5, 2, 9, 1, 5, 6]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 5, 5, 6, 9]

    # Test case with an already sorted list
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    # Test case with an empty list
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == []

    # Test case with one element
    arr = [3]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [3]

    # Test case with negative numbers
    arr = [-3, -1, -2, 0, -5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [-5, -3, -2, -1, 0]


# Test the selection_sort function
def test_selection_sort():
    # Test case with unsorted integers
    input_list = [5, 2, 9, 1, 5, 6]
    selection_sort(input_list)
    assert input_list == [1, 2, 5, 5, 6, 9]

    # Test case with an already sorted list
    input_list = [1, 2, 3, 4, 5]
    selection_sort(input_list)
    assert input_list == [1, 2, 3, 4, 5]

    # Test case with an empty list
    input_list = []
    selection_sort(input_list)
    assert input_list == []

    # Test case with one element
    input_list = [3]
    selection_sort(input_list)
    assert input_list == [3]

    # Test case with negative numbers
    input_list = [-3, -1, -2, 0, -5]
    selection_sort(input_list)
    assert input_list == [-5, -3, -2, -1, 0]
