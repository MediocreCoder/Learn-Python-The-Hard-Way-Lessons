# Opening calls from sys for argv
from sys import argv

# argv will use information taken from the the terminal, ex $
# $python ex36.py ex36_wall.txt

# NOW, Define the variable names you will store the argv values
script, wall = argv


# This is the default menu for this program, aka start or HOME MENU
def start():
    
    """ 
    Preparing our HOME MENU
    WHILE LOOP chosen to allow infinite cycles of use in one running of the program
    To setup our while loop, first we must setup a comparison, boolean in nature, which will end in this case when
    
    proceed == False becomes proceed == True, 
    WITHIN this function. Remember, defining this variable in another function isolates
    
    The variable to THAT function and will not effect the start()'s while loop.
    """
    # function defined variable proceed created for while loop, set to False.
    proceed = False
    
    while proceed == False:
        
        #Repeat this text first
        print   """
Welcome to your two magic room Selection:

    1. Left Room
    2. Right Room
    3. Stay put
    
    4. Exit Game
            """
        #Repeat this input after text
        next = raw_input("Which room # would you now like to enter?> ")
        
        #Use these if statements to direct the user based on their input
        #First, we will confirm their input next isdigit(), must be an integer too!
        if next.isdigit() == True:
        
            if next == "1":
                left()
                #get_repeat will return a True or False value to proceed
                proceed = get_repeat()
            elif next == "2":
                right()
                proceed = get_repeat()
            elif next == "3":
                print "Nothing happens, other rooms may have more effective ACTIONS to escape!"
            elif next == "4":
                proceed = True
            # If next is a digit but is either too high, too low, or float!!
            elif next > "3":
                print "***This isn't a mansion. Pick 1, 2, or 3***"
            else:
                print "***Seriously? Pick 1, 2, or 3***"
        # If next.isdigit() == False, then the user did not enter an integer number required to proceed, 
        # End of loop, NO RESOLUTION to proceed, proceed still False... REPEAT from beginning!
        else:
            print "***Please use numbers only, the integer kind! ;)***"
            
    print "Thank you for playing!"


#This function will alter the start()'s while loop, returning a True or False!
def get_repeat():
    
    print """
    1. Exit Room
    2. -
    3. -

    4. Exit Game
    """
    next = raw_input("> ")
    
    if next == "4":
        return True
        
    else:
        return False

def game_over():
    next = ''
    proceed = False
    while proceed == False:
        next = raw_input("\n\nGame over!!!\n\n Continue?> ")
        if next.lower() == "yes" or next.lower() == "y":
            proceed = True
        else:
            print ""
            
    return True
        
    

# count lines of a document
def file_len(wall):
    i = 0
    with open(wall) as w:
        for i, l in enumerate(w):
            pass
    return i + 1

###
#Main part done
###
#Now to setup the functions, aka ROOMS, from which the start() will call


