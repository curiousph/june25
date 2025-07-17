# This program returns the preorder traversal of a binary tree's nodes' values.

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    """
    Returns a list of values representing the preorder traversal of the binary tree.
    Preorder: root -> left -> right
    """
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)    # Visit root
        dfs(node.left)             # Traverse left subtree
        dfs(node.right)            # Traverse right subtree
    dfs(root)
    return result

# Example usage and test cases
if __name__ == "__main__":
    # Construct the following binary tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1,
        left=TreeNode(2, TreeNode(4), TreeNode(5)),
        right=TreeNode(3)
    )
    print("Preorder traversal:", preorder_traversal(root))  # Output: [1, 2, 4, 5, 3]