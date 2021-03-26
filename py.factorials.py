def factorials(x):
    if x == 1:
        return 1
    else:
        return(x * factorials(x-1))

if __name__ == "__main__":

    num = input(" what do yu want the factorials of?    ")
    print("the factorial of " , num , " is ", factorials(int(num)))
    
