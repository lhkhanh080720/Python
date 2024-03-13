x = int(input("Số tiêu thụ điện: "))

giatien = 0.0

if x >=0 and x <= 50:
    giatien =  x * 1.484
else:
    giatien += 50 * 1.484
    if x >= 51 and x <= 100:
        giatien += (x-50) * 1.533
    else:
        giatien += 100 * 1.533
        if x >= 101 and x <= 200:
            giatien += (x-100) * 1.786
        else:
            giatien += 200 * 1.786
            if x >= 201 and x <= 300:
                giatien += (x-200) * 2.242
            else:
                giatien += 300 * 2.242
                if x >= 301 and x <= 400:
                    giatien += (x-300) * 2.503
                else:
                    giatien += 400 * 2.503
                    if x >= 401:
                        giatien += (x-400) * 2.587

print("Số tiền phải trả là:", giatien, "VNĐ")