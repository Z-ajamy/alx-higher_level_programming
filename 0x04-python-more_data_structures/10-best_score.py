#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary or a_dictionary is not None:
        length = len(a_dictionary)
        list_of_dict = list(a_dictionary.items())
        print(list_of_dict)
        print(list_of_dict[2][1])
        for i in range(length - 1):
            if list_of_dict[i][1] > list_of_dict[i + 1][1]:
                idx = i
        return list_of_dict[idx][0]

            
