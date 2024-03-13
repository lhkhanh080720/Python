x = int(input("Số kg cam là: "))

giatien = 0

if x <= 5:
    giatien =  x * 12000
else:
    giatien += 5 * 12
    if x >= 6 and x <= 10:
        giatien += (x-10) * 10000
    else:
        giatien += 10 * 10000
        if x >= 11:
            giatien += (x-10) * 8000

print("Số tiền phải trả là:", giatien, "VNĐ")