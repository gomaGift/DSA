from Trees.BinaryTrees.TreeNode import TreeNode


def max_sum(node: TreeNode) -> int:
    max_sum = node.val

    def path_sum(root: TreeNode):
        nonlocal max_sum

        if not root:
            return 0

        left_max = max(0, path_sum(root.left))
        right_max = max(0, path_sum(root.right))
        max_sum = max(max_sum, root.val+left_max + right_max)

        return root.val + max(left_max, right_max)

    path_sum(node)
    return max_sum