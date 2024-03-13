a = int(input("Nhập số nguyên có 2 chữ số: "))

a1 = int(a/10)
a2 = int(a%10)

if a1 == 2:
    at1 = "hai"
if a1 == 3:
    at1 = "ba"
if a1 == 4:
    at1 = "bốn"
if a1 == 5:
    at1 = "năm"
if a1 == 6:
    at1 = "sáu"
if a1 == 7:
    at1 = "bảy"
if a1 == 8:
    at1 = "tám"
if a1 == 9:
    at1 = "chín"  

if a2 == 1:
    at2 = "mốt"
if a2 == 2:
    at2 = "hai"
if a2 == 3:
    at2 = "ba"
if a2 == 4:
    at2 = "bốn"
if a2 == 5:
    at2 = "năm"
if a2 == 6:
    at2 = "sáu"
if a2 == 7:
    at2 = "bảy"
if a2 == 8:
    at2 = "tám"
if a2 == 9:
    at2 = "chín" 

if a1 == 1:
    if a2 == 0:
        print("mười")
    else:
        print("mười", at2)
else:
    if a2 == 0:
        print(at1, "mươi")
    else:
        print(at1, "mươi", at2)