
list_of_all = []
file_base = open('/home/darek/Pulpit/Music_library/text_albums_data.txt','r')
for line in file_base.readlines():
    list_of_all.append(line.rstrip().split(','))
    
file_base.close()  


def all_albums(list_of_all):
    for line in list_of_all:
        album = line[1]
        print(album)
    

def albums_by_genre():
    pass
def albums_time_range():
    pass
def shortest_longest_album():
    pass
def albums_created_by_artist():
    pass
all_albums(list_of_all)