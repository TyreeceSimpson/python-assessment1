#Function to reverse inputted string
def print_reverse(text, print_spaces=False):   
    #Sets the length of the string to var y
    y = len(text)
    
    #Repeat for the length of the string
    for x in range(y):
        #Decreases the length by one
        y = y - 1
        #Prints each letter with spaces else without
        if print_spaces==True:
            print(" "*y, text[y])
        else:
            print(text[y])

#Calls the function, defines the string and spaces
print_reverse("reversestring")
