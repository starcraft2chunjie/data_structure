#Construct a tree
class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)

#Create a tree
left = Tree(2)
right = Tree(3)
tree1 = Tree(4, left, right)

#A expression tree
tree2 = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

#preorder
def print_tree_prefix(tree):
    if tree is None:
        return
    print(tree.cargo, end = ' ')
    print_tree_prefix(tree.left)
    print_tree_prefix(tree.right)

#postorder
def print_tree_postorder(tree):
    if tree is None:
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end = ' ')
#infix
def print_tree_infix(tree):
    if tree is None:
        return
    print_tree_infix(tree.left)
    print(tree.cargo, end = ' ')
    print_tree_infix(tree.right)


#indented print the element of tree
def  print_tree_indented(tree, level = 0):
    if tree is None:
        return
    print_tree_indented(tree.right, level + 1)
    print(' ' * level + str(tree.cargo))
    print_tree_indented(tree.left, level + 1)




""" application example"""
#Building the expression tree
#given a expression like (3 + 7) * 9, try to yield the expression tree

#compares the expected token to the first token on the list
def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

#handle operands, if the next token in token_list is a number, the function removes it and returns a leaf
#node containing the number
def get_number(token_list):
    X = token_list[0]
    if type(X) != type(0): return None
    del token_list[0]
    return Tree(X, None, None)

#When considering the existance of parienthess, the get_number code should be modified like this

def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise ValueError('Missing close parenthesis')#handling errors
        return x
    else:
        x = token_list[0]
        if type(x) != type(0):return None
        del token_list[0]
        return Tree(x, None, None)


#Build an expression tree for products, needs two number as operands, like 3 * 7
#here is the simple version and the compound version
def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_number(token_list)
        return Tree('*', a, b)

#If you want something compound like 3 * 7 * 8

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a


#To parse sum, just feel free to view the get_product as the get_number(actually it really is a number 
# in essential)
def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree('+', a, b)
    return a
"""
An animal tree, the program starts at the top of the tree and ask the first question, depending on the 
answer, It moves to the left or right child and continues untill it gets to a leaf node, then it makes a
guess, if the answer is wrong, it will ask a question to distinguish the guess from the new animal.Then
it adds a node to the tree with the new question and the new animal
"""
def yes(ques):
    ans = input(ques).lower()
    return ans[0] == 'y'











