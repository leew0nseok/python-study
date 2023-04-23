import math

# Product
class MyVector:
    def __init__(self, dim, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        dim = -1
        norm = 0
    
    def normalize(self):
        self.norm = self.getMagnitude()
        self.x = self.x / self.norm
        self.y = self.y / self.norm
        self.z = self.z / self.norm

    def getMagnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y,2) + math.pow(self.z,2))
    
    def getDegree(self):
        return self.dim
    
    def getState(self):
        return self.x, self.y, self.z
    
# Builder
class VectorBuilder:
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.dim = None

    def setDim(self, dim):
        self.dim = dim
        return self

    def setX(self, x):
        self.x = x
        return self
    
    def setY(self, y):
        self.y = y
        return self
    
    def setZ(self, z):
        self.z = z
        return self
    
    def Build(self):
        vector = MyVector(self.dim, self.x, self.y, self.z)
        return vector
    
# Concreate Builder
class VectorBuilder2D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.z = 0
        self.dim = 2

# Concreate Builder
class VectorBuilder3D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.dim = 3

### Client ###
vec2D = VectorBuilder2D().setX(10).setY(20).Build()
print(vec2D.getState())
vec2D.normalize()
print(vec2D.getState())

# Director
class Director:
    def vectorZeros(builder:VectorBuilder):
        builder.setX(0)
        builder.setY(0)
        builder.setZ(0)
    
    def vectorOnes(builder:VectorBuilder):
        builder.setX(1)
        builder.setY(1)
        builder.setZ(1)

### Client ###
builder3D = VectorBuilder3D()
Director.vectorOnes(builder3D)
vec3D = builder3D.Build()

print(vec3D.getState())