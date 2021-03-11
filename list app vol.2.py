myList = []

def mainP():
    while true:
        print(" hello lets make a list")
        print(" choose from the following, type a munber")
        choice = input("""1. add a list ,
    2. return the value as an index position
    3 exit   """)
        if choice == "1":
            addToList()
            elif choice == "2":
                indexvalues()
                elif choice == "3":
                    break
        
            
def addToList():
    print ("adding a new list, good choice")
    newItem = inpur("type an integer here    ")
    myList.append(int(newItem))
def indexVal():

if __name__  == "__main__":
    mainP()


def indexValues():
    print(" ooOoo! you want a specific piece of data, let me see what i can do")
    index pos = input("what index position would you like to see     ")
    
          
