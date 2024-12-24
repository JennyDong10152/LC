#Iterative Traversals
def preorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorderTraversal(root):
    stack = []
    result = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def postorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push left first, then right to process right first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    # Reverse the result since we collected Root → Right → Left
    return result[::-1]

#For binary trees
# successor: the smallest node after the current one; one step right and go all the way left
# predecessor: the largest node before the current one; one step left and go all the way right
def successor(root: TreeNode) -> TreeNode:
    root = root.right
    while root.left:
        root = root.left
    return root

def predecessor(root: TreeNode) -> TreeNode:
    root = root.left
    while root.right:
        root = root.right
    return root