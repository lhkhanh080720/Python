a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
r = float(input("Nhập giá trị cho r: "))
x = float(input("Nhập giá trị cho x: "))
y = float(input("Nhập giá trị cho y: "))

d = float(((a-x)**2 + (b-y)**2)**(1/2))

if d < r:
    print("Điểm I nằm trong đường tròn")
else:
    if d == r:
        print("Điểm I nằm trên đường tròn")
    else:
        print("Điểm I nằm ngoài đường tròn")