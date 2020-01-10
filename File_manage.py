def file_load(file_location):
    list_of_all = []                                                        
    file_base = open(file_location,'r')
    for line in file_base.readlines():
            list_of_all.append(line.rstrip().split(','))
    file_base.close()
    return list_of_all

def file_save(file_location,txt):
        file_base = open(file_location,'a')
        new_music = ','.join(txt)
        file_base.write(new_music+'\n')
        file_base.close()