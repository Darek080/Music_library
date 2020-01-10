import random
import time
import os
import File_manage


list_of_all = File_manage.file_load('text_albums_data.txt')

def choice_select(box):
        select = input()
        for i in range(0,len(box),1):
                if select == str(i+1):
                        choice = box[i]
                        return choice
        return 
        
                
def all_albums(all):                                               
        for line in all:
                album = line[1]
                print(album.center(140, " "))
        input()
    
def albums_by_genre(box,list_of_all):
        try:
                choice = choice_select(box) 
                list_genre = []
                for line in list_of_all:
                        if choice == line[3]:
                                list_genre.append(line)
                os.system('clear')
                for lines in list_genre:
                        print(str(' '.join(lines)).center(140,' '))

                input()
        except:
                print('WRONG SELECT'.center(140,' '))
                input()
    
def albums_time_range():                              
        swith = input()
        list_time = []
        if swith == '1':
                time_select(1960,1970,list_of_all)
        elif swith == '2':
                time_select(1970,1980,list_of_all)        
        elif swith == '3':
                time_select(1980,1990,list_of_all)
        elif swith == '4':
                time_select(1990,2000,list_of_all)
        elif swith == '5':
                time_select(2000,2010,list_of_all)
        elif swith == '6':
                time_select(2010,2020,list_of_all)
        elif swith == '7':
                time_select(0,1960,list_of_all)
        elif swith == '0':
                os.system('clear')
                return
        else:
                print('WRONG SELECT'.center(140,' '))

def time_select(year_min,year_max,list_of_all): 
        os.system('clear')                       
        list_time = []
        for line in list_of_all:
                if int(line[2]) < year_max and int(line[2]) >= year_min :
                        list_time.append(line)
        if list_time == []:                
                print("Don't hawe albums from this years!".center(140,' '))
        else: 
                for lines in list_time:       
                        print(str(' '.join(lines)).center(140,' '))
        input()

def shortest_album(list_of_all):                                          
        a = []
        list_of_all.sort(key = sortSecond)
        os.system('clear') 
        for line in list_of_all:
                print(str(' '.join(line)).center(140,' '))
        input()

def longest_album(list_of_all):
        a = []
        list_of_all.sort(key = sortSecond,reverse = True)
        os.system('clear') 
        for line in list_of_all:
                print(str(' '.join(line)).center(140,' '))
        input()

def shortest_longest_album(choice,list_of_all):
        if choice == '1':
                shortest_album(list_of_all)
        elif choice == '2':
                longest_album(list_of_all)
        elif choice == '0':
                os.system('clear')
                pass
        else:
                print('WRONG SELECT'.center(140,' '))

def albums_created_by_artist(box,list_of_all):
        try:
                choice = choice_select(box)                                  
                artist = []
                for line in list_of_all:
                        if choice in line[0]:
                                artist.append(line)
                os.system('clear')
                for lines in artist:   
                        print(str(' '.join(lines)).center(140,' '))
                input()
        except:
                print('WRONG SELECT'.center(140,' '))
                input()

def find_album(box,list_of_all):
        try:
                choice = choice_select(box) 
                artist = []
                for line in list_of_all:
                        if choice in line[1]:
                                artist.append(line)
                os.system('clear')
                for lines in artist:      
                        print(str(' '.join(lines)).center(140,' '))
                input()
        except:
                print('WRONG SELECT'.center(140,' '))
                input()

def sortSecond(val):
        h,m = val[4].split(':') 
        el = int(h)*60 + int(m)
        return el

def new_album():
        tittle=['Artist name','Album name','Year relase','Genre','Time track']
        new_track = []
        for el in tittle:
                try:
                        inputs = input('Write '+el+': ')
                        new_track.append(inputs)
                except:
                        new_track.append('No data')
        return new_track

        
