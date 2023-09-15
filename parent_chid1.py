from time import sleep
class a(object):
    def __init__(self, some):
        print('Class a is called')
        self.some = some
        print(some)
        sleep(1)
        
class b(a):
    def __init__(self, some):
        print('Class b is called')
        self.some = some
        a.__init__(self, some)      #Calling init function of parent(a) class
        print(some, 'Mitra')
        sleep(1)
    
while True:
    obj = b('Ishan') 
