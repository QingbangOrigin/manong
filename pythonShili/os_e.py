#coding = utf-8
import os
dirs = os.getcwd()
subdirs = os.listdir(dirs)
for i in subdirs:
    path = os.path.join(dir,i)
    if os.path.isdir(path):
        end_dir = os.listdir(path)
        for i in range(len(end_dir)):
            newname = end_dir[i][0:50]
            os.rename(os.path.join(path,end_dirp[i])),os.path.join(path,newname)
