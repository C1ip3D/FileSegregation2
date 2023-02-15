import os
import shutil
source = r"C:/Users/shett\Documents/BYJU/Coding/Python/FileSegregation2"
dest =r"C:/Users/shett/Documents/BYJU/Coding/Python/FileSegregation2"
files= os.listdir(source)
print(files)
for fileName in files:
    name, ext = os.path.splitext(fileName)
    print(name)
    print(ext)
    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg','.jpeg', '.jfif']:
        path1 = source + '/'+fileName
        path2 = dest + '/' + "Image_Files"
        path3 = dest + '/' + "Image_Files" + '/'+fileName
        print("Path1", path1)
        print("Path3", path3)
        if os.path.exists(path2):
            print("Moving "+ fileName + '.....' )
            shutil.move(path1, path3)
        else:
            os.mkdirs(path2)
            print("Moving "+ fileName + '.....' )
            shutil.move(path1, path3)