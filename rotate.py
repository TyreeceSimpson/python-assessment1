#Function to rotate string
def print_rotate(text, print_direction):
    #Variables to be used to rotate string
    y = len(text)
    z = 0

    #Pointing North
    if print_direction == 0:
        for x in range(y):    
            while z < y:
                print(text[z])
                z = z +1

    #Pointing North-East            
    if print_direction == 1:
        for x in range(y):
            y = y - 1
            print(" "*y, text[z])
            z = z +1

    #Pointing East            
    if print_direction == 2:
        for x in range(y):
            y = y - 1
            print(text[y], end = '')

    #Pointing South-East        
    if print_direction == 3:
        for x in range(y):
            p = y
            while z < p:       
                y = y - 1
                print(" "*z, text[y])
                z = z +1
                
    #Pointing South
    if print_direction == 4:
        for x in range(y):
            y = y - 1
            print(text[y])
        
    #Pointing South-West    
    if print_direction == 5:
        for x in range(y):
            y = y - 1
            print(" "*y, text[y])

    #Pointing West        
    if print_direction == 6:
        print(text)

    #Pointing North-West    
    if print_direction == 7:
        for x in range(y):    
            while z < y:
                print(" "*z, text[z])
                z = z +1

#Calls the function, defines the string and rotation
print_rotate("rotate", 0)
