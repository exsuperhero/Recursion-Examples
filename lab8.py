def main():

    #1test recursive printing
    n = input("Enter a number: ")
    rprint(int(n))

    #2test recursive multiplication
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    print(rmultiplication(int(x), int(y)))


    #3test out recursive lines
    n = input("Enter a number: ")
    rlines(int(n))



    #4test out largest list item
    n = input("Enter a list of numbers: ")
    n = n.split(",")
    n = [int(i) for i in n]
    print(listItem(n))





    # #5test out recursive list item
    n = input("Enter a list of numbers: ")
    n = n.split(",")
    n = [int(i) for i in n]
    print(rListSum(n))




    #6test out sum of numbers
    n = input("Enter a number: ")
    print(sumofNumbers(int(n)))


    #7 test out recursive power method
    x = input("Enter a number: ")
    y = input("Enter an exponent: ")
    print(rpower(int(x), int(y)))


#recursive printing
def rprint(n):
    if n ==0:
        return

    rprint(n - 1)
    print(n)

#recursive multiplication
def rmultiplication(x, y):
    if y == 0:
        return 0
    result = x + rmultiplication(x, y-1)
    return result

#recursive lines
def rlines(n):
    if n == 0:
        return 0

    rlines(n -1)
    list = n
    while list > 0:
        print("*", end="")
        list = list -1

    print(end="\n")




#4 largest list item
def listItem(n):
    if len(n)==1:
         return n[0]

    n.sort()
    result = listItem(n[1:])
    return result






#5 recursive list sum
def rListSum(n):
    if len(n) == 0:
        return 0
    result = n[0] + rListSum(n[1:])
    return result



#6 sum of numbers
def sumofNumbers(n):
    if n ==0:
        return 0

    result = n + sumofNumbers(n - 1)
    return result


#7 recursive power method
def rpower(x,y):
    if y ==0:
        return 1
    result = x * rpower(x, y-1)
    return result

main()