### renamer.py
import os
import shutil

home ='/home/daniel/'
descargas = os.path.join(home,'Descargas')
file_list = os.listdir(descargas)
if not 'PDF Folder' in file_list :
    os.mkdir(os.path.join(descargas,'PDF Folder'))
elif not os.path.isdir(descargas+'/PDF Folder') :
    os.mkdir(os.path.join(descargas,'PDF Folder'))
    
pdf_folder =(os.path.join(descargas,'PDF Folder'))

for file in file_list :
    if file.endswith('.pdf') :
        source = os.path.join(descargas,file)
        ### IT IS CRUCIAL TO ADD / TO DESTINY IN ORDER TO
        ### MOVE TO A DIRECTORY
        ### IF YOU DO NOT ADD /, IT WILL CREATE A ### FILE ###
        ### WITH ALL THE FILES AND YOU WILL LOSE ALL FILES
        destiny = os.path.join(descargas,'PDF Folder' + '/')
        shutil.move(source,destiny)

pdf_files = os.listdir(pdf_folder)

for file in pdf_files :
    old = pdf_folder + '/' + file
    new = pdf_folder + '/' + file.replace('_',' ')
    os.rename(old,new)
    


        
        