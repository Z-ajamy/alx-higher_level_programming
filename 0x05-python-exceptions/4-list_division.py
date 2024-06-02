#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            a = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            a = (0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            a = (0)
            continue
        except IndexError:
            print("out of range")
            a = (0)
            continue
        finally:
            new_list.append(a)
    return new_list
