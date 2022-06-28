class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False
        for i in 'abcdefghijklmnopqrstuvwxyz':
            self.children[i] = None
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ptr = self.root
        for letter in word:
            if ptr.children[letter]:
                ptr = ptr.children[letter]
            else:
                ptr.children[letter] = TrieNode()
                ptr = ptr.children[letter]
        ptr.isWord = True


    def search(self, word):
        ptr = self.root
        for letter in word:
            if ptr.children[letter]:
                ptr = ptr.children[letter]
            else:
                return False
        return ptr.isWord

    def startsWith(self, prefix):
        ptr = self.root
        for letter in prefix:
            if ptr.children[letter]:
                ptr = ptr.children[letter]
            else:
                return False
        return True

trieTree = Trie()
print(trieTree.insert('apple'))
print(trieTree.search('apple'))
print(trieTree.search('app'))
print(trieTree.startsWith('app'))
print(trieTree.insert('app'))
print(trieTree.search('app'))
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)