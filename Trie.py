class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.suggestions = []

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for character in key:
            if not node.children.get(character):
                node.children[character] = TrieNode()
            node = node.children[character]
        node.isWord = True

    def suggestionsRecords(self, node, word):
        if node.isWord:
            self.suggestions.append(word)  # print(word)
        for character, child in node.children.items():
            self.suggestionsRecords(child, word + character)

    def autoSuggestions(self, key):
        node = self.root
        for character in key:
            if not node.children.get(character):
                return 0
            node = node.children[character]
        if not node.children:
            return -1
        self.suggestionsRecords(node, key)
        return 1

    def getSuggestions(self):
        return self.suggestions