# Room 1
def left():
    #repeating menu with all variables to be used PRE-defined with a value or left empty, just needs to be created for later use!
    proceed = False
    line1 = ""
    line2 = ""
    next = ""
    while proceed == False:
        
        if file_len(wall) < 5:

            #Open and read the contents of wall file
            # wall file contents will be stored in the variable "textfile" for use in this function, remember to always .close() to save
            textfile = open(wall, 'r+')
            print "...MAGIC WALL CONTENTS...\n\n"
            print textfile.read(),
            print "\n\n...END OF MAGIC WALL CONTENTS..."
            #Get user input
            next = raw_input (
"""
    ACTIONS:
    1. Spray once on the wall
    2. Spray twice on the wall
    3. Wash wall

    4. Stop Spraying
>""")
        
                    
            if next == "1":
                # Prompt user for line1 with raw_input and then .write() to our target file, 
                print "Add one line below!"
                line1 = raw_input("ADD: ")
                if line1 == "b4" or line1 == "B4":
                    print "\n\n\n\n\n\n\n\n\n\nYOU WIN\n\n\n"
                    next = raw_input("Created by Alex Zuloaga")
                    next = raw_input("Hope you enjoyed this quick mock up puzzle")
                    next = raw_input("Press ENTER to resume the maze like a true veteran")
                    proceed = True
                print "...Writing..."
                textfile.write(
                    """*%s\t(ADDED USING .write())\n""" % line1)
                textfile.close()
            elif next == "2":
                print "Add lines below!"
                line1 = raw_input("ADD: ")
                line2 = raw_input("ADD: ")
                print "...Writing...Writing..."
                if line1 == "b4" or line1 == "B4" or line2 == "b4" or line2 == "B4":
                    print "\n\n\n\n\n\n\n\n\n\nYOU WIN\n\n\n"
                    next = raw_input("Created by Alex Zuloaga")
                    next = raw_input("Hope you enjoyed this quick mock up puzzle")
                    next = raw_input("Press ENTER to resume the maze like a true veteran")
                    proceed = True
                    
                textfile.write(
                    """*%s\t(ADDED USING .write())
*%s\t(ADDED USING .write())\n""" % (line1, line2)
                )
                textfile.close()
            elif next == "3":
                textfile.close()
                textfile = open(wall, 'w')
                textfile.close()
            else:
                proceed = True
        else:
            print """



























!!!

Suddenly, Police are on the seen!

!!!

            """
            next = raw_input("(Press ENTER to advance)")
            print """
    ACTIONS
    1. Keep spraying
    2. Do nothing
    3. Wash wall quickly
    
    4. RUN!
"""
            next = raw_input("> ")
            if next == "1":
                textfile = open(wall, 'r+')
                textfile.read()
                line1 = raw_input("ADD: ")
                line1 = line1[0:4] + "... *PAINT SMEARS*"
                textfile.write(line1 + "\n")
                textfile.close()
                
                #Show contents of wall
                textfile = open(wall, 'r+')
                print "...WALL CONTENTS...\n\n"
                print textfile.read(),
                print "\n\n...END OF WALL CONTENTS..."
                textfile.close()
                
                print "You just got arrested mid spray!"
                game_over()
                
            elif next == "2":
                print "You got arrested!"
                game_over()
                
            elif next == "3":
                # Delete file using 'w'
                textfile = open(wall, 'w')
                textfile.close()
                
                #Show contents of wall
                textfile = open(wall, 'r+')
                print "...WALL CONTENTS...\n\n"
                print textfile.read(),
                print "\n\n...END OF WALL CONTENTS..."
                textfile.close()
                print "Whew, Police walk past and you were not noticed!"
                proceed = True
            elif next == "4":
                print "Barely made it out of there alive!"
                proceed = True
                
                
            proceed = True


def right():
    # Define variable used within function
    print "The room is in disarray, a single torn page is on the floors"
    proceed = False
    count = 0
    books = []
    
    #while loop for menu cycling
    while proceed == False:
        next = raw_input(
""" 
    ACTIONS
    1. Read torn page
    2. Look around room
    3. Go to window
    
    4. Stop browsing
> """)

        if next == "1":
            print """
            '
You've been carrying a cardboard suitcase which has been falling apart. 
At one time it was black but the black coating has since peeled off and
yellow cardboard remains exposed. You've tried to solve that by smearing
black shoepolish over the exposed cardboard. As you walk along in the
rain the shoepolish on the suitcase runs and unwittingly rubs black
streak on both legs of your pants as you switch the suitcase from
hand to hand.

Welcome to "B4" of the basement floor, you read as you've been here before.
            '
""" 
        elif next == "2":
            print """
            
You are standing in a shadow concealed.

The walls are lightly lit from a single window casting light from the
street as the floor creaks.

You look at a confussion of numbers and letters scratched into the walls
with no apparent meaning.

Printed largely "B4"

You remember that this house is under close watch as you feel the hairs on the back of your
neck stand on end.

This house isn't safe.

"""
            next = raw_input("Press ENTER to advance")
            print """
            
    1. Try to calculate the math with your calculator
    2. -
    3. -
    
    4. Stop analyzing the math
            """
            next = raw_input("> ")
            if next == "1":
                math()
            else:
                return True
        elif next == "3":
            print """
            
                
            
A spotlight hits where you stand, cops raid into the house and arrest you

"""
            game_over()
        else:
            proceed = True
    
    
def math():
    print """
    
Your calculator is broken

All it shows is "64" repeated

And worst of all, now people know you are interested in math! 
We've notified all your social networks! :)

"""
    


start()    



""" print 

You've been carrying a cardboard suitcase which has been falling apart. 
At one time it was black but the black coating has since peeled off and
yellow cardboard remains exposed. You've tried to solve that by smearing
black shoepolish over the exposed cardboard. As you walk along in the
rain the shoepolish on the suitcase runs and unwittingly rubs black
streak on both legs of your pants as you switch the suitcase from
hand to hand.

Welcome to "B4" of the basement floor, you read as you've been here before.
"""
