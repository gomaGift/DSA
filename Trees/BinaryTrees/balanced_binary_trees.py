from typing import Optional
from Trees.BinaryTrees.TreeNode import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    def tree_height(node):
        # Base case
        if not node:
            return 0

        left = tree_height(node.left)
        if left == -1:  # if left subtree already unbalanced
            return -1

        right = tree_height(node.right)
        if right == -1:  # if right subtree already unbalanced
            return -1

        if abs(left - right) > 1:
            return -1  # signal imbalance

        return 1 + max(left, right)

    # Start recursion and check signal
    return tree_height(root) != -1



