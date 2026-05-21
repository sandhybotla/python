# calulate the height of a tree
#   1
#  / \
#  2  3
#  
class node:            
   def __int__(self,data):
      self.data=data
      self.left=None
      self.right=None
def heght(root):
    if not root:
      return 0
    return 1 +max(hegiht(root.left),height(root.right)) 
root=node(int(input("enter root:")))
root=left=node(int(input("enter left:")))
root=right=node(int(input("enter right:"))) 
print("Height level of the tree:",height(root))