import math

a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))

if(a + b + c - max(a, b ,c) > max(a, b ,c)):
    P = a + b + c
    S = math.sqrt(P/2 * (P/2 - a) * (P/2 - b) * (P/2 - c))
    print("Chu vi tam giac la: ", P)
    print("Dien tich tam giac la: ", S)
else:
    print("3 gia tri khong phai do dai tam giac")