#this code to arrange/orgnize  files in folder to orgnize files with same type in one folder  
import os                                         
import shutil                                                             #library to move files from folder to another
        
import schedule
import time                                                           


def claen_path(enter_path=False):                                        
    if enter_path:
          user_path=input("Enter path") 
          os.chdir(user_path)
    else:
          user_path="D:\\Python Automation\\data"                          #defualt path    
          
                
                                                                           #change path  directory

    for file in os.listdir('.'):                                           #to loop in cuurent directory data ,'.' mean the current path
        if file.endswith(('.png','jpg','jpeg','webp')):                    #determin type of files by file extension .png,to group the same type use tuple with endwith()  
            os.makedirs('images',exist_ok=True)                            #create folder/dir name it 'image',exist_ok work with makedirs not makedir
                                                                           #exist_ok =True  if folder already exit prvent creation folder with same name 
            shutil.move(file,'images')                                     #move(src path, dst path )


        elif file.endswith(('.mp4','.avi','.mov','.mkv','.flv','.webm','.m4v' )):
                os.makedirs('videos',exist_ok=True)
                shutil.move(file,'videos')  
        
        
        elif file.endswith(('.doc','.pdf','.txt','.html','.html','.csv','.rtf')):
                os.makedirs('documents',exist_ok=True)
                shutil.move(file,'documents')  
        
        elif file.endswith(('.zip','.ztg','rar')):
                os.makedirs('compression',exist_ok=True)
                shutil.move(file,'compression')  
        
          

claen_path()
schedule.every(10).seconds.do(claen_path())                              #repeat calling the fun ebery 10 sec