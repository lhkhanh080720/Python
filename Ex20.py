b = int(input("Nhập giá trị cho Tháng = "))
c = int(input("Nhập giá trị cho Năm = "))

if c % 400 == 0 or (c % 4 == 0 and c % 100 != 0):
    if b == 2:
        print("Tháng 2 Năm", c, "có 29 ngày.")
else:
    if b == 2:
        print("Tháng 2 Năm", c, "có 28 ngày.")
    else:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
            print("Tháng", b, "Năm", c, "có 31 ngày.")
        else:
            if b == 4 or b == 6 or b == 9 or b == 11:
                print("Tháng", b, "Năm", c, "có 30 ngày.")
