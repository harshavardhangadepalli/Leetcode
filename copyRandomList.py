"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        #all the items with key of index
        indices = dict()
        #all items with the object as key and index as value
        items = dict()
        #all randoms, if random there or not(Boolean)
        r = dict()
        #will have the new list
        new_list = list()
        i = 0
        indices[i] = head
        items[head] = i
        r[head] = head.random

        curr_node = head
        i+=1
        while curr_node.next:
            curr_node = curr_node.next
            indices[i] = curr_node
            items[curr_node] = i
            r[curr_node] = curr_node.random
            i+=1
        for i in range(len(indices)):
            new_list.append(Node(indices[i].val))
        for i in range(len(new_list)):
            if r[indices[i]]:
                new_list[i].random = new_list[items[indices[i].random]]
        for i in range(len(new_list)-1):
            new_list[i].next = new_list[i+1]
        #print(new_list)
        return new_list[0]