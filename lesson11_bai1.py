ho_ten = input("Nhập họ và tên của người bạn thích nhất: ")


# Tìm vị trí của khoảng trắng đầu tiên
vi_tri_khoang_trang = ho_ten.find(' ')


# Duyệt qua các ký tự từ đầu xâu đến vị trí khoảng trắng
ho = ''
for i in range(vi_tri_khoang_trang):
    ho += ho_ten[i]


print("Họ của người bạn là:", ho)