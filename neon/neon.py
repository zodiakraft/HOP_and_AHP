example_code = ''''''

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

print(compiling('output(123);'))