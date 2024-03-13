a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))

max = float(a)
if max < b:
    max = b
if max < c:
    max = c

if a + b + c - max > max:
    P = a + b + c
    S = (P/2 * (P/2 - a) * (P/2 - b) * (P/2 - c))**(1/2)
    print("Chu vi tam giac la: ", P)
    print("Dien tich tam giac la: ", S)
else:
    print("3 gia tri khong phai do dai tam giac")