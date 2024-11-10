from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest

__author__ = "730813763"

def test_only_evens_use_case_1(): 
    """Tests if the return value is as intented."""
    assert only_evens([1, 2, 3]) == [2]

def test_only_evens_use_case_2():
    """Tests if the list is modified correctly."""
    a = [1, 2, 3]
    only_evens(a) # Modifies the list to check with assert
    assert a == [1, 2, 3]

def test_only_evens_edge_case():
    """Tests if the case where the list consisting only of even values handled correctly."""
    assert only_evens([4, 4, 4]) == [4, 4, 4] # Comparing the intended return value with what is actually returned.

def test_sub_use_case_1():
    """Tests if the return value is as intented."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30] # Comparing with the intended return value.

def test_sub_use_case_2():
    """Tests if list is modified correctly"""
    a_list = [10, 20, 30, 40]
    sub(a_list, -1, 6) # Modifies the list 
    assert a_list == [10, 20, 30, 40] 

def test_sub_edge_case():
    """Tests how an empty list is handled"""
    list2 = [] # Creates an empty list
    assert sub(list2, 1, 3) == []

def test_add_at_index_use_case_1():
    """Tests that list is modified correctly."""
    list = [1, 2, 3, 4]
    add_at_index(list, 3, 2) # Modifies the list
    assert list == [1, 2, 3, 3, 4]

def test_add_at_index_use_case_2():
    """Tests that add_at_index returns None """
    assert add_at_index([1, 2, 3, 4], 2, 2) == None # Checks if there is any return value

def test_add_at_index_edge_case_1():
    """Tests that add_at_index raises an IndexError for an invalid index."""
    list = [2, 3, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(list, 2, 5)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num> 
        # that is greater than the length of our <list_object>






