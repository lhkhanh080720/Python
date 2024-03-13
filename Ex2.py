a = float(input("Nhập giá trị cho Toán: "))
b = float(input("Nhập giá trị cho Lý: "))
c = float(input("Nhập giá trị cho Hóa: "))
d = float(input("Nhập giá trị cho Văn: "))
e = float(input("Nhập giá trị cho Anh: "))

diemTB = float((a * 2 + b + c + d * 2 + e)/7)

if diemTB >= 8:
    print("Giỏi")
if diemTB >= 6.5 and diemTB < 8:
    print("Khá")
if diemTB >= 5 and diemTB < 6.5:
    print("Trung bình")
if diemTB >= 3.5 and diemTB < 5:
    print("Yếu")
if diemTB < 3.5:
    print("Kém")