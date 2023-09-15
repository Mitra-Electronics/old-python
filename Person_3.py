class person:
    def __init__(Tushan, name, age, address):
        Tushan.name = name
        Tushan.age = age
        Tushan.address = address
    def myfunc(Tushan):
        print('The name of the person is', Tushan.name)

p = person("Ishan", 11, "Kolkata")
#print(p.name, p.address)
#p.myfunc()
del p
print(p.age)
