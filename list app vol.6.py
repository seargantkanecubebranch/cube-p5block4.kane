myList = []
uniqueList = []
import random 
def mainP():
    while True:
        try:
            print(" hello lets make a list")
            print(" choose from the following, type a munber")
            choice = input("1. add to a list \n 2.add a lot of numbers \n 3. return the value as an index position \n 4.random search \n 5. linear search \n 6. print list \n 7.  recursive search \n 8. exit   \n   ")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                 indexValue()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList(mylist)
            elif choice == "7":
                printLists()
            elif choice == "8":
                recursivebinarysearch(uniqueList, 0, len(uniqueList)-1, int(searchItem)
                
            else:
                break
        except:
            print("you made a uh oh")
        
            
def addToList():
    print ("adding a new list, good choice")
    newItem = input("type an integer here    ")
    myList.append(int(newItem))
def addABunch():
    print ("oodles and oodles of numbers")
    numToAdd = input("how many ints would you like to add    ")
    numRange = input(" and how high would you like these ints to go    ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your list is now filled")



def indexValues():
    print(" ooOoo! you want a specific piece of data, let me see what i can do")
    indexPos = input("what index position would you like to see     ")
    print(myList[int(indexPos)])

def sortList(myList):
    print("need some data sorted")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input(" wanna see your new list")
    if shoeMe.lower() == "y":
        print(uniqueList)


def randomSearch():
    print("lemme see what i got")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("oh god ok give me a sec")
    searchItem = input("what you looking for")
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount - 1
            print(" your item is at index{}".format(x))
    print(indexCount)

def recursivebinarysearch(uniqueList, low, high, x):
    if high >= low
    mid = (high+low) // 2

    if uniqueList[mid] == x:
        print("whelp ive found it{}". format())
        return mid
    elif uniqueList[mid] >x:
        return recursivebinarysearch(uniqueList, low, high, mid -1, x)
    else:
        return  recursivebinarysearch(uniqueList, low, high, mid +1, x)
        

    else:
        print(" your number isnt here")

def iteritivesearch(uniqueList, x)
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1
        elif uniqueList[mid] > x:
            high = mid - 1
        else:
            return
        return -1 
        

def printLists():
    if len (uniqueList) == 0:
        print(myLIst)
    else:
        whichOne - input(" which list? sorted or not sorted
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)
            
    
if __name__  == "__main__":
    mainP()
