

def mainP():
    myList = []
    print(" hello lets make a list")
    print(" choose from the following, type a munber")
    choice = input("1. add a list , 2. return the value as an index position     ")
    if choice == "1":
        addToList()
        elif choice == "2":
            indexvalues()
        
            
def addToList():
    print ("adding a new list, good choice")
    newItem = inpur("type an integer here    ")
    myList.append(int(newItem))
def indexVal():

if __name__  == "__main__":
    mainP()
        
