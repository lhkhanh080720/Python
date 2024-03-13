a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("Nhập giá trị cho c: "))
    
max = float(a)
if max < b:
    max = b
if max < c:
    max = c

if a <= 0 or b <= 0 or c <= 0:
    print("3 giá trị không phải độ dài tam giác")
else:
    if a + b + c - max > max:
        if a == b and a == c:
            print("Đây là độ dài 3 cạnh của tam giác đều")
        else:
            print("3 giá trị không phải độ dài tam giác, nhưng không phải tam giác đều")
    else:
        print("3 giá trị không phải độ dài tam giác")