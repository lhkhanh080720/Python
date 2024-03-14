a = float(input("Nhập giá trị cho khối nước tiêu thụ: "))
b = int(input("Nhập giá trị cho số nhân khẩu: "))

if float(a/b) <= 4:
    tien = 6700 * a
else:
    if float(a/b) > 4 and float(a/b) <= 6:
        tien = 12900 * a
    else:
        tien = 14400 * a

print("Số tiền phải trả là: ", tien, "VNĐ")