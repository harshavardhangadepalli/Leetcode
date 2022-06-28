class Solution:
    def isValidBST(self, root):
        l = list()

        def is_sorted(list):
            if (list == sorted(list)):
                return True
            else:
                return False

        def has_duplicates(l):
            if len(l) == len(set(l)):
                return False
            return True

        def recursion(root):
            if root == None:
                return
            recursion(root.left)
            l.append(root.val)
            recursion(root.right)
        recursion(root)
        if has_duplicates(l):
            return False
        return(is_sorted(l))
