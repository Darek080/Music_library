
list_of_all = []
file_base = open('text_albums_data.txt','r')
for line in file_base.readlines():
    list_of_all.append(line.rstrip().split(','))
 
file_base.close()
 
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

    for ist in list_genre:
        print(ist)
    
def albums_time_range():
    pass
def shortest_longest_album():
    pass
def albums_created_by_artist():
    pass
#print(list_of_all)
albums_by_genre(list_of_all)