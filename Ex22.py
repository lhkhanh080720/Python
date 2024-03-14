a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))
d = float(input("Nhập giá trị cho d: "))
m = float(input("Nhập giá trị cho m: "))
n = float(input("Nhập giá trị cho n: "))

D = float(a*d-b*c)
Dx = float(m*d-b*n)
Dy = float(a*n-m*c)

if D == 0:
    if Dx == Dy == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Phương trình có 2 nghiệm là x =", Dx/D, "và y =", Dy/D)