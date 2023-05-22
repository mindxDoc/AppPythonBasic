num = int(input("Nhập kích thước bảng phép nhân bạn muốn: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()  # Add a blank line after each row
