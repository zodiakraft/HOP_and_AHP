from colorama import init
init()
from colorama import Fore, Back, Style

class drawing():
    def __init__(self, wheel = 0, glass = 0):
        self.wheel = wheel
        self.glass = glass
        self.draw = '''
               $$$$$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$$$$'''
        self.insert()
    
    def insert(self):
        if self.glass == 0:
            self.draw += '''
            $$$$        $$$       $$$
           $$$           $$$         $$$
          $$$$           $$$          $$$$'''
        elif self.glass == 1:
            self.draw += '''
            $$$$////////$$$       $$$
           $$$///////////$$$         $$$
          $$$$///////////$$$          $$$$'''
        elif self.glass == 2:
            self.draw += '''
            $$$$////////$$$///////$$$
           $$$///////////$$$/////////$$$
          $$$$///////////$$$//////////$$$$'''

        self.draw += '''
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$
 $$$$$$$$       $$$$$$$$$$$$$$$$$$$$$       $$$$$$'''

        if self.wheel == 0:
            self.draw += '''
  $$$$$$         $$$$$$$$$$$$$$$$$$$          $$$'''

        elif self.wheel == 1:
            self.draw += '''
  $$$$$$  #####  $$$$$$$$$$$$$$$$$$$          $$$
         ##   ##                              
         ##   ##                              
          ####                             '''

        elif self.wheel == 2:
            self.draw += '''
  $$$$$$  #####  $$$$$$$$$$$$$$$$$$$  #####   $$$
         ##   ##                     ##   ##  
         ##   ##                     ###  ##  
          ####                         ####'''

class coloring(drawing):
    def __init__(self, color = 'BLUE', element = "kuzov"):
        self.color = color
        self.element = element
        self.color_draw = ''''''
        self.colors()
    
    def colors(self):
        if self.element == "kuzov":
            for i in a.draw:
                if i == "$":
                    self.color_draw += Fore.BLUE + '$' + Back.BLUE + '$' + Style.RESET_ALL
                else: self.color_draw += i
        elif self.element == "glass":
            for i in a.draw:
                if i == "/":
                    self.color_draw += Fore.BLUE + '/' + Back.BLUE + '/' + Style.RESET_ALL
                else: self.color_draw += i
        elif self.element == "wheel":
            for i in a.draw:
                if i == "#":
                    self.color_draw += Fore.BLUE + '#' + Back.BLUE + '#' + Style.RESET_ALL
                else: self.color_draw += i


a = drawing(wheel =2, glass = 2)
# print(a.draw)
b = coloring(element='kuzov')
print(b.color_draw)