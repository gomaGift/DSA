from Trees.BinaryTrees.TreeNode import TreeNode

# recursive
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      curr = root

      # recursive approach
      if max(p.val, q.val) < curr.val:
          return lowest_common_ancestor(curr.left, p, q)
      if min(p.val, q.val) > curr.val:
          return lowest_common_ancestor(curr.right, p, q)
      else:
          return curr

# iterative
def lowest_ancestor_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if max(p.val, q.val) < curr.val:
            curr = curr.left
        elif min(p.val, q.val) > curr.val:
            curr = curr.right
        else:
            return curr




