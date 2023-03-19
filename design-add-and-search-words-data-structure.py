from typing import List

class WordDictionary:
    def __init__(self):
        self.root = TrieNode("")
        
    def addWord(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True
        node.counter += 1

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def search(self, x: str) -> List:
        self.output = []
        node = self.root
        
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


if __name__ == "__main__":
    


