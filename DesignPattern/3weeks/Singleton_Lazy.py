class LazyInstantiation:
    _instance = None
    def __init__(self):
        if not LazyInstantiation._instance:
            print("__init__ method called but notting is created")
        else:
            print("instance already created", self.getInstance())
        
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = LazyInstantiation()
        return cls._instance
    
s = LazyInstantiation()
print(s._instance)
s1 = LazyInstantiation.getInstance()
s2 = LazyInstantiation()