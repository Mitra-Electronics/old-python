import time
class num:
    def __iter__(self):
        self.n1 = 1
        return self
    def __next__(self):
        n2 = self.n1
        self.n1 += 1
        return n2

numbers = num()
iteration = iter(numbers)

while True:
    print(next(iteration))
    time.sleep(0.5)
