import os
from PIL import Image




data_folder=input("enter a data_folder : ")
logo_name=input("enter logo name : ")
save_location=input("enter save folder :")

#open logo
logo_image=Image.open(logo_name)
logo_width,logo_height=logo_image.size

#create save location
os.makedirs(save_location,exist_ok=True)




for file in os.listdir(data_folder):
    if not file.endswith(('.jpg','.png','.jpeg','.gif','.webp')):
        continue
    
    image_path=os.path.join(data_folder,file) 
    img=Image.open(image_path)
    width,height=img.size
    img.paste(logo_image,(width-logo_width,height-logo_height),logo_image)
    img.save(os.path.join(save_location,file))
    print(f'added logo to {file}')