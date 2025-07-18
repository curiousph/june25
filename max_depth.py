# This program returns the maximum depth of a binary tree.
# The maximum depth is the number of nodes along the longest path from the root to a leaf.

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Returns the maximum depth of the binary tree rooted at 'root'.
    """
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

# Example usage and test cases
if __name__ == "__main__":
    # Construct the following binary tree:
    #     1
    #    / \
    #   2   3
    #  / 
    # 4   
    root = TreeNode(1,
        left=TreeNode(2, left=TreeNode(4)),
        right=TreeNode(3)
    )
    print("Maximum depth of the tree:", max_depth(root))  # Output: 3

    # Empty tree
    print("Maximum depth of empty tree:", max_depth(None))  #