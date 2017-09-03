#   A lightweight tool for generating complex folder and file structures from strings
#   
#   Input formatting:
#     Structured input must be within braces
#     --[] (empty input string)
#     
#     Directories are designated with the name, followed by a slash, and then curly braces.
#     An empty directory must include an empty set of curly praces in its structure.
#     --e.g. [foldr/{}] (empty directory named folder)
#
#     Folder contents are comma separated strings within the curly braces.
#     --e.g. [foldr/{index.html, style.css}] 
#     --(creates a directory named foldr, containing the files index.html and style.css)
#
#     Subdirectories can be nested directly within a directory.
#     --e.g. [foldr/{ sub1/{}, sub2/{} }]
#       
#     --e.g. [folder/{(file$.html)*4 sub/{%_index.html, %_thumbs.db}+test (example$)*2.js}]

import re
import os
import sys
import inspect
from os import mkdir, utime, chdir, getcwd


#   #   #   #   #   #   #   #
#   CLASS OBJECTS           #
#   #   #   #   #   #   #   #

class fold(object):
    def __init__(self):
        self.name = ""
        self.files = []
        self.subfolders = []

    
class trail_obj(object):
     def __init__(self):
        self.trail = ""
        self.extension = ""
        self.iterator = ""
        self.injector = ""

    

class kernel(object):
    
    def __init__(self, input_string):
        
        self.kstring = input_string
        
        b_count, p_count = self.count_group_char()
        
        if b_count == 0 and p_count == 0:
            self.type = "file"
            self.file_name = input_string
        else:
            self.type = "grouping"
            self.group_charo = self.id_primary_group_char()
            self.group_charc = self.det_endChar()
            self.group_name = self.get_group_name()
            self.group_contents = self.get_group_contents()
            self.group_trail = self.get_group_trail()



            
            
            
    def det_endChar(self):
        #   returns the end grouping character
        if self.group_charo == "(": 
            return ")"
        elif self.group_charo == "{":
            return "}"
            
    def id_primary_group_char(self):
        #   returns first grouping character in the input string,
        #   or empty string if none found
        for char in self.kstring:
            if char == "{" or char == "(":
                return char

        return ""
        
    def count_group_char(self):
        kstring = self.kstring
        b_count = kstring.count("{")
        p_count = kstring.count("(")
        return b_count, p_count

    
    
    
    
    
    def get_group_contents(self):
        return self.kstring[
                self.kstring.find(self.group_charo)+1:
                self.kstring.rfind(self.group_charc)
                ]

    #   identify the grouping trail
    def get_group_trail(self):
        return self.kstring[
                self.kstring.rfind(self.group_charc)+1:
                ]

    #   identify the grouping name
    def get_group_name(self):
        return self.kstring[
                :self.kstring.find("/")
                ]

def place_holder2():
    return True

#   determine whether the input_string has an equal number of
#   open and close grouping characters
    
        
    
#   determine whether the input_string has an equal number of
#   open and close grouping characters
def grouping_equilibrium(input_string, char):
    closing_char = det_endChar(char)
    if input_string.count(char) == input_string.count(closing_char):
        return True
    else:
        return False
    
    
def pop_kernel_from_string(input_string, grain=""):
    
    #   if the input_string is null (meaning all characters
    #   have been passed to the grain), the grain pops into
    #   a kernel (see :else, below)
    if input_string != "":
        first_character = input_string[0]
        
        #   the grain is fed the next character of the 
        #   input_string until it pops into a kernel
        #
        #   the pop occurs when:
        #       1) the end of input_string is reached, or
        #       2) the next character is a space, and
        #       3) all "()" and "{}" groupings are closed
        #
        if (
            first_character == " " and
            grouping_equilibrium(grain, "(") and
            grouping_equilibrium(grain, "{")
           ):
            
            #   comma separation between elements is allowed,
            #   but not required
            #
            #   if the user is using comma separation, the comma
            #   is removed before further processing
            kstring = grain[:-1] if grain[-1] == "," else grain
            
        #   if the pop has not yet occurred, the first character
        #   of the input string is added to the grain, and both
        #   elements are recursed back in to the function
        else:
            kstring = pop_kernel_from_string(
                        input_string[1:], 
                        grain + first_character
                        )
    else:
        kstring = grain
    return kstring
    
def place_holder3():
    return True


    
    
#   #   #   #   #   #   #   #   #   #
#   FILE PROCESSING                 #
#   #   #   #   #   #   #   #   #   #

def injector_tion(injector, file_list, folder_list):
    file_list[:] = [
                            _file.replace("%", injector) 
                            for _file in file_list
                        ]

    folder_list[:] = [
                            folder.name.replace("%", injector)
                            for folder in folder_list
                    ]
    
    return file_list, folder_list


def iterator_tion(iterator, file_list, folder_list):
    for _file in file_list:
        if "$" in _file:
            for x in range(iterator):
                file_list.append(_file.replace("$", str(x+1)))
            file_list.remove(_file)

    for folder in folder_list:
        if "$" in folder.name:
            
            new_folder_list = []
            
            for x in range(iterator):
                new_folder_list.append(fold())
                new_folder_list[-1:][0].name = folder.name.replace("$", str(x+1))
                new_folder_list[-1:][0].files = folder.files
                new_folder_list[-1:][0].subfolders = folder.subfolders
            
            folder_list.remove(folder)
                
            [folder_list.append(item) for item in new_folder_list]
                
    return file_list, folder_list


