# George Close (glclose1@sheffield.ac.uk) 2022
# Distribute and modify freely ! 
import os
from distutils.dir_util import copy_tree
from distutils.errors import DistutilsFileError
import shutil
import datetime
import getpass
import concurrent.futures
import subprocess

username = getpass.getuser()
print("Your username is: ", username)
save_root = "/fastdata/%s/"%username
start_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


def backup_file(file):
    file = file.strip()
    print("FILE: ",file)
    new_file = file.replace(username,"%s/%s"%(username,backup_name))
    #print("NEW_FILE:", new_file)
    if not os.path.exists(new_file) and not os.path.islink(file):
        try:
            copy_tree(file,new_file,preserve_symlinks=1)
        except DistutilsFileError:
            shutil.copy(file,new_file,follow_symlinks=True)



with open("to_save_list.txt") as f:
    in_list = f.readlines()

print("Getting list of files older than 60 days...")
print("(This may take some time)")

# we create a file containing a list of all files older than 60 days in fastdata
save_list = "save_list_%s.txt"%start_time
f = open(save_list, "w")
subprocess.call(("lfs find -ctime +60 %s"%(save_root)).split(), stdout=f)
f.close()

with open (save_list) as f:
    in_list = f.readlines()

backup_name = "backup-%s"%start_time
backup_dir = os.path.join(save_root,backup_name)
print("saving %s files to %s"%(len(in_list),backup_dir))
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

#creates a number of threads to iterate over the list of files and back them up 
executor = concurrent.futures.ThreadPoolExecutor()
futures = [executor.submit(backup_file, file) for file in in_list]
concurrent.futures.wait(futures)

print("Done! Now don't forget to move these files back to fastdata later! :)")