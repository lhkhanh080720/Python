a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))
d = float(input("Nhập giá trị cho d: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("4 giá trị không phải độ dài tứ giác")
else:
    if a + b + c > d and a + b + d > c and b + c + d > a and a + c + d > b:
        print("Đây là tứ giác")
    else:
        print("4 giá trị không phải độ dài tứ giác")