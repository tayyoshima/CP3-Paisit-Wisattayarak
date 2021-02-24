usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "guest" and passwordInput == "1234":
    print("Login Success")
    print("----- Welcome to ZONE TEEN Shop -----")
    print("1. ลูกอม ตรา โบวตัน(ยาสีฟันคอลเกต สบู่วิเศษจริงๆ) ราคา 1 บาท/1 ชิ้น")
    print("2. ขนม ตรา เหล่                          ราคา 10 บาท/1 ชิ้น")
    print("3. ยาดม ตรา โอ๊ยเซียน                      ราคา 50 บาท/1 ชิ้น")
    print("4. ยาหม่อง ตรา ถ้วยทึง                      ราคา 30 บาท/1 ชิ้น")
    print("--------------------------------------------------------")
    userSelected = int(input("ท่านลูกค้าต้องการสินค้าหมายเลข >> "))
    if userSelected == 1:
        amout = int(input("ต้องการ ลูกอม ตรา โบวตัน(ยาสีฟันคอลเกต สบู่วิเศษจริงๆ) ราคา 1 บาท จำนวนกี่ชิ้นค่ะ >> "))
        print("ราคารวมทั้งหมด คือ "+str(amout*1)+" บาท")
    elif userSelected == 2:
        amout = int(input("ต้องการ ขนม ตรา เหล่ ราคา 10 บาท จำนวนกี่ชิ้นค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 10) + " บาท")
    elif userSelected == 3:
        amout = int(input("ต้องการ ยาดม ตรา โอ๊ยเซียน ราคา 50 บาท จำนวนกี่ชิ้นค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 50) + " บาท")
    elif userSelected == 4:
        amout = int(input("ต้องการ ยาหม่อง ตรา ถ้วยทึง ราคา 30 บาท จำนวนกี่ชิ้นค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 30) + " บาท")
    else :
        print("ไม่มีรหัสสินค้าในรายการ")
else:
    print("Username or Password is Incorrect.")