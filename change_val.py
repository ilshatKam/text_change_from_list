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
		#add_round_key.m
    myfile2 = open('add_round_key.m', 'r') # fail v kotorom proizvoditsya zamena
    line2 = myfile2.read()
    line2=line2.replace(a,b)    
    for l in line2:
        print(l, end='')
    myfile2 = open('add_round_key.m', 'w')
    myfile3 = open('dob_kluch_raunda.m', 'w')
    myfile2.write(line2)
    myfile3.write(line2)
		#aes_demo.m
    myfile2 = open('aes_demo.m', 'r') # fail v kotorom proizvoditsya zamena
    line2 = myfile2.read()
    line2=line2.replace(a,b)    
    for l in line2:
        print(l, end='')
    myfile2 = open('aes_demo.m', 'w')
    myfile3 = open('aes_main.m', 'w')
    myfile2.write(line2)
    myfile3.write(line2)
		#aes_init.m
    myfile2 = open('aes_init.m', 'r') # fail v kotorom proizvoditsya zamena
    line2 = myfile2.read()
    line2=line2.replace(a,b)    
    for l in line2:
        print(l, end='')
    myfile2 = open('aes_init .m', 'w')
    myfile3 = open('aes_gen.m', 'w')
    myfile2.write(line2)
    myfile3.write(line2)
myfile1.close()
myfile2.close()
myfile3.close()
#udalenie
os.remove('add_round_key.m')