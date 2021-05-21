# variables
exclamation_mark = "\""
text_with_exclamation_mark = "abcd\""


# methods
def remove_exclamation_marks(text):
    indexes_list = []
    for element in range(0, len(text)):
        if text[element] == exclamation_mark:
            indexes_list.append(element)
    print(indexes_list)


# execution
remove_exclamation_marks(text_with_exclamation_mark)

#   notes
#   task
#   ---
#   input string
#   output string without exclamation marks
#   ---
#   string abc  check every letter if " remove
#   loop through string as array of chars and remove every wrong char
#   ---
#   1.remove chars from string
#   2.loop through string   --- DONE
#   ---
#   slice(start, stop, step)
#   s[start:stop:step]
#   l = len(py_string)
#   t - i - 2   0 1 3 - (l-1)
#   print(py_string[0:2] + py_string[3: l])
#   remove y => position "1"
#   l - 6
#   py_string[0:2:]
