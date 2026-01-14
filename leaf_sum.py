#!/usr/bin/env python3

from tree import TreeNode

def leaf_sum(t: TreeNode, k: int) -> bool:
    """
    Given a binary tree t consisting of integers and int k, return true if there is a single 
    root-to-leaf path with the sum k.
    """
    if t.is_leaf():
        return k == t.value
    for child in t.children:
        if leaf_sum(child, k-t.value):
            return True
    return False

t = tree.SAMPLE_TREE_1
rootNode = t.root
print(t)
print(leaf_sum(rootNode, 7))
