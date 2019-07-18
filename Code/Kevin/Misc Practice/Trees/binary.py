class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
root = Node("Video Games")

root.left = ("Shooters")
root.left.left = ("1st Person")
# root.left.left.left = ("Halo")
# root.left.left.right = ("Call of Duty")


root.left.right = ("3rd Person")
# root.left.right.left = ("Borderlands")
# root.left.right.right = ("Gears of War")

root.right = ("Role-Playing")
root.right.left = ("J-RPG")
# root.right.left.left = ("Final Fantasy")

root.right.right = ("W-RPG")
# root.right.right.left = ("Fallout")
# root.right.right.right = ("Mass Effect")







