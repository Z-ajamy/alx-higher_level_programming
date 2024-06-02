#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    try:
        for element in my_list[:x]:
            print(element, end='')
            count += 1
        print()
        return count
    except IndexError:
        for element in my_list:
            print(element, end='')
            count += 1
        print()
        return count
