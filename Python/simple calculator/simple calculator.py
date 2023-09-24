while True:
    num1 = float(input("number 1 : "))
    print("\n","+","\n","-","\n","*","\n","/")
    func = input("Please select your function: ")
    num2 = float(input("number 2 : "))

    if func == "+" :
        a = num1+num2
        print(str(num1) + "/t+/t" + str(num2) + "=" + str(a))
    elif func == "-" :
        b = num1 - num2
        print(str(num1) + "-" + str(num2) + "=" + str(b))
    elif func =="*" :
        c = num1 * num2
        print(str(num1) + "*" + str(num2) + "=" + str(c))
    elif func == "/" :
        d= num1 / num2
        print(str(num1) + "/" + str(num2) + "=" + str(d))

    q = input("Do want Exit ?" )
    if q == "y":
        break
