a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("3 giá trị không phải độ dài tam giác")
else:
    if a + b > c and a + c > b and b + c > a:
        P = a + b + c
        S = (P/2 * (P/2 - a) * (P/2 - b) * (P/2 - c))**(1/2)
        print("Chu vi tam giac la: ", P)
        print("Dien tich tam giac la: ", S)
    else:
        print("3 giá trị không phải độ dài tam giác")