from typing import Optional

from Trees.BinaryTrees.TreeNode import TreeNode

# recursively
def insert_val_binary_tree(root: TreeNode, val: int) -> Optional[TreeNode]:

      if not root:
          return TreeNode(val)

      if val > root.val:
          root.right = insert_val_binary_tree(root.right, val)
      else:
          root.left = insert_val_binary_tree(root.left, val)

      return root



# iteratively`
def insert_iteratively(root: TreeNode, val: int) -> Optional[TreeNode]:
    curr = root

    while curr:
        if val > curr:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(val)
                return root
        else:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(val)
                return root
