class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

p = person("Ishan", 11, "Kolkata")
print(p.name, p.address)
