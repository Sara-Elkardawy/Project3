#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
#
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
#
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# # Finding Suffixes
#
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
#
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)


#=====================================================================================
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []
        current_suffix = suffix
        for char, trie_node in self.children.items():
            if trie_node.is_word:
                suffixes.append(current_suffix+char)
            suffixes.extend(trie_node.suffixes(current_suffix+char))
        return suffixes

#=====================================================================================
#=====================================================================================

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if word is None or len(word) == 0:
            return None
        current_node = self.root
        for char in word:
            if current_node.children.get(char) is None:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix is None or len(prefix) == 0:
            return None
        current_node = self.root
        for char in prefix:
            if current_node.children.get(char) is None:
                return None
            else:
                current_node = current_node.children[char]

        return current_node

    def get_suffixes(self, prefix):
        prefixNode = self.find(prefix)
        if prefixNode is not None:
            suffixes = prefixNode.suffixes()
            print(f"The suffixes for the prefix '{prefix}' are: {suffixes}")
        else:
            print(f"The node with prefix '{prefix}' NOT FOUND")

    def display_trie(self):
        print("\n{")
        self.display_trie_recursive(self.root,"\t")
        print("}\n")

    def display_trie_recursive(self, node, prefix):
        for key in node.children:
            print("{}'{}' : (".format(prefix,key))
            if len(node.children) > 0:
                self.display_trie_recursive(node.children[key], prefix+"\t")
                print("{}'is_word':{}".format(prefix,node.children[key].is_word))
            print("{}),".format(prefix))
#=====================================================================================
#=====================================================================================

# # Testing it all out
#
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             suffixes = prefixNode.suffixes()
#             print(suffixes)
#             print('\n'.join(suffixes))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');

#=====================================================================================
#=====================================================================================
def test_trie(wordList):
    if wordList is None:
        return
    print(f"\nBuild a TRIE from the wordlist: {wordList}")
    MyTrie = Trie()
    for word in wordList:
        MyTrie.insert(word)
    print("The Trie:")
    MyTrie.display_trie()

    MyTrie.get_suffixes("")
    MyTrie.get_suffixes("a")
    MyTrie.get_suffixes("fu")
    MyTrie.get_suffixes("trig")
    MyTrie.get_suffixes("zoo")
    MyTrie.get_suffixes("th")
    MyTrie.get_suffixes("an")


#=====================================================================================
#=====================================================================================
test_trie(None)

wordList1 = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
test_trie(wordList1)

wordList2 = ["the","a","there","anaswe","any", "by","their"]
test_trie(wordList2)
