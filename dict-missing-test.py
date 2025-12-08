class MissingDict(dict):
    def __missing__(self, key):
        value = 1
        self[key] = value
        return value
    
testdict = MissingDict()
testdict[1] = 2
print(testdict[2])
print(testdict)