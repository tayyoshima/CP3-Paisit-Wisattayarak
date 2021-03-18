systemMenu = {"ยำไก่แซ่บ": 40, "ก๋วยเตี๋ยวเป็ด": 50, "ปลาทูทอด": 30, "เกี๊ยวทอด": 20}
menuList = []

def showBill():
    sum = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        sum = sum + int(menuList[number][1])
    print("Total : ", sum)

while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()