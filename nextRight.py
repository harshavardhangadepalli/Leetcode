"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        d = dict()
        if not root:
            return root
        i = 0
        d[i] = list()
        d[i].append(root)
        while True:
            if i in d:
                for item in d[i]:
                    if item.left or item.right:
                        if i+1 in d:
                            if item.left:
                                d[i+1].append(item.left)
                            if item.right:
                                d[i+1].append(item.right)
                        else:
                            d[i+1] = list()
                            if item.left:
                                d[i+1].append(item.left)
                            if item.right:
                                d[i+1].append(item.right)
            else:
                break
            i += 1

        # the dictionary has all levels in order from left to right
        key = 1
        while key in d:
            for i in range(len(d[key])):
                if i+1 < len(d[key]):
                    d[key][i].next = d[key][i+1]
            key += 1
        return root