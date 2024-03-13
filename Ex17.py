a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))
d = float(input("Nhập giá trị cho d: "))
e = float(input("Nhập giá trị cho e: "))

if b / a == c / b and c / b == d / c and d / c == e / d:
    print("Đây là cấp số nhân.")
else:
    print("Đây không phải là cấp số nhân.")