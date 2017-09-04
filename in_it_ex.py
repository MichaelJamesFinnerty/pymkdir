#   #   #   #   #   #   #   #   #   #
#   IN_IT_EX PROCESSING                 #
#   #   #   #   #   #   #   #   #   #

def inject(injector, file_list, folder_list):
    
    # replace the % wildcard with the injector sring
    file_list[:] = [ _file.replace("%", injector) for _file in file_list ]
    folder_list[:] = [ _folder.name.replace("%", injector) for _folder in folder_list ]
    
    return file_list, folder_list


def iterate(iterator, file_list, folder_list):
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


def extend(extension, file_list):
    # append the extension to each file in the file_list
    file_list[:] = [ _file + extension for _file in file_list ]
    
    return file_list


def in_it_ex(trail_string, folder):
    
    file_list, folder_list = folder.files, folder.subfolders
    start_char = trail_string[0]
    
    # 1 is added back to account for the ommitted leading character
    next_spec_char = determine_next_spec_char(trail_string[1:])+1
    
    print "trail_string:\t", trail_string
    print "next_spec_char pos:\t", next_spec_char
    print "trail_string[1:next_spec_char]:\t", trail_string[1:next_spec_char], "\n\n"
        
    if start_char == "+":
        injector = trail_string[1:next_spec_char]
        (file_list, folder_list) = inject(injector, file_list, folder_list)
        
    elif start_char == "*":
        iterator = int(trail_string[1:next_spec_char])
        (file_list, folder_list) = iterate(iterator, file_list, folder_list)
            
    elif start_char == ".":
        extension = trail_string[:next_spec_char]
        file_list = extend(extension, file_list)
        
    if trail_string[next_spec_char:] != "":
        file_list, folder_list = in_it_ex(trail_string[next_spec_char:], folder)
        
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
    
    