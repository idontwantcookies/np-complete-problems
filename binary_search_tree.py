from generics import Ordered


class BSTree:
    def __init__(self, value: Ordered):
        self.value: Ordered = value
        self.left: "BSTree | None" = None
        self.right: "BSTree | None" = None
        self.parent: "BSTree | None" = None

    def insert(self, value: Ordered) -> "BSTree":
        if value == self.value:
            return self
        elif value < self.value:
            if self.left: return self.left.insert(value)
            self.left = BSTree(value)
            return self.left
        else:
            if self.right: return self.right.insert(value)
            self.right = BSTree(value)
            return self.right
    
    def find(self, value: Ordered) -> "BSTree | None":
        if value == self.value: return self
        elif value < self.value and self.left: return self.left.find(value)
        elif value > self.value and self.right: return self.right.find(value)
        else: return None
