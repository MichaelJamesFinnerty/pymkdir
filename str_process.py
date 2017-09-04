#   determine whether the input_string has an equal number of
#   open and close grouping characters
def grouping_equilibrium(input_string, char):
    closing_char = ")" if char == "(" else "}"
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
    
