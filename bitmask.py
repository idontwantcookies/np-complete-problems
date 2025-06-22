class Bitmask:
    def __init__(self, size: int, mask: int = 0):
        self.mask = mask
        self.size = size

    def check_index(self, i):
        if not (0 <= i < self.size):
            raise ValueError(f"Index {i} out-of-bounds (0, {self.size}).")

    def __getitem__(self, i: int) -> bool:
        self.check_index(i)
        return bool((self.mask >> i) & 1)
    
    def __setitem__(self, i: int, b: bool):
        self.check_index(i)
        if b:
            self.mask |= (1 << i)
        else:
            self.mask &= ~(1 << i)
        
    def flip(self, i):
        self.check_index(i)
        self.mask ^= (1 << i)
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        s = bin(self.mask).replace("0b", "").zfill(self.size)[::-1]
        return f"Bitmask({self.size}): {s}"
    
    def count(self):
        return self.mask.bit_count()
    
    def copy(self):
        return self.__class__(self.size, self.mask)
