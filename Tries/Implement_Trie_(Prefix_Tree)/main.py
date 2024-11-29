

# Prefix Tree (Hash Map)
# time complexity: O(n) for each function call
# space complexity: O(t)
class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        
# test
prefixTree = PrefixTree()
prefixTree.insert("apple")
print(prefixTree.search("apple")) # expect True
print(prefixTree.search("app")) # expect False
print(prefixTree.startsWith("app")) # expect True
prefixTree.insert("app")
print(prefixTree.search("app")) # expect True
print(prefixTree.startsWith("app")) # expect True
prefixTree.insert("app")
print(prefixTree.search("app")) # expect True
print(prefixTree.startsWith("app")) # expect True
