from Trie import Trie
from tkinter import *

trie = Trie()
fileDescriptor = open("words.txt")
words = fileDescriptor.read().split()
trie.formTrie(words)

window = Tk()
window.geometry("410x400")
window.title("پروژه ساختمان داده")
font = ("Times", 24, "bold")


def check(event):
    value = entry.get()
    if value == '':
        data = words

    else:
        trie.autoSuggestions(value.lower())
        data = trie.getSuggestions()
    update(data)


def update(data):
    menu.delete(0, END)
    for value in data:
        menu.insert(END, value)


text = Label(window, text="Enter your query")
text.pack(padx=15, pady=20)
entry = Entry(window, width=35)
entry.pack()
entry.bind('<KeyRelease>',check)
menu = Listbox(window)
menu.pack()

update(words)

window.mainloop()


