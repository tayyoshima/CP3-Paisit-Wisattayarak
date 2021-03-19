from forex_python.converter import CurrencyRates
import datetime
c = CurrencyRates()

def conversionRate():
    while True:
        m = input("ระบุค่าเงินที่คุณต้องการแปลง : ")
        try:
            print("Conversion rate from", m)
            t = input("to ... : ")
            print("1", m, "=", c.get_rate(m, t), t)
            break
        except:
            print("โปรดระบุค่าเงินใหม่")

def rateToday():
    money = input("ระบุค่าเงินที่คุณต้องการจะเทียบ : ")
    date_obj = datetime.datetime.now()
    print("เวลาที่ทำการเทียบ ณ ปัจจุบัน "+str(date_obj))
    date = c.get_rates(money, date_obj)
    print(date)


print("ยินดีต้อนรับ สู่โปรแกรมเปรียบเทียบค่าเงิน")
while True :
    print("----กด 1 ดูสถานะค่าเงินของวันนี้----")
    print("----กด 2 แปลงค่าเงินของวันนี้------")
    choice = input("เลือกหมายเลขบริการที่ต้องการ : ")
    if choice == "1" :
        rateToday()
    elif choice == "2" :
        conversionRate()
    else:
        print("ไม่มีบริการที่ต้องการ กรุณาเลือกใหม่ ...")
