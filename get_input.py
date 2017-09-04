def get_input():
    import re
    import sys
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

    #print "pre-re:", strExp
            
    #   cleanup whitespace in the strExp
    strExp = re.sub("\s+"," ",strExp)
    strExp = re.sub("{\s+","{",strExp)
    strExp = re.sub("\s+}","}",strExp)
    strExp = re.sub(",\s+",", ",strExp)    
    
    #print "post-re:", strExp
            
    return strExp