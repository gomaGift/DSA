def is_same_tree(root, sub_root):
    if root is None and sub_root is None:
        return True

    if root and sub_root is None or root is None and sub_root:
        return False

    return root.val == sub_root.val and (is_same_tree(root.left, sub_root.left) and is_same_tree(root.right, sub_root.right))