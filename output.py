#   #   #   #   #   #   #   #   #   #
#   OUTPUT PRINTING                 #
#   #   #   #   #   #   #   #   #   #

#   print results (no return)        
def verbose_output(fold_in, lead_in):
    import os

    if fold_in.name == '':
        fold_in.name =  os.getcwd()
    
    print lead_in + "Folder name:\t" + fold_in.name
    #
    if len(fold_in.files) != 0:
        print lead_in + "\tFiles:"
        for item in fold_in.files:
            print lead_in + "\t" + item
        print
    #
    if len(fold_in.subfolders) != 0: 
        print lead_in + "\tSubfolders:"
        for item in fold_in.subfolders:
            verbose_output(item, lead_in + "\t\t")
        print

def touch(fname, times=None):
    from os import utime
    
    with open(fname, 'a'):
        utime(fname, times)
    
def folder_maker(fold_in, base_path):
    from os import mkdir, chdir, getcwd
    
    for sub in fold_in.subfolders:
        mkdir(sub.name)
        chdir(sub.name)
        folder_maker(sub, sub.name)
        chdir("../")

    for _file in fold_in.files:
        touch(_file)
    



        
