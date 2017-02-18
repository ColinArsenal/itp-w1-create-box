"""This is the entry point of the program."""

def create_box(height, width, character):
    box = ""
    if height >= 1 and width >= 1:
        for _ in range(height):
            for i in range(width):
                box += character
            box += '\n'
        return box
    else:
        return 'invalid entry'


#co = create_box(4,4,'@')
#print(co)

def empty_box(height, width, character):
    box = ""
    if height >= 1 and width >= 1:
        for j in range (height):
            if j == 0 or j == height - 1:
                # Create a full row
                for i in range(width):
                    box += character
                box += '\n'
                
            else:
                # Create a row with only the first and last characters:
                for i in range(width):
                    if i == 0 or i == width - 1:
                        box += character
                    else:
                        box += " "
                box += '\n'
            
            
        return box
#    else:
 #      return 'invalid entry'
    
#border = empty_box(4, 6, '@')
#print (border)