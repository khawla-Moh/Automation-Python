#using os lib 
import os



#os.mkdir('Test')                                         #create floder
#print(os.getcwd())                                       #get the current work directory     
#os.rename('txt.txt','python.txttxt')
#os.makedirs('Test/python/project1')                      #create multiple folders

#****************

#print(os.getcwd()) 
#os.chdir('Test/python')                                  #change directory/folder 
#print(os.getcwd())

#os.rmdir('Test/python/project1')                          #remove directory Test   
#os.removedirs('Test/python')                              #remove multiple directories/folders  
#****************


#d="C:\\Users\\KhaMoh\\Documents"                          #d='path'
#print(os.listdir(d))                                      #list all folders/directories 

#****************
d="C:\\Users\\KhaMoh\\Documents"                          #d='path'
for dirpath,dirname,filename in os.walk(d):               #walk to access in each folder 
    print(f"Path:{dirpath}")                              #print path 
    print(f"Name:{dirname}")                              #print folder/directory name
    print(f"File:{filename}")                             #print file name  

       