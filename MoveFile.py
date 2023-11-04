import os
import shutil

fromdir ='C:/Users/nisha/Downloads'
todir ='C:/Users/nisha/OneDrive/Documents/docs_file'

list_of_files = os.listdir(fromdir)
print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == "" :
       continue

    if extension in [".seb", ".json", ".exe", ".apk", ".dll", ".msi"]:
       path1 = fromdir + '/' + file_name
       path2 = todir + "/" + "Others_file"
       path3 = todir + '/' + "Others_file" + "/" + file_name
       print("Path 1", path1)
       print("Path 3", path3)

       if os.path.exists(path2):
        print("moving" + file_name + "....")
        shutil.move(path1, path3)

       else:
          os.mkdir(path2)
          print("moving" + file_name + "....")
          shutil.move(path1, path3)



