# This program finds the minimum depth of a binary tree.
# The minimum depth is the number of nodes along the shortest path from the root to the nearest leaf node.

class TreeNode:
    """Node class for a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    """
    Returns the minimum depth of the binary tree rooted at 'root'.
    """
    if not root:
        return 0
    # If one child is None, recurse only on the other child
    if not root.left and not root.right:
        return 1
    if not root.left:
        return min_depth(root.right) + 1
    if not root.right:
        return min_depth(root.left) + 1
    # If both children exist, take the minimum of both depths
    return min(min_depth(root.left), min_depth(root.right)) + 1

# Example usage and test cases
if __name__ == "__main__":
    # Tree:      1
    #          /   \
    #         2     3
    #        /
    #       4
    root1 = TreeNode(1,
        left=TreeNode(2, left=TreeNode(4)),
        right=TreeNode(3)
    )
    print("Minimum depth of Tree 1:", min_depth(root1))  # Should print 2

    # Tree:      1
    #          /
    #         2
    #        /
    #       3
    root2 = TreeNode(1,
        left=TreeNode(2, left=TreeNode(3))
    )
    print("Minimum depth of Tree 2:", min_depth(root2))  # Should print 3

    # Empty tree
    print("Minimum depth of empty tree:", min_depth(None))  #