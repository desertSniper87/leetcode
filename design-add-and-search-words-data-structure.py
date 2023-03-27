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

    def check(self, string, node):
        if string[0] == node.char:
            return self.search(string[1:]. no)

    def search(self, string: str, node=None) -> bool:
        self.output = []
        l = len(string)

        if not node:
            node = self.root


        for i in range(l):
            char = string[i]

            if char == '.':
                for n in node.children:
                    return self.check(string[i+1:], node=node)

            elif char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return False

        return True
        
        #  self.dfs(node, x[:-1])

        #  return sorted(self.output, key=lambda x: x[1], reverse=True)
        


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

    def __str__(self):
        if self.is_end:
            return f'{self.char} {self.is_end}'
        else:
            return self.char


if __name__ == "__main__":
    action = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    words = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

    # action = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    # words = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

    t = WordDictionary()
    res = None

    for (a, w) in zip(action, words):
        print(a, w)
        match a:
            case "WordDictionary":
                t = WordDictionary()
            case "addWord":
                res = t.addWord(*w)
            case "search":
                res = t.search(*w)

        print(res)

    



