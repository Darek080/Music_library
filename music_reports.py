import random

list_of_all = []
file_base = open('text_albums_data.txt','r')
for line in file_base.readlines():
    list_of_all.append(line.rstrip().split(','))
 
file_base.close()

def time_select(year_min,year_max,list_of_all):
        
        for line in list_of_all:
                list_time = []
                if int(line[2]) < year_max and int(line[2]) >= year_min :
                        list_time.append(line)        
                        return list_time

def all_albums(list_of_all):
    for line in list_of_all:
        album = line[1]
        print(album)
    
def albums_by_genre(list_of_all):
    choise = input('Select the genre: ')
    list_genre = []
    for line in list_of_all:
    
        if choise in line[3]:
            list_genre.append(line)

    for line in list_genre:
        print(line)
    
def albums_time_range(list_of_all):
        swith = input('Select time range: ')
        
        if int(swith) == 1:
                time_select(1960,1969,list_of_all)
        if swith == 2:
                time_select(1970,1979,list_of_all)        
        if swith == 3:
                time_select(1980,1989,list_of_all)
        if swith == 4:
                time_select(1990,1999,list_of_all)
        if swith == 5:
                time_select(2000,2009,list_of_all)
        if swith == 6:
                time_select(2010,2019,list_of_all)
        if swith == 7:
                time_select(0,1959,list_of_all)
        else:
                print('Wrong select')
        list_time = []
        print(list_time)


def shortest_longest_album():
        choise = input('Select s to shortest  ')
        if choise == s:
                shortest = list_of_all.sort(list_of_all[4])
                print(shortest)

def albums_created_by_artist():
        choise = input('Select the Artist: ')
        artist = []
        for line in list_of_all:
        
                if choise in line[0]:
                        artist.append(line)

        for line in artist:
                print(line)
        pass
#print(list_of_all)
#albums_by_genre(list_of_all)
albums_time_range(list_of_all)
#---shortest_longest_album()