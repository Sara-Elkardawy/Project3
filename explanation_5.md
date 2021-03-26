Problem 5: Autocomplete with Tries
**********************************************************
Problem Statement:
=================
Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().


Solution:
=========
The trie's implementation is using python dictionary.
**Insert all words in the array to the dictionary, since each word inserted in O(L), where L is the word's length.
Then all the words inserted in O(n*l), where n is the number of words and l is the word length.

** To find the suffixes for any prefix:
  Step 1: Reach the prefix's end node by calling <Find> method.
          Calling <Find> takes O(k) time complexity, where k is the prefix length, because each dictionary lookup takes O(1).
  Step 2: Recurse from the node returned from find method to all levels and add any sub string marked as "is_word". This step takes O(n*m) time complexity in the worse case, where n is the number of words and m is the average number of letters in each word. Because we need to check every character in the sub tree rooted by the prefix end node.


Time complexity:
=================
Time complexity of Finding Suffixes of specific prefix = Time complexity of finding the prefix end node + Time complexity of navigating all paths in the subtree of the root <Prefix end Node>

TC(suffixes) = O(k) + O(n*m) ~= O(n*m)
If we take into account the insert process, then TC(suffixes) = O(2 * n * m)~= O(n*m)

Time complexity is O(n*m), where n is the words list and m is the average number of characters per each word.

Space complexity:
=================
Since the trie's implementation with a dictionary, then the space complexity is O(n*m), where n is the words list and m is the average number of characters per a word.
