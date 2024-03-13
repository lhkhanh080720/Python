a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))

if a == 0:
    if b == 0:
        if c ==0: 
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        print("Nghiệm của phương trình là: ", -c/b)
else:
    denta = float(b**2 - 4*a*c)
    if denta > 0:
        print("Phương trình có 2 nghiệm phân biệt là: x1 =", float((-b + denta**(1/2))/2/a), " và x2 =", float((-b - denta**(1/2))/2/a))
    else:
        if denta == 0:
            print("Phương trình có nghiệm kép là: x =", -b / (2*a))
        else:
            print("Phương trình vô nghiệm.")