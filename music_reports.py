import random
import time
import os


list_of_all = []                                                        # Wyciąga tekst z pliku i wrzuca do list
file_base = open('text_albums_data.txt','r')
for line in file_base.readlines():
        list_of_all.append(line.rstrip().split(','))
file_base.close()
                

'''class base_list:
    def bbbb(self, artist, album, year, genre, long):
                for lists in list_of_all:
                        self.artist = lists[0]
                        self.album = lists[1]
                        self.year = lists[2]
                        self.genre = lists[3]
                        self.long = lists[4]
                print(artist)'''

def time_select(year_min,year_max,list_of_all):                         #def dla wyciagania z listy albomow po dacie
        list_time = []
        for line in list_of_all:
                if int(line[2]) < year_max and int(line[2]) >= year_min :
                        list_time.append(line)
        if list_time == []:                
                print("Don't hawe albums from this years!".center(140,' '))
        else: 
                for lines in list_time:       
                        print(str(' '.join(lines)).center(140,' '))

def all_albums(self):                                                   #def wyswietla wszystkie albumy
    for line in self:
        album = line[1]
        print(album.center(140, " "))
    
def albums_by_genre(box,list_of_all):                                       #def wyswietla albumy po gatunku
        select = input()                                       
        if select == '1':
                choice = box[0]
        elif select == '2':
                choice = box[1]
        elif select == '3':
                choice = box[2]
        elif select == '4':
                choice = box[3]
        elif select == '0':
                os.system('clear')
                return
        else:
                print('Wrong select!'.center(140, " "))
                return
        list_genre = []
        for line in list_of_all:
                if choice == line[3]:
                        list_genre.append(line)
                '''if 'progressive' or 'hard' in line:
                        list_genre.remove(line)'''
        for lines in list_genre:
                print(str(' '.join(lines)).center(140,' '))
    
def albums_time_range():                                                #def wyswietla abumy po dacie
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

def shortest_album(list_of_all):                                        
        def sortSecond(val): 
                return val[4]  
        a = []
        list_of_all.sort(key = sortSecond)
        for line in list_of_all:
                print(str(' '.join(line)).center(140,' '))

def longest_album(list_of_all):
        def sortSecond(val): 
                return val[4]  
        a = []
        list_of_all.sort(key = sortSecond,reverse = True)
        for line in list_of_all:
                print(str(' '.join(line)).center(140,' '))

def shortest_longest_album(list_of_all):
        
        time_list = []
        for line in list_of_all:
                line(line[4].replace(':','.'))
                print(line)
        '''change.sort(change[4])
        print(change)'''

def albums_created_by_artist(box,list_of_all):                                         #def wyswietla abumy po artyscie 
        select = input() 
        choice = ''                                      
        if select == '1':
                choice = box[0]
        elif select == '2':
                choice = box[1]
        elif select == '3':
                choice = box[2]
        elif select == '4':
                choice = box[3]
        elif select == '5':
                choice = box[4]
        elif select == '6':
                choice = box[5]
        elif select == '7':
                choice = box[6]
        elif select == '8':
                choice = box[7]
        elif select == '9':
                choice = box[8]
        elif select == '10':
                choice = box[9]
        elif select == '0':
                os.system('clear')
                return
        else:
                print('Wrong select!'.center(140, " "))
        artist = []
        for line in list_of_all:
                if choice in line[0]:
                        artist.append(line)
        for lines in artist:   
                print(str(' '.join(lines)).center(140,' '))

def find_album(box,list_of_all):                                                       #def wyswietla abumy po nazwie albumu
        select = input() 
        choice = ()                                      
        if select == '1':
                choice = box[0]
        elif select == '2':
                choice = box[1]
        elif select == '3':
                choice = box[2]
        elif select == '4':
                choice = box[3]
        elif select == '5':
                choice = box[4]
        elif select == '6':
                choice = box[5]
        elif select == '7':
                choice = box[6]
        elif select == '8':
                choice = box[7]
        elif select == '9':
                choice = box[8]
        elif select == '10':
                choice = box[9]
        elif select == '11':
                choice = box[10]
        elif select == '0':
                os.system('clear')
                return
        else:
                print('Wrong select!'.center(140, " "))
        artist = []
        for line in list_of_all:
                if choice in line[1]:
                        artist.append(line)
        for lines in artist:      
                print(str(' '.join(lines)).center(140,' '))
#list_of_all = base_file()
#print(list_of_all)
#all_albums(list_of_all)
#albums_by_genre(list_of_all)
#albums_time_range()
#shortest_longest_album(list_of_all)
#shortest_album(list_of_all)
#time_select(1980,1990,list_of_all)