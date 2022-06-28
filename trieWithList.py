class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [False] * 26
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ptr = self.root
        for letter in word:
            if ptr.children[97-ord(letter)]:
                ptr = ptr.children[97-ord(letter)]
            else:
                ptr.children[97-ord(letter)] = TrieNode()
                ptr = ptr.children[97-ord(letter)]
        ptr.isWord = True


    def search(self, word):
        ptr = self.root
        for letter in word:
            if ptr.children[97-ord(letter)]:
                ptr = ptr.children[97-ord(letter)]
            else:
                return False
        return ptr.isWord

    def startsWith(self, prefix):
        ptr = self.root
        for letter in prefix:
            if ptr.children[97-ord(letter)]:
                ptr = ptr.children[97-ord(letter)]
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