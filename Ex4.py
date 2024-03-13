a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))
d = float(input("Nhập giá trị cho d: "))
e = float(input("Nhập giá trị cho e: "))

min = float(a)
if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
if min > e:
    min = e

print("Số nhỏ nhất trong 5 số là: ", min)