class AA():
    def __init__(self):
        self.__x = 1

    def a(self):
        return self.__x
    
instance = AA()
assert instance.a() == 1
assert instance._AA__x == 1
