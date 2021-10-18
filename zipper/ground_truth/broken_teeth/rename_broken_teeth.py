import os 
path = './'
files = os.listdir(path) 

print(files)

for index,file in enumerate(files):
    if file[-2:] != "py":
        print("Not python file") 
        classname = "broken_teeth-";
        num = file[0:3]
        print(index, file)
        print(os.path.join(path, ''.join([classname,num, '.png'])))
        os.rename(os.path.join(path,file), os.path.join(path, ''.join([classname,num, '.png']))) 
    else:
        print("IS a python file") 
