"""
Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents
this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before
their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array
postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will
be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove
the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a
binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to
operands (numbers), and internal nodes (nodes with two children) correspond to the
operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations
are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able
to support additional operators without making changes to your existing evaluate implementation?

Example:
Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.
Note: Visualize to understand

Tag: 1628/2927 , R1724/2935 , R42/50 (amz)
Note: Programs runs but produces wrong output, debug and fix it.
"""

from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        else:
            return self.left.evaluate()


class TreeBuilder(object):
    def build_tree(self, postfix: list[str]) -> 'Node':
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur


def main():
    postfix_string = ["3", "4", "+", "2", "*", "7", "/"]
    tree_builder = TreeBuilder()
    exp_tree = tree_builder.build_tree(postfix_string)
    print(exp_tree.evaluate())


if __name__ == "__main__":
    main()
