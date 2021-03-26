# HTTPRouter using a Trie
# For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.
#
# There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.
#
# The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
# In a dynamic web server, the content will often come from a block of code called a handler.
#
#
# First we need to implement a slightly different Trie than the one we used for autocomplete.
# Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
#
# In addition to a path though, we need to know which function will handle the http request.
# In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path.
# For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
#
# We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site.
# A more sensible way to split things would be on the parts of the path that are separated by slashes ("/").
# A Trie with a single path entry of: "/about/me" would look like:
#
# (root, None) -> ("about", None) -> ("me", "About Me handler")
#
# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
# We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

# Next we need to implement the actual Router.
#  The router will initialize itself with a RouteTrie for holding routes and associated handlers.
#   It should also support adding a handler by path and looking up a handler by path.
#    All of these operations will be delegated to the RouteTrie.
#
# Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
#
# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
#
# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
#==============================================================================================================================
#==============================================================================================================================
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, word, handler = None):
        # Insert the node as before
        self.children[word] = RouteTrieNode(handler)
#==============================================================================================================================
#==============================================================================================================================
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, path_list, path_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for word in path_list:
            if current_node.children.get(word) is None:
                current_node.insert(word, self.not_found_handler)
            current_node = current_node.children[word]
        current_node.handler = path_handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(path_list)==0:
            return self.root.handler
        current_node = self.root
        for word in path_list:
            if current_node.children.get(word) is None:
                return self.not_found_handler
            current_node = current_node.children[word]
        return current_node.handler

    def display_trie(self):
        print("\n******************************************************\n( root handler = '{}'".format(self.root.handler))
        self.__display_trie_recursive__(self.root,"\t")
        print(")\n")

    def __display_trie_recursive__(self, node, prefix):
        for key in node.children:
            print("{}'{}' , its handler = '{}': (".format(prefix,key, node.children[key].handler))
            if len(node.children) > 0:
                self.__display_trie_recursive__(node.children[key], prefix+"\t")
            print("{}),".format(prefix))
#==============================================================================================================================
#==============================================================================================================================

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path_str, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        # as a list to the RouteTrie
        if path_handler is None:
            print(f"Failure to add the handler: <'{path_handler}'>")
            return
        if path_str == None:
            print(f"Failure to add the handler: <'{path_handler}'> to a <NONE> path")
            return
        self.route_trie.insert(self.split_path(path_str), path_handler)

    def lookup(self, path_str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path_str == None:
            print(f"Failure to lookup a <NONE> path")
            return
        return self.route_trie.find(self.split_path(path_str))

    def split_path(self, path_str):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_str.replace("//", "/")
        path_list = path_str.split('/')
        return [str for str in path_list if str] #to eliminate any empty string

#==============================================================================================================================
#==============================================================================================================================
#Test Cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

router.route_trie.display_trie()

# some lookups with the expected output
print("The handler for the path '{}' is: '{}'".format("",router.lookup(""))) # should print 'root handler'
print("The handler for the path '{}' is: '{}'".format("/",router.lookup("/"))) # should print 'root handler'
print("The handler for the path '{}' is: '{}'".format("//",router.lookup("//"))) # should print 'root handler'
print("The handler for the path '{}' is: '{}'".format("/home",router.lookup("/home"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("/home/",router.lookup("/home/"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("home/",router.lookup("home/"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("home",router.lookup("home"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("/home/about",router.lookup("/home/about"))) # should print 'about handler'
print("The handler for the path '{}' is: '{}'".format("/home//about",router.lookup("/home//about"))) # should print 'about handler'
print("The handler for the path '{}' is: '{}'".format("/home/about/",router.lookup("/home/about/"))) # should print 'about handler' or None if you did not handle trailing slashes
print("The handler for the path '{}' is: '{}'".format("/home/about/me",router.lookup("/home/about/me"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("/home/about/me/",router.lookup("/home/about/me/"))) # should print 'not found handler' or None if you did not implement one
print("The handler for the path '{}' is: '{}'".format("/home/about/about",router.lookup("/home/about/about"))) # should print 'not found handler'


router.add_handler('/', 'home')
router.add_handler('/udacity', 'udacity')
router.add_handler('udacity/courses/nd/', 'data structures and algorithms')
router.route_trie.display_trie()
print("The handler for the path '{}' is: '{}'".format("/udacity/",router.lookup("/udacity"))) # should print 'udacity'
print("The handler for the path '{}' is: '{}'".format("udacity/",router.lookup("udacity/"))) # should print 'udacity'
print("The handler for the path '{}' is: '{}'".format("udacity",router.lookup("udacity"))) # should print 'udacity'
print("The handler for the path '{}' is: '{}'".format("udacity/courses/",router.lookup("udacity/courses/"))) # should print 'not found handler'
print("The handler for the path '{}' is: '{}'".format("udacity/courses/nd//",router.lookup("udacity/courses/nd//"))) # should print 'data structures and algorithms'
print("The handler for the path '{}' is: '{}'".format("udacity/courses/nds/",router.lookup("udacity/courses/nds/"))) # should print 'not found handler'
print("The handler for the path '{}' is: '{}'".format("s/",router.lookup("s/"))) # should print 'not found handler'

#edge cases

print("\nAdd a <None> path and a <None> handler")
router.add_handler(None, None)
print("\nAdd a <empty> path and a <None> handler")
router.add_handler('', None)
print("\nAdd a <None> path and a <empty> handler")
router.add_handler(None, '')
print("\nAdd a <empty> path and a <empty> handler")
router.add_handler('', '')

router.route_trie.display_trie()

print("The handler for the path '{}' is: '{}'".format("None",router.lookup(None))) # should print failure/none

print("The handler for the path '{}' is: '{}'".format("",router.lookup(""))) # should print None


router.add_handler('about/me', 'About Me handler')
print("\nAdding about/me handler:")
router.route_trie.display_trie()
print("The handler for the path '{}' is: '{}'".format("about/me",router.lookup("about/me")))
print("\n")
