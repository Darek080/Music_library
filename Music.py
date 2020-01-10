import Display
import os
import Music_reports
import File_manage

menu = ['SHOW ALL ALBUMS','SELECT BY GENRE','SELECT BY TIMEs','SELECT BY ARTIST','SELECT BY ALBUM','SELECT BY LONGEST/SHORTEST',"NEW ALBUM"]
times = ['60','70','80','90','2000','2010','Oldest']
longest_shortest = ['SHORTEST','LONGEST']

def run():
    os.system('clear')
    active = True
    while active:
        list_of_all = File_manage.file_load('text_albums_data.txt')

        Display.display('MENU',menu)
        select = input()
        if select == '1':
            os.system('clear')
            Music_reports.all_albums(list_of_all)

        elif select == '2':
            box = Display.display_list(list_of_all, 3)
            Display.display('SELECT BY GENRE',box)
            Music_reports.albums_by_genre(box,list_of_all)

        elif select == '3':
            Display.display('SELECT BY TIMEs',times)
            Music_reports.albums_time_range()

        elif select == '4':
            box = Display.display_list(list_of_all, 0)
            Display.display('SELECT BY ARTIST',box)
            Music_reports.albums_created_by_artist(box,list_of_all)

        elif select == '5':
            box = Display.display_list(list_of_all, 1)
            Display.display('SELECT BY ALBUM',box)
            Music_reports.find_album(box,list_of_all)

        elif select == '6':
            Display.display('SELECT BY LONGEST/SHORTEST',longest_shortest)
            choice = input()
            Music_reports.shortest_longest_album(choice,list_of_all)

        elif select == '7':
            os.system('clear')
            list_new_album = Music_reports.new_album()
            File_manage.file_save('text_albums_data.txt',list_new_album)

        elif select == '0':
            os.system('clear')
            break
        else:
            print('WRONG SELECT'.center(140,' '))