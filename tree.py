import random
from typing import Self

class Tree:
    """
    Flexible tree structure that can be used to represent a variety of cases.
    """
    def __init__(self, root) -> None:
        self.root = root

    def __str__(self):
        return str(self.root)

    @classmethod 
    def random_binary_tree(cls, n: int):
        """
        Generates a random binary tree of size n using integers as the value from 0, ... n-1
        """
        return cls(TreeNode.random_binary_tree(0, n-1))


class TreeNode:
    """
    Defines a TreeNode for use in a Tree. The value stored can be flexible (int, str, e.t.c.)
    """
    def __init__(self, value, children: list[Self] = []) -> None:
        self.value = value
        self.children = children

    def is_leaf(self):
        """
        Returns True if this node is a leaf, False otherwise.
        """
        return self.children == []

    def is_binary(self):
        """
        Returns True if this node and all subnodes are binary nodes (i.e. at most two children)
        """
        if len(self.children) > 2:
            return False
        for child in self.children:
            if not child.is_binary:
                return False
        return True

    def to_string(self, prefix: str, is_last: bool) -> str:
        """
        Returns a string representation of the node. prefix represents the 
        Final nodes should use └─ character, otherwise ├─ is used.
        """
        if is_last:
            prefix += '  '
        else:
            prefix += '| '

        s = prefix 
        if is_last:
            s += '└─ '
        else:
            s += '├─ '
        s += str(self.value) + '\n'
        for i, child in enumerate(self.children):
            s += child.to_string(prefix, i == len(self.children) - 1)
        return s

    def __str__(self):
        return self.to_string(' ', True)

    @classmethod
    def random_binary_tree(cls, n:int, m:int):
        """
        Generates a random tree with integers n, ..., m as the values. Tree is not guarenteed to be balanced.
        """
        # leaf node
        if n == m:
            return cls(n)

        val = random.randint(n, m)
        children = []
        if val != n:
            children.append(cls.random_binary_tree(n, val-1))
        if val != m:
            children.append(cls.random_binary_tree(val+1, m))
        return cls(val, children)

def main():
    print(Tree.random_binary_tree(10))

if __name__ == '__main__':
    main()
