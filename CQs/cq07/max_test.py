from find_max import find_and_remove_max

__author__ = "730813763"

def test_empty_list_edge_case() -> None: # Testing the edge case that happens when the argument list is empty
    b: list[int] = []
    assert find_and_remove_max(b) == -1

def test_return_value_use_case() -> None: # Testing if max value is returned
    a: list[int] = [1, 2, 3, 4]
    assert find_and_remove_max(a) == 4

def test_mutation_use_case() -> None: # Testing if the list is modified correctly
    a: list[int] = [1, 2, 3, 4]
    find_and_remove_max(a)
    assert a == [1, 2, 3]




