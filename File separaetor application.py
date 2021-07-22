######## ----- Start Of Program ---- #####

#### ---- Importing libraries ------ ####

import os
import shutil

#####-----------Storing extensions-----------######

dict_extentions = {
'Audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
'Video_extensions' : ('mp4','.mkv','.MKV','.flv','.mpeg'),
'Document_extensions' :  ('.doc','.pdf','.txt'),
'Image_extension' : ('.jpg', '.png', '.gif', '.jpeg', '.svg', '.tif'),
'Compressed_entension' : ('.zip', '.rar', '.7z', '.rmp', '.z'),
'Database_extensions' : ('.csv', '.log', '.mdb', '.xml'),
'Executable_extensions':  ( '.cpp', '.html', '.py', '.apk', '.bin', '.exe',)
}
#####-----------End of  Storing extensions-----------######

Status : print('\nStatus : Please Enter Path To Extract The File\n')  #### Show status #####

folderpath = input('Enter Folder Path : ')  #####   Take Path From User   ####


def file_finder(folder_path,file_extensions):
    files = []  ### Creating empty file ###
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

for extension_type,extension_tuple in dict_extentions.items():
    folder_name = extension_type.split('_')[0] + 'files'  ###   Creating file name with same extension as file present in folder ###
    folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    
    for item in file_finder(folderpath,extension_tuple):
         item_path = os.path.join(folderpath,item)
         item_new_path = os.path.join(folder_path,item)
         shutil.move(item_path,item_new_path)  ### Moving file into a folder ####


Status : print('\nStatus : File Is Extracted Successfully') ### Show status ###

##################### ---------- End Of Program ---------- ##############
