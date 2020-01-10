
import Music_reports
import os
import File_manage

def display(head,list):
    os.system('clear')
    print('\n')
    print(head.center(140,' ')+'\n')
    i=1
    for el in list:
        print(' '*55+str(i)+'.>--'+el)
        i+=1
    print(' '*55+'0.>--EXIT')

def display_list(list_of_all, number):
    box = []
    for line in list_of_all:
        if line[number] not in box:
            box.append(line[number])
    return box