users = []

def register():
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    check_register = True;
    if not validate_password(password):
        print("Mật khẩu không hợp lệ. Mật khẩu phải có ít nhất 6 ký tự.")
        return
    
    for user in users:
            stored_username, stored_password = user.split(":")
            if stored_username == username:
                check_register = False;
    if check_register == True:
        users.append(username + ":" + password)
        print("Đăng ký thành công")
    else:
        print("Tài khoản đã tổn tại")
        
def validate_password(password):
    return len(password) >= 6

def login():
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    check_login = False;
    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username and stored_password == password:
            check_login = True;
    
    if check_login == True:
        print("Đăng nhập thành công")
    else:
        print("Đăng nhập không thành công. Sai tên người dùng hoặc mật khẩu")

def main():
    while True:
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Nhập lựa chọn của bạn (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Lựa chọn không hợp lệ.")

main()