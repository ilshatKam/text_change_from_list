import time
import sys
import os
import re
myfile1 = open('val_swap_list.txt') # spisok osuchestvlyaemih zamen peremennih
myfile1_1 = open('val_swap_list.txt') # spisok osuchestvlyaemih zamen peremennih
while True:
    len_check = False
    line = myfile1.readline()
    if len(line) == 0:
        break
    match = re.search("(.*)[ ]+=[ ]+(.*)", line)
    a = match.groups()[0]+'.m'
    b = match.groups()[1]+'.m'
    print (repr(a),repr(b))
		#stage2
    if (os.path.isfile(a) == True):
        print ('__________________________________________________________________________________________________',len_check)
        myfile1_1.seek(0)
        while len_check == False:
            newline = myfile1_1.readline()
            if len(newline) == 0:
                len_check = True
            else:
                match2 = re.search("(.*)[ ]+=[ ]+(.*)", newline)
                c = match2.groups()[0]
                d = match2.groups()[1]
                print ('stage 2:',repr(c),repr(d))
                myfile2 = open(a, 'r') # fail v kotorom proizvoditsya zamena
                line2 = myfile2.read()
                line2=line2.replace(c,d)    
                for l in line2:
                    print(l, end='')
                myfile2 = open(a, 'w')
                myfile3 = open(b, 'w')
                myfile2.write(line2)
                myfile3.write(line2)	
        myfile2.close()
        myfile3.close()
        os.remove(a)
myfile1.close()

#udalenie
#os.remove('add_round_key.m')