#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list[:x]:
            if isinstance(element, int):
                print(element, end='')
                count += 1
            else:
                x += 1
                continue
        print()
        return count
    except IndexError:
        for element in my_list:
            print(element, end='')
            count += 1
        print()
        return count
