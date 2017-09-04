#   A lightweight tool for directly generating complex folder and file structures in python
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

import inspect
from objects import fold, kernel


def parse(input_string, output_folder):
    
    from in_it_ex import inject, iterate, extend, in_it_ex, determine_next_spec_char
    from str_process import grouping_equilibrium, pop_kernel_from_string
    
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
            sub_folder = parse(
                            element.group_contents, 
                            fold()
                            )
            
            #   apply the trail, if exists
            if element.group_trail != "": 
                sub_folder.files, sub_folder.subfolders = in_it_ex(
                                                            element.group_trail, 
                                                            sub_folder
                                                            )
            
            #   if the grouping is a folder, the subfolder will
            #   be appended into the :subfolders list for the
            #   current output_folder
            #
            if element.group_char_open == "{":
                sub_folder.name = element.group_name
                output_folder.subfolders.append(sub_folder)
                                
            #   if it is just a file grouping, the individual files
            #   contents will be appended to the :files list for the
            #   current output folder
            elif element.group_char_open == "(":
                for _file in sub_folder.files:
                    output_folder.files.append(_file) 
                
        #   recurse the rest of the input string back into parse()
        remain_string = input_string[len(element.kstring):]
        
        if remain_string != "":
            while remain_string[0] == " " or remain_string[0] == ",":
                remain_string = remain_string[1:]
        
        parse(remain_string, output_folder)
    
    return output_folder
    
    
def main(strExp="", vbose=False):

    from output import verbose_output, touch, folder_maker
    from get_input import get_input

    #   Set the input string expression (strExp)
    if strExp == "":
        strExp = get_input()
    
    #process parsed elements into the folder object
    result_folder = parse(strExp[1:-1], fold())
    
    if vbose:
        try:
            verbose_output(result_folder, "")
        except:
            print "ERROR"

    #folder_maker(result_folder, "./")
    return result_folder
    
if __name__ == '__main__':
    main()