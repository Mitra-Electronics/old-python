class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def myfunc(self):
        print('The name of the person is', self.name)
        
#p = person("Ishan", 11, "Kolkata")
#del p.address
#del p.age
class Student(person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


  def welcome(self):
    print("Welcome", self.firstname, self.lastname)

x = Student("Ishan", "Mitra")
x.welcome()


        
#print(p.name, p.address)
#p.myfunc()
#del p
#print(p.age)
