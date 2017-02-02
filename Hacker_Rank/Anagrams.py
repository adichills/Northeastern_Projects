'''

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Sample Input

cde
abc
Sample Output

4

'''
def number_needed(a, b):
    a_dict={}
    b_dict={}
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for alp in alphabets:
        a_dict[alp] = 0
        b_dict[alp] = 0
    for c in a:
        a_dict[c] = a_dict[c]+1
    for c in b:
        b_dict[c] = b_dict[c]+1
    number = 0
    for alp in alphabets:
        number = number + (max(a_dict[alp],b_dict[alp]) - min(a_dict[alp],b_dict[alp]))
    return number
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
