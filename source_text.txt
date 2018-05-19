import time
import sys
import os
import re
myfile1 = open('val_swap_list.txt') # spisok osuchestvlyaemih zamen peremennih

while True:
    line = myfile1.readline()
    if len(line) == 0:
        break
    match = re.search("(.*)[ ]+=[ ]+(.*)", line)
    a = match.groups()[0]
    b = match.groups()[1]
    print (repr(a),repr(b))
    myfile2 = open('source_text.txt', 'r') # fail v kotorom proizvoditsya zamena
    line2 = myfile2.read()
    line2=line2.replace(a,b)    
    for l in line2:
        print(l, end='')
    myfile2 = open('source_text.txt', 'w')
    myfile2.write(line2)

myfile1.close()
myfile2.close()
