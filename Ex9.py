a = int(input("Năm: "))

if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
    print("Năm nhuận.")
else: 
    print("Không phải là năm nhuận.")