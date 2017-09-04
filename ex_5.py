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

import inspect
from objects import fold, trail_obj, kernel


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
        print "Popping kernel"
        element = kernel(
                    pop_kernel_from_string(input_string)
                    )
        
    
        if element.type == "file":
            
            #   if element is a file, it gets added to the 
            #   current output folder
            print "File element detected."
            output_folder.files.append(
                            element.file_name
                            )
            print "The element ",element.file_name," has been added to the ",
            print "folder.\n\n" if output_folder.name else "grouping.\n\n"
            
        elif element.type == "grouping":
            
            #   all groupings are processed in the context of a
            #   sub_folder
            #
            print "Grouping detected. Parsing contents. Type: ",
            print "folder.\n" if element.group_char_open == "{" else "grouping.\n"
            sub_folder = parse(
                            element.group_contents, 
                            fold()
                            )
            print "\nPARSING COMPLETE\nPROCESSING GROUPING\n"
            
            #   apply the trail, if exists
            if element.group_trail != "": 
                print "in_it_ex-ing"
                sub_folder.files, sub_folder.subfolders = in_it_ex(
                                                            element.group_trail, 
                                                            sub_folder
                                                            )
            
            #   if the grouping is a folder, the subfolder will
            #   be appended into the :subfolders list for the
            #   current output_folder
            #
            
            #   MTC
            #   in the case:
                #   [index.html, styles/{%$, archive/{}}*4+style.css, js/{}]
            #   "archive" is created as a string, not subfolder, but:
                #   [folder/{sub/{ssuubb/{}}}]
            #   seems to work fine
            
            if element.group_char_open == "{":
                print "Folder detected. Appending to ",
                print "folder.\n" if output_folder.name else "grouping.\n"
                sub_folder.name = element.group_name
                output_folder.subfolders.append(sub_folder)
                                
            #   if it is just a file grouping, the individual files
            #   contents will be appended to the :files list for the
            #   current output folder
            elif element.group_char_open == "(":
                print "Grouping detected. Appending files."
                for _file in sub_folder.files:
                    print "Appending ",_file
                    output_folder.files.append(_file)            
                print "\n"
                
        #   recurse the rest of the input string back into parse()
        remain_string = input_string[len(element.kstring):]
        
        if remain_string != "":
            while remain_string[0] == " " or remain_string[0] == ",":
                remain_string = remain_string[1:]
        
        parse(remain_string, output_folder)
    
    return output_folder
    
    
def main():

    from output import verbose_output, touch, folder_maker
    from get_input import get_input

    #   Welcome the user to the program
    print "\n\nFILE EXPANDER:\n\n"
    
    #   Set the input string expression (strExp)
    strExp = get_input()
    
    #process parsed elements into the folder object
    result_folder = parse(strExp[1:-1], fold())
    print "FULL PARSING COMPLETED.\nPRINTING OUTPUT."
    
    #verbose_output(result_folder, "")

    #folder_maker(result_folder, "./")
    return result_folder
    
if __name__ == '__main__':
    main()