from Trie import Trie

trie = Trie()
fileDescriptor = open("words.txt")
words = fileDescriptor.read().split()
trie.formTrie(words)
compare = trie.autoSuggestions(input("Enter your query: ").lower())
suggestions = trie.getSuggestions()

counter = 0
for suggestion in suggestions:
    print(suggestion, end="\t")
    counter += 1
    if counter == 3:
        print()
        counter = 0
