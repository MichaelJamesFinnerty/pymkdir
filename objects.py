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
        
        self.b_count, self.p_count = self.count_group_char()
        
        if self.b_count == 0 and self.p_count == 0:
            self.type = "file"
            self.file_name = input_string
        else:
            self.type = "grouping"
            self.group_char_open = self.id_primary_group_char()
            self.group_char_close = self.det_endChar()
            self.group_name = self.get_group_name()
            self.group_contents = self.get_group_contents()
            self.group_trail = self.get_group_trail()



            
            
            
    def det_endChar(self):
        #   returns the end grouping character
        if self.group_char_open == "(": 
            return ")"
        elif self.group_char_open == "{":
            return "}"
        else:
            return ""
            
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
        return self.kstring[ self.kstring.find(self.group_char_open)+1:self.kstring.rfind(self.group_char_close) ]

    #   identify the grouping trail
    def get_group_trail(self):
        return self.kstring[self.kstring.rfind(self.group_char_close)+1:]

    #   identify the grouping name
    def get_group_name(self):
        return self.kstring[:self.kstring.find("/")] if self.kstring.find("/") > -1 else ""
