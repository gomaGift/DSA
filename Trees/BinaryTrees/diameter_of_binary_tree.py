from Trees.BinaryTrees.TreeNode import TreeNode


def diameter_of_bt(root: TreeNode) -> int:
    diameter = 0

    def height(node):
        if not node:
            return 0
        nonlocal diameter
        left_height = height(node.left)
        right_height = height(node.right)

        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter
