thong_tin_dang_nhap = "MindX:12345"
username, password = thong_tin_dang_nhap.split(':')
nhap_username = input("Nhập tên đăng nhập: ")
nhap_password = input("Nhập mật khẩu: ")
while nhap_username != username and nhap_password != password:
    print("Thông tin đăng nhập chưa chính xác, vui lòng thử lại.")
    nhap_username = input("Nhập tên đăng nhập: ")
    nhap_password = input("Nhập mật khẩu: ")
print("Đăng nhập thành công")