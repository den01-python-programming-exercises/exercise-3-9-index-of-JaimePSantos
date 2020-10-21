def main():
    #write your code below this line
    intList = []
    max = 0
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)

    searchNumber = int(input("Search for?"))
    for i in range(len(intList)):
      if(intList[i] == searchNumber):
        print("%s is at index %s"%(intList[i],i))


if __name__ == '__main__':
    main()
