def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login Successfully")
        showMenu()
    else:
        print("Login Failed!!")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    button = menuSelect()
    if button==1 :
        sum = int(input("โปรดระบุราคาที่ต้องการคำนวณ : "))
        print(vatCalculator(sum))
    elif button==2 :
        print(priceCalculator())
    else :
        print("กรุณากรอกเลขใหม่ค่ะ")
        showMenu()

def menuSelect():
    userSelected = int(input(">> "))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
