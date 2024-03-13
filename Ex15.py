a = int(input("Nhập giá trị cho Ngày = "))
b = int(input("Nhập giá trị cho Tháng = "))
c = int(input("Nhập giá trị cho Năm = "))

if a <= 0 or b <= 0 or c <= 0:
    print("Ngày, Tháng, Năm không hợp lệ")
else:
    if c % 4 == 0:
        if b == 2 and a > 29:
            print("Ngày không hợp lệ")
        else:
            print("Ngày, Tháng, Năm hợp lệ")
    else:
        if b == 2 and a > 28:
            print("Ngày không hợp lệ")
        else:
            print("Ngày, Tháng, Năm hợp lệ")

    if b > 12:
        print("Tháng không hợp lệ")
    else:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
            if a > 31:
                print("Ngày không hợp lệ")
            else:
                print("Ngày, Tháng, Năm hợp lệ")
        else:
            if b == 4 or b == 6 or b == 9 or b == 11:
                if a > 30:
                    print("Ngày không hợp lệ")
                else:
                    print("Ngày, Tháng, Năm hợp lệ")
