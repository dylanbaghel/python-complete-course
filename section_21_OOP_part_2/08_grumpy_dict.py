class GrumpyDict(dict):
    def __repr__(self):
        print("None Of Your Buisness")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOu Want {key}? Well It ain't Here")
    
    def __setitem__(self, key, value):
        print("You Want To Change The Dictionary")
        print("OK Fine...")
        super().__setitem__(key, value)

data = GrumpyDict({"first": "Abhishek", "age": 21})
print(data)
data['city'] = 'Tokyo'
print(data)