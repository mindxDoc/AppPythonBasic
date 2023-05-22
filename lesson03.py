print("Chào mừng đến với Currency Converter - chuyển đổi tiền tệ")

dollar = input("Vui lòng nhập số tiền cần chuyển (đô la Mỹ): $")

print("Số tiền sẽ được quy đổi ra Việt Nam Đồng")
vnd = int(dollar) * 23442

print("$" + dollar + " quy đổi ra được " + str(vnd) + "đ")