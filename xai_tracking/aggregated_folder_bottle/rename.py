import os 
path = './'
files = os.listdir(path) 

print(files)

for index,file in enumerate(files):
    if file[-2:] != "py" and "good" in file:
        # print("Not python file") 
        classname = "bottle_good-";
        num = file[5:8]
        print(index, file)
        print(os.path.join(path, ''.join([classname,num, '.png'])))
        os.rename(os.path.join(path,file), os.path.join(path, ''.join([classname,num, '.png']))) 
    else:
        # print("IS a python file") 
        pass
