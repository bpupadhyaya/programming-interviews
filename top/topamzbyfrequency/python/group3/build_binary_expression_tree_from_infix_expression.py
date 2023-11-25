"""
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a
binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to
operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-'
(subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression it represents is (A o B), where A is the expression
the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above,
and parentheses '(' and ')'.

Return any valid binary expression tree, whose in-order traversal reproduces s after omitting the parenthesis from it.

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated
first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

Example 1:
Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.

Example 2:
Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Note: Visualize to understand
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis.
The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid
answer because it does not evaluate to the same value.

The third tree below (visualization) is also not valid. Although it produces the same result and is equivalent to the
above trees, its inorder traversal does not produce s and its operands are not in the same order as s.

Example 3:
Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.

Tag: 1597/2927 , R1777/2935 , R44/50 (amz)
"""
import collections


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def parse_factor(tokens) -> 'Node':
    if tokens[0] == '(':
        tokens.popleft()    # consume '('
        node = parse_expression(tokens)
        tokens.popleft()    # consume ')'
        return node
    else:
        # Single operand
        token = tokens.popleft()
        return Node(val=token)


def parse_term(tokens) -> 'Node':
    lhs = parse_factor(tokens)
    while len(tokens) > 0 and tokens[0] in ['*', '/']:
        op = tokens.popleft()
        rhs = parse_term(tokens)
        lhs = Node(val=op, left=lhs, right=rhs)
    return lhs


def parse_expression(tokens) -> 'Node':
    lhs = parse_term(tokens)
    while len(tokens) > 0 and tokens[0] in ['+', '-']:
        op = tokens.popleft()
        rhs = parse_term(tokens)
        lhs = Node(val=op, left=lhs, right=rhs)
    return lhs


def exp_tree(s: str) -> 'Node':
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]

    tokens = collections.deque(list(s))
    return parse_expression(tokens)


def main():
    s = "3*4-2*5"
    node = exp_tree(s)
    # Print in-order traversal
    print(node.val, node.left.val, node.right.val, node.left.left.val, node.left.right.val, node.right.left.val,
          node.right.right.val)


if __name__ == "__main__":
    main()


"""
Note on implementation:
standard expression parser implementation where you call parse-functions on those with the lowest precendence 
and recursively invoke parse-functions of things with higher precendence.

     Standard parser implementation based on this BNF
       s := expression
       expression := term | term { [+,-] term] }
       term := factor | factor { [*,/] factor] }
       factor :== digit | '(' expression ')'
       digit := [0..9]
    
"""