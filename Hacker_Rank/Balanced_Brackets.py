'''
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is considered to be balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES on a new line; otherwise, print NO on a new line.


'''


class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if (len(self.items) == 0):
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def brackets_match(br1, br2):
    if br1 == '{':
        return br2 == '}'
    if br1 == '(':
        return br2 == ')'
    if br1 == '[':
        return br2 == ']'
    else:
        return False


def is_matched(expression):
    s = stack()
    for e in expression:
        if e == '{' or e == '(' or e == '[':
            s.push(e)
        else:
            if s.is_empty():
                return False
            if not brackets_match(s.pop(), e):
                return False
    return s.is_empty()


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