def extension_tion(extension, file_list):
    file_list[:] = [
                            _file + extension
                            for _file in file_list
                        ]
    
    return file_list


def trail_func(trail_string, folder):
    
    file_list, folder_list = folder.files, folder.subfolders
    start_char = trail_string[0]
    next_spec_char = determine_next_spec_char(trail_string[1:])
    
    if start_char == "+":
        injector = trail_string[1:next_spec_char]
        (file_list, folder_list) = injector_tion(injector, file_list, folder_list)
        
    elif start_char == "*":
        iterator = int(trail_string[1:next_spec_char])
        (file_list, folder_list) = iterator_tion(iterator, file_list, folder_list)
            
    elif start_char == ".":
        extension = trail_string[:next_spec_char]
        file_list = extension_tion(extension, file_list)
        
    if trail_string[next_spec_char:] != "":
        trail_func(trail_string[next_spec_char:], file_list, folder_list)
        
    return file_list, folder_list

    
    
#   determine the location of the next special character
#   returns an integer
def determine_next_spec_char(string):
    #   returns an integer representing the location of the next
    #   special character
    spec_char = ['+', '*' , '.']
    
    #   set the current result as the length of the string
    #
    #   if no special character is found, the entire string will
    #   be returned
    loc_out = len(string)
    
    #   any special characters that are found wll be set as the
    #   cut-off location (if they occur earlier than the 
    #   current cur-off location)
    for char in spec_char:
        if char in string:
            loc_cur = string.find(char)
            if loc_cur < loc_out: loc_out = loc_cur
                
    return loc_out
    
    
    
def parse(input_string, output_folder):
    
    #   isolates the leading kernel for processing
    #
    #   the kernel is the first element in current string
    #
    #   the kernal may be an individual file object or a group object
    if input_string != "":
        
        #   feed the input string into that function, and have the
        #   function return the kernel object
        element = kernel(
                    pop_kernel_from_string(input_string)
                    )
    
        if element.type == "file":
            
            #   if element is a file, it gets added to the 
            #   current output folder
            output_folder.files.append(
                            element.file_name
                            )
            
        elif element.type == "grouping":
            
            #   all groupings are processed in the context of a
            #   sub_folder
            #
            sub_folder = fold()
            sub_folder = parse(
                            element.group_contents, 
                            sub_folder
                            )
            
            #   apply the trail, if exists
            if element.group_trail != "": 
                sub_folder.files, sub_folder.subfolders = trail_func(
                                                            element.group_trail, 
                                                            sub_folder
                                                            )
            
            #   if the grouping is a folder, the subfolder will
            #   be appended into the :subfolders list for the
            #   current output_folder
            #
            if element.group_charo == "{":
                sub_folder.name = element.group_name
                output_folder.subfolders.append(sub_folder)
                                
            #   if it is just a file grouping, the individual files
            #   contents will be appended to the :files list for the
            #   current output folder
            elif element.group_charo == "(":
                for _file in sub_folder.files:
                    output_folder.files.append(_file)            
            
        #   recurse the rest of the input string back into parse()
        remain_string = input_string[len(element.kstring):]
        
        if remain_string != "":
            while remain_string[0] == " " or remain_string[0] == ",":
                remain_string = remain_string[1:]
        
        parse(remain_string, output_folder)
    
    return output_folder
    
    
    
    
    

    
    
    
        

#   #   #   #   #   #   #   #   #   #
#   OUTPUT PRINTING                 #
#   #   #   #   #   #   #   #   #   #

#   print results (no return)        
def verbose_output(fold_in, lead_in):
    if fold_in.name == '':
        fold_in.name =  os.getcwd()
    
    print lead_in + "Folder name:\t" + fold_in.name
    #
    if len(fold_in.files) != 0:
        print "\n" + lead_in + "\tFiles:"
        for item in fold_in.files:
            print lead_in + "\t" + item
    #
    if len(fold_in.subfolders) != 0: 
        print "\n" + lead_in + "\tSubfolders:"
        for item in fold_in.subfolders:
            verbose_output(item, lead_in + "\t\t")
    

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
    
def folder_maker(fold_in, base_path):
    for _file in fold_in.files:
        touch(_file)
    
    for sub in fold_in.subfolders:
        mkdir(sub.name)
        chdir(sub.name)
        folder_maker(sub, sub.name)
        chdir("../")




        
def main():

    #   Welcome the user to the program
    print "\n\nFILE EXPANDER:\n\n"
    
    #   Set the initial (empty) variables for the output folder 
    #   (result_folder) and the input string expression (strExp)
    result_folder = fold()
    strExp = ""
    
    #   Determine whether a strExp has been provided
    if len(sys.argv) > 1:
        strExp = sys.argv[1]
    else:
        
        #   Prompt user for a strExp input
        #
        #   strExp will be concatenated from the user input 
        #   until the closing "]" character is provided
        print ">>> Please provide expansion string:"
        print ">>> (--Format: [folder/{(file$.html)*4 sub/{%_index.html, %_thumbs.db}+test (example$)*2.js}]--)"
        while "]" not in strExp:
            f = raw_input(">>> \t")
            
            #   remove trailing comma
            if f[-1:] == ",":
                f += " "   
            strExp += f

    #   cleanup whitespace in the strExp
    strExp = re.sub("\s+"," ",strExp)
    
    #process parsed elements into the folder object
    result_folder = parse(strExp[1:-1], result_folder)
    
    verbose_output(result_folder, "")

    folder_maker(result_folder, "./")

if __name__ == '__main__':
    main()