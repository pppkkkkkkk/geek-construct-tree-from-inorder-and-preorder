'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        
        def build(inList, preList):
            node = Node(preList[0])
            for i in range(len(inList)):
                if inList[i] == preList[0]:
                    break
            if i>0: 
                node.left = build(inList[0:i], preList[1:i+1])
            if i<len(preList)-1:
                node.right = build(inList[i+1:len(inList)], preList[i+1:len(preList)])
            
            return node
            
        return build(inorder, preorder)
            
            
            
            
            