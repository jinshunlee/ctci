class TreeNode:
    def __init__(self, data, left=None, right=None, height=0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height
    
    def __str__(self):
        string = "("
        if self.left:  
            string += str(self.left)
        string += str(self.data)
        if self.right: 
            string += str(self.right)
        return string + ")"