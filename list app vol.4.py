myList = []
import random 
def mainP():
    while true:
        try:
            print(" hello lets make a list")
            print(" choose from the following, type a munber")
            choice = input("""1. add a list
2.add a lot of numbers
3. return the value as an index position
4.random search
5. print list
6.  exit   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                 indexValue
            elif choice == "4":
                randomSearch
            elif choice == "5":
            
                def randomSearch
            else:
                break
        except:
            print("you made a uh oh")
        
            
def addToList():
    print ("adding a new list, good choice")
    newItem = inpur("type an integer here    ")
    myList.append(int(newItem))
def addABunch():
    print ("oodles and oodles of numbers")
    numToAdd = input("how many ints would you like to add    ")
    numRange = input(" and how high would you like these ints go    ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print(" your list is nor filled
def indexVal():

if __name__  == "__main__":
    mainP()


def indexValues():
    print(" ooOoo! you want a specific piece of data, let me see what i can do")
    index pos = input("what index position would you like to see     ")
    print(myList[int(indexPos)])

def randomSearch():
    print("lemme see what i got"):
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("oh god ok give me a sec")
    searchItem = input("what you looking for")
    for x in range(len(mylist)):
        print(" your item is at index{}".format(x))
