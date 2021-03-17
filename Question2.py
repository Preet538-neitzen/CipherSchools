def cipherSchools():
    while True:
        try:
            bg = float(input("Enter your budget : "))
            currentAmt = bg
        except ValueError:
            print("Enter a number only")
            continue
        else:
            break
    a ={"name":[],
        "quantity":[],
        "priceperpiece":[]
        }

    array1 = list(a.values())
    firstVal = array1[0]
    secondVal = array1[1]
    thirdVal = array1[2]
    while True:
        try:
            character = int(input("1.Add an item\n2.EXIT\nEnter your choice : "))
        except ValueError:
            print("\nERROR: Choose only digits from the given option")
            continue
        else:
            if character == 1 and currentAmt>0:
                pn = input("Enter product : ")
                q = input("Enter quantity : ")
                p = float(input("Enter price : "))

                if p>currentAmt:
                    print("\nCAN, T BUT THE PRODUCT")
                    continue

                else:
                    if pn in firstVal:
                        ind = firstVal.index(pn)
                        secondVal.remove(secondVal[ind])
                        thirdVal.remove(thirdVal[ind])
                        secondVal.insert(ind, q)
                        thirdVal.insert(ind, p)
                        currentAmt = bg-sum(thirdVal)
                        print("\namount left", currentAmt)
                    else:
                        firstVal.append(pn)
                        secondVal.append(q)
                        thirdVal.append(p)
                        currentAmt = bg-sum(thirdVal)
                        print("\namount left", currentAmt)
            elif currentAmt<= 0:
                print("\nNO BUDGET")
                break
            else:
                break
    print("\nAmount left : Rs.", currentAmt)
    if currentAmt in thirdVal:
        print("\nAmount left can buy you a", firstVal[thirdVal.index(currentAmt)])
    print("\n\n\nGROCERY LIST")
    print("\n Name Quantity Price")
    for i in range(len(firstVal)):
        print(firstVal[i], secondVal[i], thirdVal[i])

cipherSchools()