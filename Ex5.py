a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))

if a == 0:
    if b ==0: 
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    print("Nghiệm của phương trình là: ", -b/a)