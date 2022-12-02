class vector2d:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __str__(self):
        return f"{self.i}i + {self.j}j"


class  vector3d(vector2d):
    
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
v2d = vector2d(6, 4)        
v3d = vector3d(4, 5, 11)
print(v2d)
print(v3d)

