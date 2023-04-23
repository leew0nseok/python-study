class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Box(metaclass = MetaSingleton):
    pass

b1 = Box()
b2 = Box()

print( b1 is b2)