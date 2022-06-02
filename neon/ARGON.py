from __future__ import print_function
import colorama
import os
from time import sleep

import msvcrt
import time
 

def input_wait(prompt='', timeout=1000, *, _delay=0.02):
    inpute_line = str()
    start = time.time()
    
    while time.time() - start < timeout:
        prompt_t = '\r{:.1f}| {}{}'.format(timeout - time.time() + start,
                                           prompt, inpute_line)
        print(prompt_t, end='')
        
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == '\r':
                msvcrt.putwch('\n')
                break
            elif char == '\000' or char == '\xe0':
                msvcrt.getwch()
                pass
            elif ord(char) == 8: # backspace
                print('\r{}'.format(' ' * len(prompt_t)), end='')
                inpute_line = inpute_line[:-1]
            else:
                inpute_line += char
        else:
            time.sleep(_delay)
    else:
        inpute_line = None
    
    return inpute_line
    

WIDTH = 1440
HEIGHT = 900

while True:
    os.system('cls||clear')

    print('#'*int(WIDTH/7.1))

    colorama.init()

    # # ESC [ n A       # move cursor n lines up
    # # ESC [ n B       # move cursor n lines down

    cursor_up = lambda lines: '\x1b[{0}A'.format(lines)
    cursor_down = lambda lines: '\x1b[{0}B'.format(lines)

    lines_up = 3
    print(cursor_up(lines_up), end='')
    sleep(1)
    print("woof", " " * 10)
    sleep(1)
    lines_down = 1
    sleep(1)
    print(cursor_down(lines_down), end='')
    sleep(1)
    print("woof-woof-woof", " " * 10)
    sleep(1)
    lines_up = 2
    sleep(1)
    print(cursor_up(lines_up), end='')
    print("woof-woof", " " * 10)
    sleep(1)
    
    timeout = 10
    prompt = 'Enter answer: '
    
    print('Сколько будет 5 + 5?')
    print('у вас есть 10 секунд')
    
    while True:
        answer = input_wait(prompt, timeout=timeout)
        
        if answer is None:
            print('\nTime is up')
        else:
            if answer == '10':
                print("It's right answer!")
            elif answer == 'q':
                print('exit...')
                break        
            else:
                print("No! Try again.")