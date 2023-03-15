# Given a string with alpha-number characters and parentheses, return a string with balanced parentheses by removing the fewsest characters possible.
# You cannont add anything to the string.
# Balanced parentheses means that each opening parenthesis has a corresponding closing parenthesis and the pairs of parentheses are properly nested.


def balance(string):
    remove_pos = set()  # container
    open_pos = []  # stack
    for index, char in enumerate(string):
        if char not in "()":
            continue
        if char == "(":
            open_pos.append(index)
        elif open_pos == []:  # if ) and there is not open para
            remove_pos.add(index)
        else:  # there is opening, pop
            open_pos.pop()
    remove_pos = remove_pos.union(set(open_pos))  # union un-pop(left-over) open para
    output = ""
    for index, char in enumerate(string):
        if index not in remove_pos:
            output += char
    return output


string = "(we)(ff(we)"
string1 = "()"
string2 = "a(b)c)"
string3 = ")("
string4 = "(((("
string5 = "(()()("
string6 = ")(())("
string7 = ")())(()()("
string8 = "(())())"

print(string1 + " -> " + balance(string1))
print(string2 + " -> " + balance(string2))
print(string3 + " -> " + balance(string3))
print(string4 + " -> " + balance(string4))
print(string5 + " -> " + balance(string5))
print(string6 + " -> " + balance(string6))
print(string7 + " -> " + balance(string7))
print(string8 + " -> " + balance(string8))
