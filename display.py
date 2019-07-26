
import music_reports
import os



list_of_all = []                                                        # Wyciąga tekst z pliku i wrzuca do list
file_base = open('text_albums_data.txt','r')
for line in file_base.readlines():
        list_of_all.append(line.rstrip().split(','))
file_base.close()

def display_list(list_of_all):
    box = []
    for line in list_of_all:
        if line[3] not in box:
            box.append(line[3])
        else:
            pass
    return box

os.system('clear')
active = True
while active:
    def display(a,b,c,d,e,f,g,h,i,j,k,l,m):
        print()
        print(a.center(140,' ')+'\n')
        print(' '*60+b)
        print(' '*60+c)
        print(' '*60+d)
        print(' '*60+e)
        print(' '*60+f)
        print(' '*60+g)
        print(' '*60+h)
        print(' '*60+i)
        print(' '*60+j)
        print(' '*60+k)
        print(' '*60+l)
        print(' '*60+m)
        
    display('MENU','','1.>--SHOW ALL ALBUMS','2.>--SELECT BY GENRE','3.>--SELECT BY TIMEs','4.>--SELECT BY ARTIST','5.>--SELECT BY ALBUM','6.>--SELECT BY LONGEST/SHORTEST','','','','','')
    select = input()
    if select == '1':
        os.system('clear')
        music_reports.all_albums(list_of_all)
    elif select == '2':
        os.system('clear')
        box = []
        for line in list_of_all:
            if line[3] not in box:
                box.append(line[3])
        display('SELECT BY GENRE','','','1.>--'+box[0],'2.>--'+box[1],'3.>--'+box[2],'4.>--'+box[3],'0.>--EXIT','','','','','')
        music_reports.albums_by_genre(box,list_of_all)
    elif select == '3':
        os.system('clear')
        display('SELECT BY TIMEs','','','1.>--60','2.>--70','3.>--80','4.>--90','5.>--2000','6.>--2010','7.>--Oldest','0.>--EXIT','','')
        music_reports.albums_time_range()
    elif select == '4':
        os.system('clear')
        box = []
        for line in list_of_all:
            if line[0] not in box:
                box.append(line[0])
            else:
                print('WRONG SELECT'.center(140,' '))
        display('SELECT BY ARTIST','1.>--'+box[0],'2.>--'+box[1],'3.>--'+box[2],'4.>--'+box[3],
        '5.>--'+box[4],'6.>--'+box[5],'7.>--'+box[6],'8.>--'+box[7],'9.>--'+box[8],'10.>--'+box[9],'0.>--EXIT','')
        music_reports.albums_created_by_artist(box,list_of_all)
    elif select == '5':
        os.system('clear')
        box = []
        for line in list_of_all:
            if line[1] not in box:
                box.append(line[1])
            elif select == '0':
                pass
            else:
                print('WRONG SELECT'.center(140,' '))
        display('SELECT BY ALBUM','1.>--'+box[0],'2.>--'+box[1],'3.>--'+box[2],'4.>--'+box[3],
        '5.>--'+box[4],'6.>--'+box[5],'7.>--'+box[6],'8.>--'+box[7],'9.>--'+box[8],'10.>--'+box[9],'11.>--'+box[10],'0.>--EXIT',)
        music_reports.find_album(box,list_of_all)
    elif select == '6':
        os.system('clear')
        display('SELECT BY LONGEST/SHORTEST','','','1.>--SHORTEST' ,'2.>--LONGEST',' ', '0.>--EXIT','','','','','','')
        choise = input()
        if choise == '1':
            music_reports.shortest_album(list_of_all)
        elif choise == '2':
            music_reports.longest_album(list_of_all)
        elif select == '0':
            os.system('clear')
            pass
        else:
            print('WRONG SELECT'.center(140,' '))

    elif select == '0':
        os.system('clear')
        break
    else:
        print('WRONG SELECT'.center(140,' '))

