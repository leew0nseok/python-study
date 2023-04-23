class MonoState:
    __shard_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shard_state
        pass

ms1 = MonoState()
ms2 = MonoState()

print(ms1)
print(ms2)

print(ms1 == ms2)

ms2.x = 10
print(ms1.x)
print(ms2.x)

print(ms1 is ms2)