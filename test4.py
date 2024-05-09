start = 0
end = 1
class EvenNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.i=0
    def __iter__(self):
        self.i=(self.start+1)//2*2-2
        return self
    def __next__(self):
        self.i += 2
        if self.i>=self.start:
                if self.i > self.end:
                    raise StopIteration()
        return self.i

en = EvenNumbers(start=10,end=25)
print('После перебора и вывода:')
for i in en:
    print(i)


