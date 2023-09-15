#x = 4               #global scope
def fun():
    #x = 4          #local scope
    global x        #type global inside function to make a variable global
    x = 4
    def infun():    #local scope
        print(x)
    infun()
fun()
print(x)
