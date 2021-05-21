# variables
from typing import List

exclamation_mark = "\""
test_text_with_exclamation_mark = "\"abcd\""


# methods
def get_exclamation_marks_index_location(text: str):
    indexes_list: List[int] = []
    for element in range(0, len(text)):
        if text[element] == exclamation_mark:
            indexes_list.append(element)
    return indexes_list


testList = get_exclamation_marks_index_location(test_text_with_exclamation_mark)
print(testList)


# abcde
# def slice_string(text: str): pass
# char at middle
# t1 = text[0:3]
# t2 = text[4:len(text)]
# t_final = t1+t2
# char at start
# t = text[1:len(text)]
# char at end
# lf = len(text)-1
# ll = len(text)
# t = text[lf:ll]
# print(t)
# execution
#   task
#   ---
#   input string
#   output string without exclamation marks
#   ---
#   loop through string as array of chars and remove every wrong char
#   ---
#   1.remove chars from string
#   2.loop through string   --- DONE
#   ---
#   string removal:
#   slice(start, stop, step)
#   s[start:stop:step]
#   l = len(py_string)
#   t - i - 2   0 1 3 - (l-1)
#   print(py_string[0:2] + py_string[3: l])
#   remove y => position "1"
#   l - 6
#   py_string[0:2:]
