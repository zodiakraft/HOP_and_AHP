code = '''output('Hello, Architect!');
'''

def compiling(code):
    a = []
    code = code.replace('(', ';').replace(')', ';').replace('\'', ';').replace('"', ';')
    for i in code.split(';'):
        a.append(i)
    while True:
        try:
            a.remove('\n')
        except:
            try:
                a.remove('')
            except:
                break

    for i in range(len(a)):
        if a[i] == 'output':
            return a[i+1]

print(compiling('output(\'Hello!\');'))
