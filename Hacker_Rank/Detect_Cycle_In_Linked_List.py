'''\
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided in the editor below.
It has one parameter: a pointer to a Node object named that points to the head of a linked list.
Your function must return a boolean denoting whether or not there is a cycle in the list.
If there is a cycle, return true; otherwise, return false.


'''

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.



A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    one_stepper = head
    two_stepper = head
    while (two_stepper is not None):
        one_stepper = head.next
        if two_stepper.next is not None:
            two_stepper = two_stepper.next.next
        else:
            return 0
        if one_stepper is two_stepper:
            return 1

    return 0

