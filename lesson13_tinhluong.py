def tinhluong(giolam, luonggio):
    tongluong = giolam * luonggio
    return tongluong

def inthongtin(ten, giolam, luonggio, tongluong):
    print("Thông tin nhân viên:")
    print("Tên:", ten)
    print("Số giờ làm:", giolam)
    print("Mức lương giờ:", luonggio)
    print("Tổng tiền lương:", tongluong)

# Nhập thông tin từ người dùng
ten = input("Nhập tên nhân viên: ")
giolam = float(input("Nhập số giờ làm: "))
luonggio = float(input("Nhập mức lương giờ: "))

# Tính tổng tiền lương
tongluong = tinhluong(giolam, luonggio)

# In thông tin nhân viên
inthongtin(ten, giolam, luonggio, tongluong)
