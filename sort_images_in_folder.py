'''this code to rename images in any folder and sort them'''
import os                                         #library acess to opreation system
types=['jpg','png','jpeg','gif','webp']                  #list of image type
folder='images'                                   #name of folder 
for path,dirs,files in os.walk(folder):           #walk to acess all folders
    for i,f in enumerate(files):                  #enumerate to determine every  iteration
        full_name=os.path.join(path,f)            #f-file name(image name in folder images) & path(c://....)
        file_extension=full_name.split('.')[-1]

        if file_extension in types:
            new_name=f"{i}.{file_extension}"
            os.rename(full_name,os.path.join(path,new_name)     ) 
            print(f'successful rename {full_name}')