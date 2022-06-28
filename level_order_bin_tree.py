class Solution:
    def levelOrder(self, root):
        d = dict()
        if root == None:
            return list()
        i = 0
        d[i] = list()
        d[i].append(root)
        while True:
            if i in d:
                for item in d[i]:
                    if item.left or item.right:
                        # if item has at least one child, append the child to the next level
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

        i = 0
        ret = []
        while i in d:
            temp = []
            for item in d[i]:
                temp.append(item.val)
            ret.append(temp)
            i += 1
        return ret