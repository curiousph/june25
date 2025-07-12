# This program checks if a binary tree is height-balanced.
# A binary tree is balanced if the heights of the two child subtrees of any node differ by no more than one.

class TreeNode:
    """Node class for a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    """
    Returns True if the binary tree rooted at 'root' is balanced, False otherwise.
    """
    def check(node):
        if not node:
            return 0  # Height of empty subtree is 0
        left_height = check(node.left)
        if left_height == -1:
            return -1  # Left subtree is not balanced
        right_height = check(node.right)
        if right_height == -1:
            return -1  # Right subtree is not balanced
        if abs(left_height - right_height) > 1:
            return -1  # Current node is not balanced
        return max(left_height, right_height) + 1  # Height of current subtree

    return check(root) != -1

# Example usage and test cases
if __name__ == "__main__":
    # Balanced tree example
    root1 = TreeNode(1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3)
    )
    print("Tree 1 is balanced:", is_balanced(root1))  # Should print True

    # Unbalanced tree example
    root2 = TreeNode(1,
        left=TreeNode(2, left=TreeNode(3, left=TreeNode(4)))
    )
    print("Tree 2 is balanced:", is_balanced(root2))  # Should print False