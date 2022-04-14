example_code = '''output(123);'''

def output(code):
    return code

def compiling(code):
    a = []
    code = code.replace('(', ';').replace(')', ';').replace('\'', ';').replace('"', ';')
    for i in code.split(';'):
        a.append(i)
    while '\n' in a: a.remove('\n')
    while '' in a: a.remove('')

    print(a)

    for i in range(len(a)):
        if a[i] == 'output':
            return output(a[i+1])

print(compiling(example_code))


'''
genome GenomeName():
    def __init__(self, donor = None):
        self.fib1 = 1
        self.fib2 = 1
        self.fib_sum = 0
        self.i = 0
        
    def __inject__(self):
        while self.i < a - 2:
            self.fib_sum = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = self.fib_sum
            self.i += 1
            

a = 5

b = GenomeName()
b.inject(a)

 
print(b)
'''