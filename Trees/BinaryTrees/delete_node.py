from typing_extensions import Optional

from Trees.BinaryTrees.TreeNode import TreeNode

#  recursively
def delete_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return root

    if val > root.val:
        root.right = delete_node(root.right, val)
    elif val < root.val:
        root.left = delete_node(root.left, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        curr = root.right
        while curr.left:
            curr = curr.left
        curr.left = root.left
        root = root.right
    return root

# iteratively
def delete_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return root

    curr = root

    while curr:
        if curr.val > val:
            curr = curr.left
        elif curr.val < val:
            curr = curr.right
        else:
            if not curr.left:
                curr = curr.right
                return root
            if not curr.right:
                curr = curr.left
                return root

            holder = curr.right
            while holder.left:
                holder = holder.left
            holder.left = curr.left
            curr = curr.right
            return root
